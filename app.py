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


# Home page
@app.route("/")
def home():
    return render_template("pages/home.html", API_KEY=retrieve_api_key())


# Route to dive destinations
@app.route("/destinations")
def dive_destinations():
    destinations = list(mongo.db.destination.find())
    return render_template(
        "pages/dive_destinations.html", destinations=destinations)


# Search function
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    destinations = list(mongo.db.destination.find(
        {"$text": {"$search": query}}))
    return render_template(
        "pages/dive_destinations.html", destinations=destinations)


# Route to map site
@app.route("/map")
def dive_map():
    return render_template("pages/dive_map.html", API_KEY=retrieve_api_key())


# Register function
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


# Login function
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                # redirect is used to redirect a user back to another page
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("home"))


# # WIP. User not updating as expected
# @app.route("/edit_username", methods=["GET", "POST"])
# def edit_username():
#     if request.method == "POST":
#         # check if username already exists in db
#         existing_user = mongo.db.users.find_one(
#             {"username": request.form.get("username").lower()})

#         update_username = {
#             "username": request.form.get("username").lower()
#         }

#         try:
#             mongo.db.users.update(update_username)
#             flash("Username successfully updated Successful!")
#             session["user"] = request.form.get("username").lower()

#             return redirect(url_for("profile", username=session["user"]))
#         except:
#             flash("Error updating the username")
#         # put the new user into "session" cookie

#     return render_template("pages/profile.html")


# Profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    destinations = list(mongo.db.destination.find({"created_by": username}))

    if session["user"]:
        return render_template(
            "pages/profile.html", destinations=destinations, username=username)

    return redirect(url_for("home"))


# Log out function
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("home"))


# Add a dive function
@app.route("/add_dive", methods=["GET", "POST"])
def add_dive():
    if request.method == "POST":
        dive = {
            "continent": request.form.get("continent"),
            "country": request.form.get("country"),
            "place": request.form.get("place"),
            "dive_description": request.form.get("dive_description"),
            "image_of_place": request.form.get("image_of_place"),
            "created_by": session["user"]
        }

        mongo.db.destination.insert_one(dive)
        flash("Your Dive is added to your collection!")
        return redirect(url_for(
                        "profile", username=session["user"]))

    continents = mongo.db.continents.find().sort("continent_name", 1)
    return render_template("pages/add_dive.html", continents=continents)


# Edit Dive Function
@app.route("/edit_dive/<destination_id>", methods=["GET", "POST"])
def edit_dive(destination_id):
    if request.method == "POST":
        dive = {
            "continent": request.form.get("continent"),
            "country": request.form.get("country"),
            "place": request.form.get("place"),
            "dive_description": request.form.get("dive_description"),
            "image_of_place": request.form.get("image_of_place"),
            "created_by": session["user"]
        }

        mongo.db.destination.update({"_id": ObjectId(destination_id)}, dive)
        flash("Your Dive is updated!")
        return redirect(url_for(
                        "profile", username=session["user"]))

    destination = mongo.db.destination.find_one(
        {"_id": ObjectId(destination_id)})
    continents = mongo.db.continents.find().sort("continent_name", 1)
    return render_template(
        "pages/edit_dive.html", destination=destination, continents=continents)


# Delete Dive Function
@app.route("/delete_dive/<destination_id>")
def delete_dive(destination_id):
    mongo.db.destination.remove({"_id": ObjectId(destination_id)})
    flash("Your Dive is updated!")
    return redirect(url_for(
                    "profile", username=session["user"]))

# # Function does not work after i add new entries to the database
# # Changing list to map
# def group_by_continent(destination):
#     new_dest = {}
#     for destination in destinations:
#         if destination["continent"] in new_dest:
#             new_dest[destination["continent"]].append(destination)
#         else:
#             new_dest[destination["continent"]] = [destination]
#     return new_dest


# Get API_KEY from env file
def retrieve_api_key():
    return os.environ.get("API_KEY")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
