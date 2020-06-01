from flask import Flask

#Part 2
# flask_app/__init__.py

from flask_app.routes.home_routes import home_routes
from flask_app.routes.book_routes import book_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)