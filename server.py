from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from flask import sessions
import json 
import random 

app = Flask(__name__)

@app.route("/homepage")
def homepage():
    return jsonify({'Success': 'You are now in the homepage'})


if __name__ == "__main__":
    app.run()
