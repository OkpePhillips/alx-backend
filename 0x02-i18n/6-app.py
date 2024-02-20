#!/usr/bin/env python3
"""
Module for the localisation
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


class Config:
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
    function to use a user’s preferred local if it is supported
    """
    if 'locale' in request.args:
        requested_locale = request.args['locale']
        if requested_locale in app.config['LANGUAGES']:
            return requested_locale
    # Check for user's preferred locale
    if hasattr(g, 'user') and g.user and g.user[
            'locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    # Check for locale from request header
    header_locale = request.headers.get('Accept-Language')
    if header_locale:
        header_locale = header_locale.split(',')[0]
        if header_locale in app.config['LANGUAGES']:
            return header_locale
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index():
    """
    Returns an index page
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
