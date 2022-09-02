from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label='ПІБ та підрозділ (цех)', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                             'placeholder': 'Введіть ПІБ та підрозділ вказані при реєстрації'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                 'placeholder': 'Введіть пароль'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            qs = User.objects.filter(username=username)
            if not qs.exists():
                raise forms.ValidationError('Такий користувач не зареєстрований або видалений із системи')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Невірно вказанний пароль')
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Користувач не активний')
        return super().clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Введіть ПІБ та підрозділ (цех)',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Введіть ПІБ та підрозділ згідно інструкцій!'}))
    password = forms.CharField(label='Введіть пароль', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                         'placeholder': 'Введіть пароль'}))
    password2 = forms.CharField(label='Повторіть пароль', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                            'placeholder': 'Повторіть пароль'}))

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        # password = self.cleaned_data.get('password')
        # password2 = self.cleaned_data.get('password2')

        data = self.cleaned_data

        if data['password'] != data['password2']:
            raise forms.ValidationError('!!!')  # 'Паролі відрізняються!' - можно вставыть в скобочки и в html а можно указать как указано register.html
        return self.data['password2']
