# flask_app/routes/twitter_routes.py

from flask import Blueprint, jsonify, render_template , request, flash, redirect
from flask_app.models import db, User, TweetMsg, parse_records

from web_app.services.twitter_service import api as twitter_api

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>/fetch")

def fetch_user_data(screen_name):
    print("FETCHING...",screen_name)

    # fetch user info
    user= twitter_api.get_user(screen_name)

    # TODO: store user infor in database
    db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)
    db_user.screen_name=twitter_user.screen_name
    db_user.name=twitter_user.name
    db_user.location=twitter_user.location
    db_user.followers_count=twitter_user.followers_count

    db.session.add(db_user)
    db.session.commit()

    # fetch their tweets
    statuses = twitter_api.user_timeline("elonmusk", count = 35)

    # TODO: fetch embeddings for each tweet

    # TODO: store tweets in database (w/embeddings)


    return jsonify({"user": user._json, "num_tweets": len(statuses)})

