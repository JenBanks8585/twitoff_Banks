# flask_app/routes/admin_routes.py

from flask import Blueprint, jsonify, request , render_template, flash, redirect

from flask_app.models import db

admin_routes = Blueprint("admin_routes", __name__)

API_KEY = "abc123" # set as secret env var


# GET /admin/db/reset?api_key=abc123
@admin_routes.route("/admin/db/reset")
def reset_db():
    print("URL PARAMS", dict(request.args))

    if "api_key" in dict(request.args) and request.args["api_key"] == API_KEY:
        print(type(db))
        db.drop_all()
        db.create_all()
        return jsonify({"message": "DB RESET OK"})
    else:
        print("PERMISSION DENIED")
        flash("OOPS Permission Denied")
        return redirect("/")