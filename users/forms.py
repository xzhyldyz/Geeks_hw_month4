from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm


GENDER = (
    ('male','male'),
    ('female','female'),
    ('unknown','unknown')
)
POSITIONS = (
    ('Backend','Backend'),
    ('Frontend','Frontend'),
    ('Project Managment','Project Managment'),
    ('1C','1C'),
    ('UX/UI','UX/UI'),
    ('Тестировщик','Тестировщик')
)

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=14, required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    position = forms.ChoiceField(choices=POSITIONS, required=True)
    experience_years = forms.CharField(max_length=2, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name',
            'gender',
            'phone_number',
            'position',
            'experience_years'
        )
        def save(self, commit=True):
            user = super(CustomRegisterForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user