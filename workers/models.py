from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Подразделение (Цех)'
        verbose_name_plural = 'Подразделения (Цеха)'
        ordering = ['name']


class JobTitle(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['name']


class Worker(models.Model):
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    middle_name = models.CharField(max_length=50, verbose_name='Очество')
    department = models.ForeignKey(Department, on_delete=models.PROTECT, verbose_name='Подразделение (Цех)')
    job_title = models.ForeignKey(JobTitle, on_delete=models.PROTECT, verbose_name='Должность')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name} | {self.job_title.name} | {self.department.name}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['last_name']
