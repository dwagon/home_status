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
def status():
    data = getStats()
    return render_template('status.html', data=data['devices'][0]['posts'])

###############################################################################
@app.route("/all")
def all():
    data = getStats()
    return render_template('all.html', data=data['devices'][0]['posts'])


###############################################################################
if __name__ == "__main__":
    app.run(debug=True, port=5000)

#EOF
