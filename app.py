from flask import Flask, render_template, request, json
from client import ClarifaiApi
import requests

app = Flask(__name__)

@app.route("/")
def home():
    print top_tags()
    return render_template("test.html", message="test", link="google.com")


def top_tags():
    clarifai_api = ClarifaiApi()
    result = clarifai_api.tag_image_urls('http://www.clarifai.com/img/metro-north.jpg')
    return result

def get_post_message(tags, artist_name, artist_nationality, medium, artwork_name):
    message = "Wow! " + artwork_name + " by " + artist_name + " inspires me! ";
    message = message + " The use of " + medium + " is an amazing example of ";
    message = message + artist_nationality + "artwork. ";

    for tag in tags:
        message = message + "#" + tag + " ";
    
    return message;

if __name__ == "__main__":
    app.run(debug=True)
