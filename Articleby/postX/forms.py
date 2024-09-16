from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class Postform(forms.ModelForm):
    class Meta:
        model=Post
        fields=['text','photo']

class UserRegistrationform(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','email','password1','password2',)
