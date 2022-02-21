from flask import Flask, render_template
from urllib.request import urlopen
import json

app = Flask(__name__)
BASE_URL = "https://xkcd-api-ridvanaltun.vercel.app/api/comics/random"

@app.route('/')
def read_base():
    response = urlopen(BASE_URL)
    data = json.loads(response.read())
    xkcd_url = data["img"]
    return render_template('img.html', img_url = xkcd_url)
