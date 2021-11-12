import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash 
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("pages/home.html", API_KEY=retrieve_api_key())


@app.route("/destinations")
def dive_destinations():
    destinations = mongo.db.destination.find()
    return render_template("pages/dive_destinations.html", destinations=destinations)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    destinations = list(mongo.db.destination.find({"$text": {"$search": query}}))
    return render_template("pages/dive_destinations.html", destinations=destinations)


@app.route("/map")
def dive_map():
    return render_template("pages/dive_map.html", API_KEY=retrieve_api_key())


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into "session" cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("pages/registration_page.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            #ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                #invalid password match
                flash("Incorrect Username and/or Password")
                #redirect is used to redirect a user back to another page
                return redirect(url_for("login"))
            
        else:
            #username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("home"))



@app.route("/edit_username/<user_id>", methods=["GET", "POST"])
def update_username(user_id):
    if request.method == "POST":
        # check if username already exists in db
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        if username:
            flash("Username already exists")
            return redirect(url_for("profile"))
        
        update_username = {
            "username": request.form.get("username").lower()
        }

    mongo.db.users.update(username, update_username)
    flash("Username Succesfully Updated!")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("pages/profile.html", username=username)

    return redirect(url_for("home"))


@app.route("/logout")
def logout():
    #remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("home"))


def retrieve_api_key():
    return os.environ.get("API_KEY")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
