from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . models import CustomUser
#from scripts.models import newTeamcreation,attendance,allMembers #commented this out


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = CustomUser
        fields = ('first_name','last_name', 'username','email', 'password1', 'password2', )

class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = ('first_name','last_name', 'username','email', 'password', 'team')

class CustomUserTeamRegisterForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = ('team',)

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		fields = ('first_name','last_name', 'username','email', 'password',)
