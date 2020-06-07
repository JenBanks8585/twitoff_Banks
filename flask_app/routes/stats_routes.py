from flask import Blueprint, jsonify, request , render_template, flash, redirect
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from flask_app.models import db

stats_routes = Blueprint("stats_routes", __name__)


@stats_routes.route('/stats/iris')
def iris(): 
    X, y = load_iris(return_X_y=True)
    clf = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial')
    clf.fit(X, y)
    result = str(clf.predict(X[:2, :]))
    print("PREDICTION", result)
    return result