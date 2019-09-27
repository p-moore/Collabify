from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from . forms import PostTeamForm
from . models import Team
from users.models import CustomUser
from django.contrib import messages
# Create your views here.

def home(request):
    user = request.user
    #print('got here')
    return render(request, 'team/team.html', {'user': user})

def team_info(request):
    user = request.user
    
    try:
        team = Team.objects.filter(user.team_id)#[0]
        team_name = team.team_name
        team_des = team.team_desc
        team_list = team.team_members
        args = {'text':text,'team_des':team_des,'team_list':team_list}
        return render(request, 'team_page.html',args)
    except:
        messages.error(request, 'please create team first.')
        form = PostTeamForm()
        return render(request,'team_creation_error.html',{'form':form})


class team_creation(TemplateView):
    template_name = 'team_creation.html'
    def get(self,request):
        print("test1 get called")
        form = PostTeamForm()
        return render(request,'team/team_creation.html',{'form':form})

    def post(self,request):
        model = Team
        print("test1 post called")
        form = PostTeamForm(request.POST)
        args ={}
        if form.is_valid():
            user = request.user
            team_name = form.cleaned_data['team_name']
            team_description = form.cleaned_data['team_description']
            team_members = form.cleaned_data['team_members']
            args = {'team_name':team_name,'team_description':team_description,'team_members':team_members}
            team_creation = form.save(commit=False)#sets team_creation to Team instance with variables given in form
            user.team = team_creation#sets user team info!!!!!!!!
            user.save()#saves user team info!!!!!!!
            team_creation.team_created_by = request.user.username
            team_creation.save()
            form.save_m2m() # needed since using commit=False
            form = PostTeamForm()
            return render(request,'team/team.html', args)#change to team.html??
            '''
            if len(team_members) < 4:
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
            '''

        else:
            form = PostTeamForm(request.POST)
            print('error')
            #messages.error(request, 'please make atleast four selection for team member.')
            return render(request,'team/team_creation.html',{'form':form})