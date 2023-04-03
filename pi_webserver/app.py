from flask import Flask, render_template
from flask import request
import datetime
import os

app = Flask(__name__)


@app.route('/')
def index():
    timeString = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
    indexData = {
        'title': 'RapsberryPi Webserver',
        'main_header': 'Welcome! :)',
        'time_date': timeString
        }
    return render_template('index.html', **indexData)


@app.route('/movies')
def movies():
    fileFormats = ['mp4', 'ogg', 'webm']
    filesInDir = [x for x in os.listdir('./static/')
                  if x.split('.')[-1].lower() in fileFormats]
    return render_template('movies.html', files=filesInDir)


@app.route('/video')
def video():
    fileName = request.args.get("name")
    fileFormat = request.args.get("format")
    return render_template('video.html', name=fileName, format=fileFormat)


@app.route('/pics')
def pics():
    timeString = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title': 'RapsberryPi Webserver',
        'main_header': 'Welcome! :)',
        'time_date': timeString
        }
    return render_template('pics.html', **templateData)


if __name__ == "__main__":
    app.run(host='192.168.1.113', port=5000)
