from flask import Flask, render_template
from urllib.request import urlopen
import json

app = Flask(__name__)
BASE_URL = "https://xkcd-api-ridvanaltun.vercel.app/api/comics/random"

@app.route('/')
def read_base():
    response = urlopen(BASE_URL)
    data = json.loads(response.read())
    return data

@app.route('/test')
def test():
    return 'Test'

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('index.html', result = dict)
