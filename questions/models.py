import random

from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=254, unique=True)
    number_of_questions = models.IntegerField(null=True)
    time = models.IntegerField(help_text='продолжительность теста в минутах', null=True)
    required_score_to_pass = models.IntegerField(help_text='Необходимый процент для здачи теста', null=True)

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    def __str__(self):
        return f'{self.name} | Количество вопросов: {self.number_of_questions} |'

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
        ordering = ['name']


class Question(models.Model):
    numbering = models.IntegerField(default=0)
    name = models.TextField(max_length=200)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def get_answers(self):
        return self.answer_set.all()

    def __str__(self):
        return f'{self.name}'  # отображение в админке

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['name']


class Answer(models.Model):
    name = models.TextField(max_length=200, unique=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct_answer = models.BooleanField(default=False, verbose_name='Правильный ответ')

    def __str__(self):
        if self.correct_answer:
            return f'Ответ: {self.name} | На вопрос:{self.question} | - ответ верный'
        else:
            return f'Ответ: {self.name} | На вопрос:{self.question} | - ответ ложный'

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
        ordering = ['name']
