# flask_app/routes/tweet_routes.py

from flask import Blueprint, jsonify, render_template , request, flash, redirect
from flask_app.models import db, Tweet, parse_records

tweet_routes = Blueprint("tweet_routes", __name__)

@tweet_routes.route("/tweets.json")
def list_tweets():

    tweet_records = Tweet.query.all()
    print(tweet_records)
    
    tweets_response = parse_records(tweet_records)
    return jsonify(tweets_response)

@tweet_routes.route("/tweets")
def list_tweets_for_humans():

    tweet_records = Tweet.query.all()
    print(tweet_records)
   
    return render_template("tweets.html", message="Available tweets", tweets=tweet_records)

@tweet_routes.route("/tweets/new")
def new_tweet():
    return render_template("new_tweet.html")

@tweet_routes.route("/tweets/create", methods=["POST"])
def create_tweet():
    print("FORM DATA:", dict(request.form)) #>{"tweet_string":"__". "twit_user":"___"}

    new_tweet = Tweet(twit=request.form["tweet_string"], twit_user=request.form["twit_user"])
    db.session.add(new_tweet)
    db.session.commit()


    flash(f"Tweet '{new_tweet.twit}' created successfully!", "dark")
    return redirect(f"/tweets")
