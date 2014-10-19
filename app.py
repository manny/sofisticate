from flask import Flask, render_template, request, json
from client import ClarifaiApi
from random import randint
from key import ARTSY_TOKEN
import requests
import simplejson

app = Flask(__name__)

@app.route("/")
def home():
    get_artworks()
    return render_template("test.html", message="test", link="test")

def top_tags(url):
    clarifai_api = ClarifaiApi()
    result = clarifai_api.tag_image_urls('http://www.clarifai.com/img/metro-north.jpg')
    return result

def get_artworks():
    args = {"offset": randint(0, 100), "size":1}
    headers = {"X-Xapp-Token": ARTSY_TOKEN}
    arts = requests.get('https://api.artsy.net/api/artworks',params=args, headers=headers)  
    art_json = simplejson.loads(arts.text)
    link = art_json['_embedded']['artworks'][0]['_links']['thumbnail']['href']
    
def get_post_message(tags, artist_name, artist_nationality, medium, artwork_name):
    message = "Wow! " + artwork_name + " by " + artist_name + " inspires me! ";
    message = message + " The use of " + medium + " is an amazing example of ";
    message = message + artist_nationality + "artwork. ";

    for tag in tags:
        message = message + "#" + tag + " ";
    
    return message;

if __name__ == "__main__":
    app.run(debug=True)
