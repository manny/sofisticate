from flask import Flask, render_template, request, json
from client import ClarifaiApi
import requests

app = Flask(__name__)

@app.route("/")
def home():
    print top_tags()
    return render_template("test.html")


def top_tags():
    clarifai_api = ClarifaiApi()
    result = clarifai_api.tag_image_urls('http://www.clarifai.com/img/metro-north.jpg')
    return result


if __name__ == "__main__":
    app.run(debug=True)
