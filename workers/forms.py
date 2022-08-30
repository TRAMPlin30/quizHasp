from django import forms

from workers.models import Worker


class Select(forms.Select):
    input_type = 'select'


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = [
            'last_name',
            'first_name',
            'middle_name',
            'department',
            'job_title']

        widgets = {'department': Select(),
                   'job_title': Select()}
