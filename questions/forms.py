from django import forms


class AnswerForm(forms.ModelForm):
    class Meta:
        CHOICE = []
        answer_choice = forms.ChoiceField(choices=CHOICE, widget=forms.RadioSelect)
