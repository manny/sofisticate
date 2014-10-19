from flask import Flask, render_template, request, json
from client import ClarifaiApi
from random import randint
from key import ARTSY_TOKEN
import requests

app = Flask(__name__)

@app.route("/")
def home():
    #print top_tags()
    get_artworks()
    return render_template("test.html")

def top_tags(url):
    clarifai_api = ClarifaiApi()
    result = clarifai_api.tag_image_urls('http://www.clarifai.com/img/metro-north.jpg')
    return result

def get_artworks():
    args = {"offset": randint(0, 100), "size":1}
    headers = {"X-Xapp-Token": ARTSY_TOKEN}
    arts = requests.get('https://api.artsy.net/api/artworks',params=args, headers=headers)  
    print arts.text
    
if __name__ == "__main__":
    app.run(debug=True)
