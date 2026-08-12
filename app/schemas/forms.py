from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        required=True
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2"
        ]


class ReviewForm(forms.Form):

    rating = forms.IntegerField(
        min_value=1,
        max_value=5
    )

    review = forms.CharField(
        widget=forms.Textarea,
        max_length=1000
    )