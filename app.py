from flask import Flask, request, render_template
from random import choice, sample
# from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)

# app.config['SECRET_KEY'] = "shiddy"
# debug = DebugToolbarExtension(app)

@app.route('/')
def root():
    return render_template('home.html')

@app.route('/story')
def story():
    place  = request.args["place"]
    noun  = request.args["noun"]
    verb  = request.args["verb"]
    adjective  = request.args["adjective"]
    plural_noun  = request.args["plural_noun"]
    return render_template('story.html', place = place, noun = noun, verb = verb, adjective = adjective, plural_noun = plural_noun)

