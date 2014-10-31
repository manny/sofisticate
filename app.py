from flask import Flask, render_template, request, json
from client import ClarifaiApi
from random import randint
from key import get_artsy_key
import requests
import simplejson

app = Flask(__name__)

@app.route("/")
def home():
    artwork = get_artwork()
    tags = top_tags(artwork['link'])
    message = get_post_message(tags, artwork)
    print artwork['link']
    print message
    return render_template("test.html", message=message, link=artwork['link'])

def top_tags(url):
    clarifai_api = ClarifaiApi()
    result = clarifai_api.tag_image_urls(url)
    top_three = result['results'][0]['result']['tag']['classes'][0:3]
    return top_three

def get_artwork():
    args = {"offset": randint(0, 10000), "size":1}
    key = get_artsy_key()
    headers = {"X-Xapp-Token": key}
    arts = requests.get('https://api.artsy.net/api/artworks',params=args, headers=headers)  
    art_json = simplejson.loads(arts.text)
    if not art_json['_embedded']['artworks']:
        print art_json['_embedded']['artworks']
        return get_artwork()
    art_json = art_json['_embedded']['artworks'][0]
    
    art_name = art_json['title']
    art_medium = art_json['medium']
    
    link = str(art_json['_links']['thumbnail']['href']).replace("medium", "larger")
    artist_link = art_json['_links']['artists']['href']
    artist_json = requests.get(artist_link, headers = headers)
    artist_json = simplejson.loads(artist_json.text)
    if not artist_json['_embedded']['artists']:
        return get_artwork()
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
    interjections = ["Lo and behold", "Wow", "Holy shit", "Heigh-ho",
                     "My word", "Right-o", "Good golly"]
    adjectives = ["an amazing", "an exquisite", "a guileless", 
                  "a sublime", "a phantasmagorical"]
    
    good_vibes = ["inspires me", "speaks to my soul", 
                   "reminds me of my years as a long lad abroad", 
                   "fasinates me", 
                   "stirs upon me unspeakable emotions"]

    interject = interjections[randint(0, len(interjections) - 1)]
    adject = adjectives[randint(0, len(adjectives) - 1)]
    good_vibe = good_vibes[randint(0, len(good_vibes) - 1)]

    message = interject + "! " + art_info['art_name'] + " by " + art_info['artist_name'] + " "  + good_vibe + "! ";
    message = message + " The use of " + art_info['art_medium'] + " is " + adject + " example of ";
    if not art_info['artist_nationality']:
        art_info['artist_nationality'] = ""
    message = message + art_info['artist_nationality'] + " artwork. ";
    for tag in tags:
        message = message + "#" + tag.replace(" ", "") + " ";
    
    return message;

if __name__ == "__main__":
    app.run(debug=True)
