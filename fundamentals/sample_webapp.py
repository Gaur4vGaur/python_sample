#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 05:58:09 2018

@author: gaurav
"""


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
