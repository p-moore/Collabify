from django.urls import path
from . import views as board_views
'''
'from .' means the current directory
'''

urlpatterns = [
	path('', board_views.board, name='board'),#create method for board that will load the board
]