from flask import Flask, render_template, request, jsonify, make_response, redirect
from flask_frozen import Freezer

import sys


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

freezer = Freezer(app)

@app.route('/')
def page_home():
    return render_template("index.html")

@app.route('/events/wamo1.html')
def page_wamo1():
    return render_template("wamo1.html")

if __name__ == "__main__":
    freezer.freeze()
    #app.run(port=8000)