from django import forms
from .models import BookSearch
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class BookSearchForm(forms.ModelForm):
    name_of_book = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':"form-control rounded", 'placeholder':"Enter book name"
    }))
    name_of_book = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':"form-control mr-sm-2", 'placeholder':"Enter book name"

    }))
    class Meta:
        model = BookSearch
        fields = ['name_of_book',]


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2']