# flask_app/routes/twitter_routes.py

from flask import Blueprint, jsonify, render_template , request, flash, redirect
from flask_app.models import db, Book, parse_records

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>/fetch")

def fetch_user_data(screen_name):
    print(screen_name)

    # TODO: fetch user info

    # TODO: store user infor in database

    # TODO: fetch their tweets

    # TODO: fetch embeddings for each tweet

    # TODO: store tweets in database (w/embeddings)


    return f"FETCHED {screen_name} OK"

