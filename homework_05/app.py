from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template('base.html')


@app.get("/about/")
def about():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)
