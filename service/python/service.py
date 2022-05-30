#!/usr/bin/env python3
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    response = { "hello": escape(name) }
    return response

if __name__ == "__main__":
    # Needs to listen on all interfaces otherwise the port
    # redirection doesn't work.  By default Flask binds
    # only to 127.0.0.1 which can't be accessed from outside
    # the container
    app.run(host="0.0.0.0", port=8173)

