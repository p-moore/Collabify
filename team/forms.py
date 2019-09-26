from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser as user
from . models import Team


class PostteamForm(forms.ModelForm):
    team_member = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(attrs={'size':'10'}),
                                            queryset=user.objects.all())

    class Meta:
        model = Team
        fields = {
            'team_name': forms.TextInput(attrs={'placeholder': 'What\'s your Team name?'}),
            'team_desc': forms.TextInput(attrs={'placeholder': 'Team description'}),
            'team_member' : forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(attrs={'size':'10'}),
                                                    queryset=user.objects.all())
        }
    def clean_teamcreated_by(self):
        if not self.cleaned_data['team_created_by']:
            return User()
        else:
        	return self.cleaned_data['team_created_by']

