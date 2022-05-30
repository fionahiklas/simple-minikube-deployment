#!/usr/bin/env python3
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    response = { "hello": escape(name) }
    return response

if __name__ == "__main__":
    app.run()

