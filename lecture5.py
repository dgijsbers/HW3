from flask import Flask, render_template
from flask import request
import requests
import json

app = Flask(__name__)

# Challenge 1.1: Designing a more interesting home page
## Edit the index.html template to provide links to:
## http://localhost:5000/itunesForm
## http://google.com
## http://yahoo.com

# Challenge 1.2: Designing a more interesting home page
## Use the images provided in the static folder to make localhost:5000 look like screenshot1.png

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/itunesForm')
def ituneForm():
    return render_template('itunes-form.html')

# BONUS CHALLENGE 1: Displaying the album artwork
## Edit the result.html template to display the artwork for the collection
## The correct key in the JSON object is "artworkUrl100"
@app.route('/itunes-result')
def resultTunes():
    if request.method == 'GET':
        result = request.args
        params = {}
        params['term'] = result.get('artist')
        params['limit'] = result.get('num')
        resp = requests.get('https://itunes.apple.com/search?', params = params)
        data = json.loads(resp.text)
        return render_template('result.html', results = data['results'])

# BONUS CHALLENGE 2:
## Using the Flickr API (you will have to create an API Key)
## Set up a page, http://localhost:5000/photos, with links to "mountains", "rivers", and "parks"
## Each link should take you to a different page that displays 3 images from those Flickr searches
##  - localhost:5000/photos/mountains
##  - localhost:5000/photos/rivers
##  - localhost:5000/photos/parks

## You should create a template to show these images (HINT: you only need to create 1 template to render for all 3 of these pages!).

## Things you will need / may find useful:

## API Key - https://www.flickr.com/services/api/keys/
##
## Flickr API Methods and their dcumentation:
##  - flickr.photos.search : https://www.flickr.com/services/api/flickr.photos.search.html
##  - constructing URLs to photos based on response from flickr.photos.search : https://www.flickr.com/services/api/misc.urls.html
##
## Flickr API Explorer to play and explore example requests - https://www.flickr.com/services/api/explore/flickr.photos.search

## Flickr section of our textbook (but you do NOT need to cache data here, and should not try for now): https://www.programsinformationpeople.org/runestone/static/publicpy3/UsingRESTAPIs/flickr.html

## Information about images in HTML: https://www.w3schools.com/html/html_images.asp For the Flickr code, you'll want to scroll down to "Images on Another Server"

## You may want to refer to the Templates information in the Grinberg book or other resources as well, if you're looking for specifics about Jinja templates syntax



## YOUR CODE HERE

@app.route('/photos')
def photos():
    pass

if __name__=='__main__':
    app.run(debug=True)
