from django.shortcuts import render
from django.views.generic import TemplateView
from . forms import PostteamForm
from . models import Team
# Create your views here.

def home(request):
	#need to create team.html that checks if a user has a team
	return render(request, 'team/team_page.html')

def team_info(request):
    user = request.user#does this work
    
    try:
        team = Team.objects.filter(user.team_id)#[0]
        team_name = team.team_name
        team_des = team.team_desc
        team_list = team.team_members
        args = {'text':text,'team_des':team_des,'team_list':team_list}
        return render(request, 'team_page.html',args)
    except:
        messages.error(request, 'please create team first.')
        form = PostteamForm()
        return render(request,'team_creation_error.html',{'form':form})


class team_creation(TemplateView):
    template_name = 'team_creation.html'

    def get(self,request):
        print("test1 get called")
        form = PostteamForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        print("test1 post called")
        form = PostteamForm(request.POST)
        args ={}
        if form.is_valid():
            print("test1 form valid called")
            text = form.cleaned_data['team_name']
            team_des = form.cleaned_data['team_description']
            team_list = form.cleaned_data['team_member']
            print(text)
            print(team_des)
            print(team_list)
            if len(team_list) < 4:
                messages.error(request, 'please make atleast four selection for team member.')
                form = PostteamForm(request.POST)
                return render(request,'team_creation.html',{'form':form})
            else:
                args = {'text':text,'team_des':team_des,'team_list':team_list}
                team_creation = form.save(commit=False)
                team_creation.team_created_by = request.user.username
                team_creation.save()
                form.save_m2m() # needed since using commit=False
                form = PostteamForm()
                return render(request,'team_page.html',args )

        else:
            form = PostteamForm(request.POST)
            messages.error(request, 'please make atleast four selection for team member.')
            return render(request,'team_creation.html',{'form':form})