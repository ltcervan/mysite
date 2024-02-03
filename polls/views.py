from django.shortcuts import render
# Where we create oour routes
# Create your views here.
from django.http import HttpResponse #res.json- in javascript
from pymongo import MongoClient
import os 
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
from bson import ObjectId


client = MongoClient(os.getenv('MONGO_URI'))
db = client['mysite']
print(db.list_collection_names())

db.polls_question.insert_one({
    'question_text': 'What is your favorite color?',
    'pub_date': datetime.now()
})

new_question_id = db.polls_questions.insert_one({
    'question_text': 'What ORM do we use from MongoDB?',
    'pub_date': datetime.now()
})

print(db.polls_question.find_one())

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
