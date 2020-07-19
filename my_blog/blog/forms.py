from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


from .models import Article, Author
from django.forms import ModelForm


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'  


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 