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
trainer.train([
'Hi',
'Hello i am student the chat bot. ask me a question or query and i will help you',

])


trainer.train([
'can you help me',
'yes i can please state how i can help you'
])



trainer.train([
'campus map',
'here is a map of the campus: https://www.solent.ac.uk/about/documents/east-park-terrace-campus-map.pdf'
])


trainer.train([
'i am looking to book openday',
'here is the form to book an openday'
])

#find a course
trainer.train([
'i am looking for a course',
'which course are you looking for',
'computing',
'here is the computing course https://www.solent.ac.uk/courses/undergraduate/computing-bsc',
'software engineering ',
'here is software engineering course https://www.solent.ac.uk/courses/undergraduate/software-engineering-bsc',
'Computer systems and networks engineering',
'here is systems and networks engineering https://www.solent.ac.uk/courses/undergraduate/computer-systems-and-networks-engineering-bsc'
])

trainer.train([
'opendays',
'here are the upcoming opendays: undergraduate: 28th april 2022, cadetship: 14th may 2022, Postgraduate: 18th may 2022. See more here https://www.solent.ac.uk/open-days'

])

trainer.train([
'student union',
'here is a link to the student union'

])

trainer.train([
'student hand book',
'here is a link to download and read the student handbook https://students.solent.ac.uk/official-documents/quality-management/student-handbook.pdf'

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
'here is a link to outlook to acess your solent email click hear to sign in: https://www.office.com/ having problems contact us at: ...'  
])

trainer.train([
    'about solent',
    'Solent University is all about creating opportunities: for its students, for its staff, for its partners. It offers expertise and experiences you couldnt get anywhere else, opening doors and making introductions. see more here: https://www.solent.ac.uk/about '
])

trainer.train([
    'news''events',
    'here is our latest news and events https://students.solent.ac.uk/events'
])

trainer.train([
    'library opening times',
    'Tuesday 19th April from 8.30am - Friday 20th May up to 11.45pm: The Library will be open 24/7 see more here: https://libguides.solent.ac.uk/libraryessentials'
])

trainer.train([
    'contact student hub',
    'please complete this form. and we will get back to you'
])

trainer.train([
    'contact student union',
    'please complete this form. and we will get back to you. additionaly you can find information on the Student union website https://www.solentsu.co.uk/'
])


trainer.train([
    'contact student hub',
    'please complete this form. and we will get back to you '
])

trainer.train([
    'contact student registry',
    'please complete this form, or email student.registry@solent.ac.uk, and we will get back to you'
])


trainer.train([
    'covid-19',
    'please read the latest information from the government. https://students.solent.ac.uk/news/covid-19-government-update-tuesday-21-february'
])


trainer.train([
'livechat',
'transferring you to a member of our team. who will be ready to help you'
])

trainer.train([
    'my accommodation',
    'https://students.solent.ac.uk/university-life/accommodation'
])
