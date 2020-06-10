from flask import Blueprint, jsonify, request , render_template, flash, redirect
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from flask_app.statsmodels import load_model
from flask_app.models import User, TweetMsg
from flask_app.services.basilica_service import connection as basilica_connection

stats_routes = Blueprint("stats_routes", __name__)


@stats_routes.route("/stats/iris")
def iris(): 
    X, y = load_iris(return_X_y=True)
    clf = load_model()
    result = str(clf.predict(X[:2, :]))
    print("PREDICTION", result)
    return result


@stats_routes.route("/stats/predict", methods = ["POST"])
def twitoff_predict(): 
   
    print("PREDICT ROUTE...")
    print("FORM DATA:", dict(request.form))
    #> {'screen_name_a': 'elonmusk', 'screen_name_b': 's2t2', 'tweet_text': 'Example tweet text here'}
    screen_name_a = request.form["screen_name_a"]
    screen_name_b = request.form["screen_name_b"]
    tweet_text = request.form["tweet_text"]

    print(screen_name_a, screen_name_b, tweet_text)

    
    # train a model
    tweet_embeddings=[]
    tweet_labels=[]

    user_a = User.query.filter(User.screen_name == screen_name_a).one()
    user_b = User.query.filter(User.screen_name == screen_name_b).one()
    tweets_a = user_a.tweets
    tweets_b = user_b.tweets
    all_tweets = tweets_a + tweets_b

    for tweet in all_tweets:
        tweet_embeddings.append(tweet.embedding)
        tweet_labels.append(tweet.user.screen_name)
    
    print("EMBEDDINGS", len(tweet_embeddings), "LABELS", len(tweet_labels))
    #breakpoint()
    
    classifier = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial')
    classifier.fit(tweet_embeddings, tweet_labels)


    # make a prediction and return it

    example_tweet_embedding= basilica_connection.embed_sentence(tweet_text, model = "twitter")
    result = classifier.predict([example_tweet_embedding])
    print("RESULT", result [0])

    return render_template("prediction_results.html", 
        screen_name_a = screen_name_a, 
        screen_name_b = screen_name_b, 
        tweet_text = tweet_text,
        screen_name_most_likely = result[0])





    return "OK"

