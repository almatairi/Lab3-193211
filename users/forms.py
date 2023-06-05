from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','email','password1','password2']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['username' , 'email','name','profile_image','bio']
