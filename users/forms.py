from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from blog.models import Book
from blog.models import Post


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'password1',
                  'password2'

                  )


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class RatingForm(forms.ModelForm):
    rating = forms.Textarea()

#
# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = ('title', 'details', 'author', 'file', 'year', 'faculty')
