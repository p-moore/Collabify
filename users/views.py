from . forms import SignUpForm
from . models import CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.http import HttpResponse
import logging
from django.dispatch import receiver
from . tokens import account_activation_token
from django.contrib.auth import logout

#from users.forms import SignUpForm #commented out

#import stuff from users.models.py to get methods


#def login(request):

#def register(request):
#	form = UserCreationForm()
#	return render(request, 'users/signup.html',{'form': form })

def logout_view(request):
    logout(request)
    return redirect('/users/login')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)#first name, last name, username, email, password 1 & 2
        if form.is_valid():
            user = form.save(commit=False)
            #user.refresh_from_db()  # load the profile instance created by the signal
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

            return redirect('/users/account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('/dashboard/')
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
