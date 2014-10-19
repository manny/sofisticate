from flask import Flask, render_template, request, json
from client import ClarifaiApi
from random import randint
from key import ARTSY_TOKEN
import requests
import simplejson

app = Flask(__name__)

@app.route("/")
def home():

    art_info = get_artwork()
    tags = top_tags(art_info['link'])
    print get_post_message(tags, art_info)
    return render_template("test.html", message="test", link="test")

def top_tags(url):
    clarifai_api = ClarifaiApi()
    result = clarifai_api.tag_image_urls(url)
    top_three = result['results'][0]['result']['tag']['classes'][0:3]
    return top_three

def get_artwork():
    args = {"offset": randint(0, 100), "size":1}
    headers = {"X-Xapp-Token": ARTSY_TOKEN}
    arts = requests.get('https://api.artsy.net/api/artworks',params=args, headers=headers)  
    art_json = simplejson.loads(arts.text)
    if not art_json['_embedded']['artworks']:
        return get_artwork()
    art_json = art_json['_embedded']['artworks'][0]
    
    art_name = art_json['title']
    art_medium = art_json['medium']
    
    link = str(art_json['_links']['thumbnail']['href']).replace("medium", "larger")
    artist_link = art_json['_links']['artists']['href']
    artist_json = requests.get(artist_link, headers = headers)
    artist_json = simplejson.loads(artist_json.text)
    artist_json = artist_json['_embedded']['artists'][0]
    
    artist_name = artist_json['name']
    artist_nationality = artist_json['nationality']

    print artist_name
    print artist_nationality
    print art_name
    print art_medium
    print link

    return {'artist_name': artist_name, 'artist_nationality': artist_nationality, 'art_name': art_name, 'art_medium': art_medium, 'link': link}
    
def get_post_message(tags, art_info):
    message = "Wow! " + art_info['art_name'] + " by " + art_info['artist_name'] + " inspires me! ";
    message = message + " The use of " + art_info['art_medium'] + " is an amazing example of ";
    message = message + art_info['artist_nationality'] + " artwork. ";

    for tag in tags:
        message = message + "#" + tag + " ";
    
    return message;

if __name__ == "__main__":
    app.run(debug=True)
