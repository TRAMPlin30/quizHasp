from django.contrib.auth.models import User
from django.db import models

from questions.models import Test
from workers.models import Worker


class Result(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        fixed_quantity_questions = 4
        actual_score_to_pass = int((self.score / fixed_quantity_questions) * 100)
        return f'{self.user} - {self.test} Правильных ответов: {actual_score_to_pass}%'

    class Meta:
        db_tablespace = 'result_result'
