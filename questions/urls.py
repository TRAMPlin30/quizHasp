from django.template.defaulttags import url
from django.urls import path
from questions.views import Test_render, questions_Of_test, answers_Of_question, questions_list, questions_data_list, \
    save_test_view

app_name = 'questions'

urlpatterns = [
    path('tests/', Test_render.as_view(), name='tests'),
    path('tests/<pk>/', questions_list, name='questions_list'),
    path('tests/<pk>/save', save_test_view, name='save_test_view'),
    path('tests/<pk>/data', questions_data_list, name='questions_data_list'),

    # path('<int:test_id>/', questions_Of_test, name='questions_Of_test'),
    # path('answer/<int:question_id>/', answers_Of_question, name='answers_Of_question'),

]
