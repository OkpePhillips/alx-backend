#!/usr/bin/env python3
"""
Module for the localisation
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """
    Returns an index page
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
