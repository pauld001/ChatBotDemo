# importing packages
from asyncore import read
import sys
from flask import Flask
from flask import render_template
from flask import request

from chatterbot import ChatBot
from chatterbot_corpus import corpus
from chatterbot.trainers import ListTrainer

#from chatterbot import TimeLogicAdapter
chat = Flask(__name__)

print('working')


solent = ChatBot("solent", read_only=True, 
storage_adapter='chatterbot.storage.SQLStorageAdapter',
database_uri='sqlite:///database.sqlite3',
logic_adapters=['chatterbot.logic.BestMatch']
)



@chat.route("/", methods=['POST', 'GET'])
#def index():


def index():
    solent_input = "Hello i am student the chat bot! Ask me a question or query and i will help you"
 
    if request.method == 'POST':
        print("post")
        print("post", file=sys.stderr)
        #chatpost = input "solent_input"
        chatpost = request.form['solent_input']
        print(chatpost)
        print('hi')
        solent_input = solent.get_response(chatpost)
        print(solent_input)
        
    return render_template ('index.html', outmessage=solent_input), print('/chatbot')

   

if __name__ == "__main__":
  chat.run()