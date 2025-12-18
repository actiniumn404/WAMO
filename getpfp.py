import os
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


# for dirpath, dirnames, filenames in os.walk("static/pfps"):
#     for file in filenames:
#         add_bg(dirpath + "/" + file, dirpath + "/" + file)

add_bg("static/pfps_raw/vivaanpfp.png", "static/pfps/vivaanpfp.png")