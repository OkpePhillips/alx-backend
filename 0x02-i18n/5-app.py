#!/usr/bin/env python3
"""
Module for the localisation
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _


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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """
    Returns the user
    """
    return users.get(user_id)


@app.before_request
def before_request():
    """
    Sets the logged in user as a global variable
    """
    user_id = int(request.args.get('login_as', 0))
    g.user = get_user(user_id)


@babel.localeselector
def get_locale():
    """
    Returns a translation according to location
    """
    if 'locale' in request.args:
        requested_locale = request.args['locale']
        if requested_locale in app.config['LANGUAGES']:
            return requested_locale
    return request.accept_languages.best_match(
            app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Returns an index page
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
