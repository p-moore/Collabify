from django.urls import path, include
from . import views as team_views
from board import views as board_views
'''
'from .' means the current directory
'''

urlpatterns = [
	path('',team_views.home, name="team"),
	path('board/', include('board.urls')),
	#path('team_creation', team_views.team_creation.as_view(), name='team_creation'),#def need to check team creation method
    path('team_creation/', team_views.team_creation.as_view(), name='team_creation'),
]