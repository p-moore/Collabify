from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views
'''
'from .' means the current directory
'''

urlpatterns = [
	#path('', user_views.home,name="user_home") #not exactly sure what this would do
	path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('signup/', user_views.signup, name='signup'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('logout/', user_views.logout_view, name='logout'),
    path('account_activation_sent/', user_views.account_activation_sent, name='account_activation_sent'),
    path('activate/<uidb64>/<token>/',user_views.activate, name='activate'),#possibly try to redo this
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]