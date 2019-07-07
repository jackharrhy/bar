import os
import markovify
from flask import Flask

knowledge = open("knowledge.txt", "r")
chain = markovify.Text(knowledge.read())
knowledge.close()

app = Flask(__name__)

@app.route('/')
def get_sentence():
    return chain.make_sentence()

