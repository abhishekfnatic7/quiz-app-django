
from .models import Questionpage
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models  import User
class addform(forms.ModelForm):
    class Meta:
        model=Questionpage
        fields="__all__"

class Regi(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1']