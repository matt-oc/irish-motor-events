import os
from flask import (
    Flask, flash, render_template, redirect, request, url_for, make_response)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import random
from datetime import datetime, timedelta

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_events")
def index():

    events = mongo.db.events.find()
    return render_template("events.html", events=events)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)