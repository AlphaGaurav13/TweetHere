# from django import forms
# from .models import X
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


# class XForm(forms.ModelForm):
#   class Meta:
#     model = X
#     fields = ['text', 'photo']


# class UserRegisterForm(UserCreationForm):
#   email = forms.EmailField()
#   class Meta:
#     models = User
#     fields = ('username', 'email', 'password1', 'password2')
    
from django import forms
from .models import X
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class XForm(forms.ModelForm):
    class Meta:
        model = X
        fields = ['text', 'photo']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User  # Correct and confirm the model is User
        fields = ('username', 'email', 'password1', 'password2')
