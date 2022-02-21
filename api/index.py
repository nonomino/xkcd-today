from flask import Flask, render_template
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
    url = './templates/img.html'
    with HTMLSession() as session:
        response = session.get(url)
        response.html.render()
        content = response.html.html

    soup = BeautifulSoup(content, "html.parser")
    images = soup.find_all("img")
    src = images.get("src")
    return send_file(src, mimetype = 'image/jpg')
