from django.urls import path
from . import views 
'''
'from .' means the current directory
'''

urlpatterns = [
    path('', views.dashboard, name='dashboard'),#calls views.home()
#    path('about/', views.about, name='blog-about'),
]