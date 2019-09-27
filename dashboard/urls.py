from django.urls import path, include
from . import views 
from team import views as team_views
'''
'from .' means the current directory
'''

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('team/', include('team.urls')),
]