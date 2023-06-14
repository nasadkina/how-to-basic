from flask import Flask
from flask import render_template
import requests
import json

app = Flask(__name__)


@app.get("/")
def index():
    return render_template('base.html')


def get_meme():
    url = "https://meme-api.com/gimme/wholesomememes"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit


@app.get("/about/")
def about():
    meme_pic, subreddit = get_meme()
    return render_template('meme.html', meme_pic=meme_pic, subreddit=subreddit)


if __name__ == '__main__':
    app.run(debug=True)
