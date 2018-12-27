from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ExtendedUser

from .choices import GENDER_CHOICES

class SignUpForm(UserCreationForm):

    gender = forms.TypedChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect, coerce=lambda x: x == 'True')
    image = forms.ImageField(required=False)
    url = forms.URLField(max_length=20, required=False)
    biography =  forms.CharField(max_length=1000, required=False, widget=forms.Textarea)

    class Meta:
        model = ExtendedUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'gender', 'image', 'url', 'biography')