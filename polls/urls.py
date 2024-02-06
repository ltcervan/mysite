''' 
    This file is responsible for defining URL 
    patterns that Django will use to match browser requests 
    to the correct view functions.
'''

from django.urls import path
from . import views

app_name = 'polls' # This is for namespacing URL names

urlpatterns = [
    # '''
    #     The <int:question_id>/ syntax is a path converter that matches one or more 
    #     digits and passes them to the view function as an integer. This is used for 
    #     the detail, results, and vote views to identify specific questions.
    # '''
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]