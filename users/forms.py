from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.forms import fields
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field, Submit

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('username'),
            Row(
                Column(Field('first_name')),
                Column(Field('last_name')),
            ),
            Field('email'),
            Field('age'),
            Field('password1'),
            Field('password2'),

            Submit('submit', 'Create Account', css_class="btn btn-warning btn-block")
            
        )
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name','username', 'email', 'age',)

class CustomUserChangeForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('username'),
            Row(
                Column(Field('first_name')),
                Column(Field('last_name')),
            ),
            Field('email'),
            Field('age'),
            Field('password1'),
            Field('password2'),

            Submit('submit', 'Create Account', css_class="btn btn-warning btn-block")
            
        )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'age',)

