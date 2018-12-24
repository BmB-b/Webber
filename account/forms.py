from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ExtendedUser

from .choices import GENDER_CHOICES

class SignUpForm(UserCreationForm):

    gender = forms.BooleanField(initial=GENDER_CHOICES[0], widget=forms.RadioSelect(choices=GENDER_CHOICES))
    avatar = forms.ImageField(required=False)
    url = forms.URLField(max_length=20, required=False)
    biography =  forms.CharField(max_length=1000, required=False)

    class Meta:
        model = ExtendedUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)