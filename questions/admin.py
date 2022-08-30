from django.contrib import admin

from questions.models import Question, Test, Answer


class TestAdmin(admin.ModelAdmin):
    list_display = ('Наименование теста')


class AnswerInLine(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]
    # list_display = ('№', 'Вопрос', 'Тест к которому относиться вопрос')
    # list_filter = ('question')


# class AnswerAdmin(admin.ModelAdmin):
#     list_display = ('Ответ', 'Вопрос', 'Корректность')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Test)
