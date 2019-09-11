from flask import Flask, render_template, redirect, session, url_for, request
from flask_pymongo import PyMongo
import mission as m
import json

app = Flask(__name__)

mongo = PyMongo(app, uri = "mongodb://localhost:27017/mars")

@app.route("/")
def index():
    data = mongo.db.data.find_one()    
    text = 'Mission to Mars'
    return render_template("index.html", text=text, mars=data)

@app.route("/scrape")
def scraper():
    m.Mission_to_mars.url = 'https://mars.nasa.gov/news/'
    m.Mission_to_mars.news()

    m.Mission_to_mars.url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    m.Mission_to_mars.featuredImageUrl()

    m.Mission_to_mars.url = 'https://twitter.com/marswxreport?lang=en'
    m.Mission_to_mars.marsWeather()

    m.Mission_to_mars.url = 'https://space-facts.com/mars/'
    m.Mission_to_mars.htmlTable()

    m.Mission_to_mars.url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    m.Mission_to_mars.hemisphereImageUrls()    
        
    data = {'news_title' : m.Mission_to_mars.news_title, 'news_p': m.Mission_to_mars.news_p,\
                'featured_image_url' : m.Mission_to_mars.featured_image_url,\
                'mars_weather' : m.Mission_to_mars.mars_weather,\
                'html_table': m.Mission_to_mars.html_table,\
                'hemisphere_image_urls': m.Mission_to_mars.hemisphere_image_urls}
     
    mongo.db.data.update({}, data, upsert=True)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)