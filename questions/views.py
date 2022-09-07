from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.base import View

from questions.models import Question, Test, Answer
from result.models import Result
from workers.models import Worker


class Test_render(ListView, View):
    model = Test
    template_name = "questions/tests.html"
    context_object_name = 'tests_list'


def questions_list(request, pk):
    test = Test.objects.get(pk=pk)
    context = {'test_name': test}
    return render(request, 'questions/questions.html', context)


def questions_data_list(request, pk):
    test = Test.objects.get(pk=pk)
    questions = []
    for q in test.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.name)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': test.time
    })


def save_test_view(request, pk):
    if request.POST:
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')
        print(data_)

        for k in data_.keys():
            question = Question.objects.get(name=k)
            questions.append(question)

        user = request.user
        test = Test.objects.get(pk=pk)

        score = 0
        multiplier = 100 / test.number_of_questions
        results = []
        correct_answer_result = None

        for q in questions:
            a_selected = request.POST.get(str(q.name))
            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.name:
                        if a.correct_answer:
                            score += 1
                            correct_answer_result = a.name
                    else:
                        if a.correct_answer:
                            correct_answer_result = a.name
                results.append({str(q): {'correct_answer_result': correct_answer_result,
                                         'answered': a_selected}})
            else:
                results.append({str(q): 'not answered'})

        score_ = score * multiplier
        Result.objects.create(test=test, user=user, score=score)


        if score_ >= test.required_score_to_pass:
            return JsonResponse({'passed': True, 'score': score_, 'results': results, 'user': user.username})
        else:
            return JsonResponse({'passed': False, 'score': score_, 'results': results, 'user': user.username})


def end_of_test(request):
    return render(request, 'end_of_test.html')


# ----------------------------------------------------------------------------------------
def questions_Of_test(request, test_id=None):
    context = {'tests': Test.objects.all()}
    if test_id:
        querySet = Question.objects.filter(tests_id=test_id)
        questions = {'questions': querySet}
        context.update(questions)
        return render(request, 'questions/questions.html', context)


def answers_Of_question(request, question_id=None):
    context = {'questions': Question.objects.all()}
    if question_id:
        querySet = Answer.objects.filter(question_id=question_id)
        answers = ({'answers': querySet})
        context.update(answers)
        return render(request, 'questions/answer.html', context)
