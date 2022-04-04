# importing packages
from flask import Flask
from flask import render_template
from chatterbot import ChatBot, chatterbot


app = Flask(__name__)

@app.route("/index")
def index():
    return render_template ('index.html')
    
solent = ChatBot("solent")



