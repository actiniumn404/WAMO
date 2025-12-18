from flask import Flask, render_template, request, jsonify, make_response, redirect
from flask_frozen import Freezer

import sys
import os
import json


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

freezer = Freezer(app)

@app.route('/')
def page_home():
    return render_template("index.html")

@app.route('/team.html')
@app.route('/team/')
def page_whyus():
    return render_template("team.html", members=members, core_members=core_members)

@app.route('/testimonials.html')
@app.route('/testimonials/')
def page_testimonials():
    return render_template("testimonials.html")

@app.route('/events/<event>.html')
@app.route('/events/<event>/')
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

# Load data
with open("static/members.json", 'r') as file:
    members = json.loads(file.read())

with open("static/core_members.json", 'r') as file:
    core_members = json.loads(file.read())

if "WAMODEV" in os.environ:
    app.run(port=80, host="0.0.0.0")
else:
    freezer.freeze()

