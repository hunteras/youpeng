#!/usr/bin/env python3
 # -*- coding: utf-8 -*- 
import sys
from flask import Flask, render_template, jsonify, Response, request
import json

app = Flask(__name__)

contents = None

@app.route('/')
def index():
    global contents

    if (contents == None):
        with open('data/kzsj.json') as f:
            contents = f.read()

    resp = Response(contents, status=200)
    resp.headers['Content-Type'] = 'application/json; charset=utf-8'
    return resp

if __name__ == '__main__':
    app.run(debug=True)

