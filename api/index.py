from flask import Flask, render_template, send_file 
from urllib.request import urlopen
import json
from bs4 import BeautifulSoup
from requests_html import HTMLSession

app = Flask(__name__)
BASE_URL = "https://xkcd-api-ridvanaltun.vercel.app/api/comics/random"

@app.route('/')
def read_base():
    response = urlopen(BASE_URL)
    data = json.loads(response.read())
    xkcd_url = data["img"]
    return render_template('img.html', img_url = xkcd_url)
@app.route('/comic')
def image_url():
    response = urlopen(BASE_URL)
    data = json.loads(response.read())
    xkcd_url = data["img"]
    return xkcd_url
    #return send_file(xkcd_url, mimetype = 'image/png')
