#Import Dependencies
from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/scrape")
def scrape():
    mars_facts_data = mongo.db.mars_facts_data
    mf_data = scrape_mars.scrape()
    mars_facts_data.update({}, mf_data, upsert=True)
    return redirect("/", code=302)

@app.route("/")
def index():
    mars_facts_data = mongo.db.mars_facts_data.find_one()
    return render_template("index.html", mars_facts_data=mars_facts_data)