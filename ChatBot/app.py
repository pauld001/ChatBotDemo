# importing packages
from flask import Flask
from flask import render_template
from flask import request
from chatterbot import ChatBot
from chatterbot_corpus import corpus
#from chatterbot import TimeLogicAdapter


chat = Flask(__name__)

@chat.route("/chatbot")
def index():
    return render_template ('index.html')

    userinput = request.form.get('solentinput')
    print(userinput)
    bot_input = solent.get_response(userinput)
    print(bot_input)

solent = ChatBot("solent",
storage_adapter='chatterbot.storage.SQLStorageAdapter',
database_uri='sqlite:///database.sqlite3',
logic_adapters=['chatterbot.logic.TimeLogicAdapter', 'chatterbot.logic.BestMatch']
)





