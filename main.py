from flask import Flask, render_template, request, jsonify, make_response, redirect
from flask_frozen import Freezer

import sys
import os


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

freezer = Freezer(app)

@app.route('/')
def page_home():
    return render_template("index.html")

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
    if "WAMODEV" in os.environ:
        app.run(port=8000)
    else:
        freezer.freeze()
