# importing packages

from chatterbot import ChatBot
from chatterbot_corpus import corpus
from chatterbot.trainers import ListTrainer




  
solent = ChatBot("solent",
storage_adapter='chatterbot.storage.SQLStorageAdapter',
database_uri='sqlite:///database.sqlite3',
logic_adapters=['chatterbot.logic.BestMatch']
)


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
'here is software engineering course'
'Computer systems and networks engineering'
'here is systems and networks engineering'
])

trainer.train([
'student hand book',
'here is a link to the student handbook'

])

trainer.train([
    'about solent',
    '"information about solent university"'
])

trainer.train([
    'news',
    'here is our latest news and events'
    ])


while True:
    try:
        solent_input = solent.get_response(input())
        
        print (solent_input)
    
    except(KeyboardInterrupt, EOFError, SystemExit):
        break



