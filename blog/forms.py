from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Import the User model

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        required=True,
        label='Username',
        widget=forms.TextInput(attrs={'class': 'custom-forms-input'})  # Use the custom class here
    )

    custom_field = forms.CharField(
        max_length=100,
        required=True,
        label='Custom Field',
        widget=forms.TextInput(attrs={'class': 'custom-forms-input'})  # Use the custom class here
    )

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields