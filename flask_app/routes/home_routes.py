# flask_app/routes/home_routes.py

from flask import Blueprint,  render_template

home_routes = Blueprint("home_routes", __name__)

# add def index():

@home_routes.route('/')
def hello_world():
    print("You visited the homepage")
    #return 'Hello, World!'
    return render_template("prediction_form.html")

@home_routes.route('/about')
def about():
    print("You visited the About-Me page")
    return "<h2 style = 'color:red'> About Me (TODO)</h2>"
