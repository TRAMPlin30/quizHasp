from django.contrib import admin

from workers.models import Department, JobTitle, Worker

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('Подразделение(Цех)')


class JobTitleAdmin(admin.ModelAdmin):
    list_display = ('Должность')


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('Фамилия', 'Имя', 'Очество', 'Должность', 'Цех')


admin.site.register(Department)
admin.site.register(JobTitle)
admin.site.register(Worker)
