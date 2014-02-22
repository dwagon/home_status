#!/usr/bin/env python
#
from apikey import apikey
from flask import Flask, render_template
import requests

app = Flask(__name__)


###############################################################################
def getStats():
    url = "http://api.smartcitizen.me/v0.0.1/%s/lastpost.json" % apikey
    r = requests.get(url)
    return r.json()


###############################################################################
@app.route("/")
def temperature():
    data = getStats()
    return render_template('temperature.html', data=data['devices'][0]['posts'])


###############################################################################
if __name__ == "__main__":
    app.run()

#EOF
