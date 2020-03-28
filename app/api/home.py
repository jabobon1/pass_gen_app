from flask import render_template, Blueprint

from app import app

blueprint = Blueprint('home', __name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')