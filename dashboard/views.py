from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect,render_to_response
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import update_session_auth_hash # to make sure after password reset user name comes instead of
                                        # anonymous username. so this basically saves our session!!
from django.contrib.auth.decorators import login_required # to prevent sites to be accessed based on url. only if logged
                                        # in then show the page or else don't.
#from scripts.forms import SignUpForm,PostteamForm
#from scripts.models import newTeamcreation
from scripts.tokens import account_activation_token

from django.contrib import messages
from django.views.generic import TemplateView,FormView
from django.http import HttpResponse
import logging
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver

#this is where you can pass arguments to templates/html files

def home(request):
    return render(request, 'index.html')

def redirect_view(request):#change
	response = redirect('Collabify/')
	return response
'''
#commented this out
def team_info(request):
    user_name = request.user.username
    print ("user_name\t",user_name)
    try:
        one_team = newTeamcreation.objects.filter(team_created_by=request.user.username)[0]
        text = one_team.team_name
        team_des = one_team.team_description
        team_list = one_team.team_member
        args = {'text':text,'team_des':team_des,'team_list':team_list}
        return render(request, 'team_page.html',args)
    except:
        messages.error(request, 'please create team first.')
        form = PostteamForm()
        return render(request,'team_creation_error.html',{'form':form})
'''
'''
#commented all of this out
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
                messages.error(request, 'Please select at least four team members.')
                form = PostteamForm(request.POST)
                return render(request,template_name,{'form':form})
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
            messages.error(request, 'Please select at least four team members.')
            return render(request,template_name,{'form':form})
'''
@login_required
def attendance(request):
    return render(request, 'attendance_QR_Code.html')

@login_required
def board(request):
    return render(request, 'board.html')

@login_required
def dashboard(request):
    form = UserCreationForm()
    #what does c do?
    c = {'form': form}
    #not sure what render to response is, but this should render the dashboard and also pass in name as an attr
    #need to check if user is in any teams
    return render_to_response("dashboard_2.html", {'name': request.user.username}) 
'''
#commented all of this out
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': force_text(urlsafe_base64_encode(force_bytes(user.pk))),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
'''

def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('dashboard')
    else:
        return render(request, 'account_activation_invalid.html')

log = logging.getLogger(__name__)

@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    log.info('login user: {user} via ip: {ip}'.format(
        user=user,
        ip=ip
    ))
user_logged_in.connect(user_logged_in_callback)

@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')

    log.info('logout user: {user} via ip: {ip}'.format(
        user=user,
        ip=ip
    ))
user_logged_out.connect(user_logged_out_callback)

@receiver(user_login_failed)
def user_login_failed_callback(sender,request, credentials, **kwargs):
    log.warning('login failed with username: {credentials} from ip {ip}'.format(
        credentials=credentials['username'],ip=request.META.get('REMOTE_ADDR')
    ))
user_login_failed.connect(user_login_failed_callback)
