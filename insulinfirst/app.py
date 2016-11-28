import os

from flask import Flask, render_template, redirect
from datetime import datetime, timedelta

from insulinfirst.extensions import db
from insulinfirst.models import Product


BASE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')


def create_app(package_name, settings_override=None):
    """
    This is a starter function for using the Flask application factory pattern.

    :param settings_override: settings to override the default
    :param package_name: typically __name__ for the package_name
    :return: the application instance
    """

    app = Flask(__name__, instance_relative_config=True)

    # For local
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://BHarris:@localhost:5432/strips'

    # For Heroku

    #app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

    if settings_override:
        app.config.from_object(settings_override)


    # Init extensions
    db.init_app(app)

    # You'll want to probably turn this into a blueprint eventually.
    # http://flask.pocoo.org/docs/0.11/blueprints/#blueprints
    @app.route("/")
    def home():
        products = db.session.query(Product).filter(Product.product_type == 'Test Strips').order_by(Product.product_price_per_strip)
        return render_template('base.html',
                               products=products)

    return app
