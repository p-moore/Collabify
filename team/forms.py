from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser as user
from . models import Team


class PostTeamForm(forms.ModelForm):
    #def need to add more customization - like a search function or only show users that aren't in a team
    team_members = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(attrs={'size':'10'}),
                                            queryset=user.objects.all())

    class Meta:
        model = Team
        fields = {
            'team_name': forms.TextInput(attrs={'placeholder': 'What\'s your Team name?'}),
            'team_description': forms.TextInput(attrs={'placeholder': 'Team description'}),
            'team_members' : forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(attrs={'size':'10'}),
                                                    queryset=user.objects.all())
        }

    def clean_teamcreated_by(self):
        if not self.cleaned_data['team_created_by']:
            return User()
        else:
        	return self.cleaned_data['team_created_by']

