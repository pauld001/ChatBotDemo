# importing packages
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


student = ChatBot("student",read_only=True,
      #heroku uri
database_uri='postgres://vydwsmdsbhnigz:1615d83289a217bc52c3cde49fbf59ea2675e9af7ee1f1940e3af3bdb41b498a@ec2-52-30-159-47.eu-west-1.compute.amazonaws.com:5432/d2trrt3fbq5gui',
      #test uri
#database_uri='sqlite:///database.sqlite3',
storage_adapter="chatterbot.storage.SQLStorageAdapter",
logic_adapters=['chatterbot.logic.BestMatch'])



@chat.route("/", methods=['POST', 'GET'])
#def index():


def index():
    student_input = "Hello i am student your assistant! Ask me a question or query and i will help you"
    chatpost = 'hi'
    if request.method == 'POST':
        #print("post")
        #print("post", file=sys.stderr)
        #chatpost = input "solent_input"
        chatpost = request.form['solent_input']
        print(chatpost)
        student_input = student.get_response(chatpost)
        print(student_input)
        
    return render_template ('index.html', outmessage=student_input, usermessage=chatpost)

   

if __name__ == "__main__":
  chat.run()


trainer = ListTrainer(student)

#greetings
