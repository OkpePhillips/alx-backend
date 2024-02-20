#!/usr/bin/env python3
"""
Module for the localisation
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Returns a translation according to location
    """
    return request.accept_languages.best_match(
            app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Returns an index page
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
