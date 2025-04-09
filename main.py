from flask import Flask, render_template, request, jsonify, make_response, redirect
from flask_frozen import Freezer

import sys
import os


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

freezer = Freezer(app)

from PIL import Image, ImageDraw, ImageOps

def add_bg(image_path, output_path):
    image = Image.open(image_path).convert("RGBA")
    image = image.resize((365,365))
    image.save(output_path)

    width, height = image.size

    # Create a mask with an alpha channel
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)

    # Draw a white filled circle
    draw.ellipse((0, 0, width, height), fill=255)

    # Ensure the mask is not larger than the image
    mask = mask.resize((width, height), Image.LANCZOS)

    # Apply the mask to the image
    image.putalpha(mask)

    background = Image.open('static/Background.png').convert("RGBA")
    foreground = image.convert("RGBA")

    paddingx = (background.size[0] - foreground.size[0]) // 2
    paddingy = (background.size[1] - foreground.size[1]) // 2
    foreground = ImageOps.expand(foreground, border=(paddingx, paddingy, paddingx, paddingy), fill=(0, 0, 0, 0))
    # Ensure the foreground image is the same size as the background or resize it
    #foreground = foreground.resize(background.size)

    foreground = foreground.resize(background.size)

    # Overlay the images
    output = Image.alpha_composite(background, foreground)

    # Save the output image
    output.save(output_path.split(".")[0] + ".png")

@app.route('/')
def page_home():
    return render_template("index.html")

@app.route('/whyus.html')
def page_whyus():
    return render_template("whyus.html")

@app.route('/events/<event>.html')
def page_events(event):
    return render_template(f"events/{event}.html")

@freezer.register_generator
def page_events():
    for dirpath, dirnames, filenames in os.walk("templates/events"):
        for file in filenames:
            yield {'event': os.path.splitext(file)[0]}

@app.route('/404.html') # Hack for flask freeze
def not_found():
    return render_template('404.html')

if __name__ == "__main__":
    if True:
        app.run(port=80, host="0.0.0.0")
    else:

        for dirpath, dirnames, filenames in os.walk("static/pfps"):
            for file in filenames:
                add_bg(dirpath + "/" + file, dirpath + "/" + file)

        freezer.freeze()
