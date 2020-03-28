from flask import render_template, Blueprint

from app import app

blueprint = Blueprint('home', __name__)


@app.route('/')
def home():
    return render_template('base.html')
