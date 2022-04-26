# importing packages
from asyncore import read
from email.policy import default
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


solent = ChatBot("solent",
      #heroku uri
#database_uri='postgres://nkcguvuabtmujv:6c8384842f707c8db4d64d28ce92554260989edc0813870436a5cfddf968983e@ec2-99-80-170-190.eu-west-1.compute.amazonaws.com:5432/d2t6kvgjuj9m8g',
      #test uri
database_uri='sqlite:///database.sqlite3',
storage_adapter="chatterbot.storage.SQLStorageAdapter",
logic_adapters=['chatterbot.logic.BestMatch']
)



@chat.route("/", methods=['POST', 'GET'])
#def index():


def index():
    solent_input = "Hello i am student the chat bot! Ask me a question or query and i will help you"
    chatpost = ''
    if request.method == 'POST':
        print("post")
        print("post", file=sys.stderr)
        #chatpost = input "solent_input"
        chatpost = request.form['solent_input']
        print(chatpost)
        print('hi')
        solent_input = solent.get_response(chatpost)
        print(solent_input)
        
    return render_template ('index.html', outmessage=solent_input, usermessage=chatpost), print('/chatbot')

   

if __name__ == "__main__":
  chat.run()


#training "solent" chatbot
trainer = ListTrainer(solent)

#greetings
trainer.train([
'Hi',
'Hello i am student the chat bot. ask me a question or query and i will help you',

])


trainer.train([
'can you help me',
'yes i can please state how i can help you'
])



trainer.train([
'map',
'here is a map of the campus'
])


trainer.train([
'i am looking to book openday',
'here is the form to book an openday'
])
trainer.train([
'can you help me',
'yes i can please state how i can help you'
])
#find a course
trainer.train([
'i am looking for a course',
'which course are you looking for',
'computing',
'here is the computing course',
'software engineering',
'here is software engineering course',
'Computer systems and networks engineering',
'here is systems and networks engineering'
])

trainer.train([
'student union'
'here is a link to the student union'

])

trainer.train([
'student hand book',
'here is a link to the student handbook'

])

trainer.train([
    'solent online learning',
    'here is a link to solent online learning: https://learn.solent.ac.uk'
])

trainer.train([
'timetable',
'here is a link to your student timetable: https://timetable.solent.ac.uk/'
])


trainer.train([
'email',
'here is a link to outlook to acess your solent email: https://www.office.com/ having problems contact us at: ...'  
])

trainer.train([
    'about solent',
    '"information about solent university"'
])

trainer.train([
    'news',
    'here is our latest news and events'
])

trainer.train([
    'libary opening times',
    'there are the current libary opening times:'
])

trainer.train([
    'contact student hub',
    'please complete this form. and we will get back to you'
])


#contact

trainer.train([
    'contact student hub',
    'please complete this form. and we will get back to you '
])

trainer.train([
    'contact student hub',
    'please complete this form. and we will get back to you'
])

trainer.train([
    'contact student registry',
    '<h2>instructions of use</h2>'
])




