from django.shortcuts import render
# Where we create oour routes
# Create your views here.
from django.http import HttpResponse, Http404 #res.json- in javascript
from django.shortcuts import render, get_object_or_404
# from pymongo import MongoClient
import os 
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
from bson import ObjectId
from .models import Question
# ================================================================================
#
#                               Generic
#
# ================================================================================

# def index(request):
#     ''' Fetches the latest 5 questions from the database, sorted by publication date in descending order, 
#         and creates a string with their text. It returns this string as an HTTP response.
#     '''
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(f"Here are the latest questions: {output}")

# def detail(request, question_id):
#     ''' Takes a question_id parameter from the URL and returns a placeholder 
#         response indicating which question detail is being viewed.
#     '''
#     return HttpResponse(f"You're looking at question {question_id}.")

# def results(request, question_id):
#     ''' Similar to detail, it returns a placeholder response showing the 
#         results for a specific question identified by question_id
#     '''
#     response = f"You're looking at the results of question {question_id}."
#     return HttpResponse(response)

# def vote(request, question_id):
#     ''' Also takes a question_id and returns a placeholder response 
#         indicating that a vote is being recorded for that question.
#     '''
#     return HttpResponse(f"You're voting on question {question_id}.")
# ================================================================================
#
#                               SQL DB
#
# ================================================================================
# Index view: Display the latest 5 poll questions.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# Detail view: Display a specific question and its choices.
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

# Results view: Display results for a specific question.
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# Need a votes function

# ================================================================================
#
#                               MONGO DB
#
# ================================================================================
# client = MongoClient(os.getenv('MONGO_URI'))
# db = client['mysite']
# print(db.list_collection_names())

# db.polls_question.insert_one({
#     'question_text': 'What is your favorite color?',
#     'pub_date': datetime.now()
# })
#=============== Insert a question ======================
# db.polls_questions.insert_one({
#     'question_text': 'What ORM do we use from MongoDB?',
#     'pub_date': datetime.now()
# })

# print(db.polls_question.find())

# # TODO Search by question_text
# # TODO Search a question by certain text #### EXTRA
# # TODO Search all questions by one date
# # TODO Update a question (pub_date -> needs to be set to current date)
# # TODO Delete a question 

# def search_question_by_text(request, text):
#     question = db.polls_question.find_one({'question text': text})
#     if question:
#         return HttpResponse(f"Found question: {question}")
#     else:
#         return HttpResponse(f"Question with text '{text}' not found.")

# def search_all_questions_by_pub_date(request, pub_date):
#     questions = db.polls_question.find({'pub_date': pub_date})
#     result = [f"Question: {q}" for q in questions]
#     return HttpResponse(result)

# def update_question(request, question_id):
#     result = db.polls_question.update_one(
#         {'_id': ObjectId(question_id)},
#         {'$set': {'pub_date': datetime.now()}}
#     )
#     if result.modified_count > 0:
#         return HttpResponse(f"Question with ID {question_id} updated successfully.")
#     else:
#         return HttpResponse(f"Question with ID {question_id} not found.")

# def delete_question(request, question_id):
#     result = db.polls_question.delete_one({'_id': ObjectId(question_id)})
#     if result.deleted_count > 0:
#         return HttpResponse(f"Question with ID {question_id} deleted successfully.")
#     else:
#         return HttpResponse(f"Question with ID {question_id} not found.")





