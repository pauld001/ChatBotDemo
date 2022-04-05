# importing packages
from flask import Flask
from flask import render_template
from chatterbot import ChatBot
from chatterbot_corpus import corpus
import time


chat = Flask(__name__)

@chat.route("/chatbot")
def index():
    return render_template ('index.html')
    
solent = ChatBot("solent",
storage_adapter='chatterbot.storage.SQLStorageAdapter',
database_uri='sqlite:///database.sqlite3',
logic_adapters=['chatterbot.logic.TimeLogicAdapter', 'chatterbot.logic.BestMatch']
)

bot_input = solent.get_response(input())
print(bot_input)


