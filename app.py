from flask import Flask, render_template, request, json
from client import ClarifaiApi
from random import randint
from key import ARTSY_TOKEN
import requests
import simplejson

app = Flask(__name__)

@app.route("/")
def home():
    top_tags(get_artwork())
    return render_template("test.html", message="test", link="test")

def top_tags(url):
    clarifai_api = ClarifaiApi()
    result = clarifai_api.tag_image_urls(str(url).replace("medium", "large"))
    top_three = result['results'][0]['result']['tag']['classes'][0:3]
    return top_three

def get_artwork():
    args = {"offset": randint(0, 100), "size":1}
    headers = {"X-Xapp-Token": ARTSY_TOKEN}
    arts = requests.get('https://api.artsy.net/api/artworks',params=args, headers=headers)  
    art_json = simplejson.loads(arts.text)
    link = art_json['_embedded']['artworks'][0]['_links']['thumbnail']['href']
    print link
    return link
    
def get_post_message(tags, artist_name, artist_nationality, medium, artwork_name):
    message = "Wow! " + artwork_name + " by " + artist_name + " inspires me! ";
    message = message + " The use of " + medium + " is an amazing example of ";
    message = message + artist_nationality + "artwork. ";

    for tag in tags:
        message = message + "#" + tag + " ";
    
    return message;

if __name__ == "__main__":
    app.run(debug=True)
