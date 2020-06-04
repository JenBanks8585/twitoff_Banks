# flask_app/routes/twitter_routes.py

from flask import Blueprint, jsonify, render_template , request, flash, redirect
from flask_app.models import db, User, TweetMsg, parse_records
from flask_app.services.basilica_service import connection as basilica_connection
from flask_app.services.twitter_service import api as twitter_api

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

    # fetch embeddings for each tweet
    #counter = 0
    for status in statuses:
        print(status.full_text)
        print("----")
        #print(dir(status))
        # get existing tweet from the db or initialize a new one:
        db_tweet = Tweet.query.get(status.id) or Tweet(id=status.id)
        db_tweet.user_id = status.author.id # or db_user.id
        db_tweet.full_text = status.full_text
        
        #fetching corresponding embedding:
        embedding = basilica_connection.embed_sentence(status.full_text, model="twitter") # todo: prefer to make a single request to basilica with all the tweet texts, instead of a request per tweet
        #embedding = embeddings[counter]
        #print(len(embedding))
        db_tweet.embedding = embedding
        db.session.add(db_tweet)
        #counter+=1

    db.session.commit()
    return f"FETCHED {screen_name} OK"

    # TODO: store tweets in database (w/embeddings)


    return jsonify({"user": user._json, "num_tweets": len(statuses)})

