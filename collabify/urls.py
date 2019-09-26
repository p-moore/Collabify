"""collabify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views
from django.contrib import admin
#from dashboard import views as core_views
from django.conf import settings
from django.conf.urls.static import static

from dashboard import views as dash_views
from . import views as core_views
from users import views as user_views

urlpatterns = [
    #path('', core_views.redirect_view,name='redirect'),#sets url to include Collabify
    #path('Collabify/', core_views.home,name='index'),#change?
    #path('Collabify/dashboard/', core_views.dashboard, name='dashboard'),#need to check this method a little
    path('', core_views.home,name='index'),

    #this might not work 'users/login.html'
    path('users/', include('users.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('team/', include('team.urls')),    

    #commented this out -- needs to go to team
    #path('team_creation', core_views.team_creation.as_view(), name='team_creation'),#def need to check team creation method
    #path('team_info', core_views.team_info, name='team_info'),
    
    #needs to go to board
    #path('board', core_views.board, name='board'),


    #don't think I'm implementing this yet
    #path('attendance', core_views.attendance, name='attendance'),
    

    
    #needs to go to users
    #path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    #path('account_activation_sent/', core_views.account_activation_sent, name='account_activation_sent'),
    #path('activate/<uidb64>/<token>/',core_views.activate, name='activate'),#possibly try to redo this
    #path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    #path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    
    path('admin/', admin.site.urls)
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
