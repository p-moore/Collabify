from django.db import models
#import something from teams (primary key = team_id)
from django.core.validators import MaxValueValidator, MinValueValidator
from team.models import Team
from users.models import CustomUser as User

# Create database for cards, board, etc
'''
class render(models.Model):
	#do stuff to render the board on startup
	#continuously call this to keep up with real time?
'''
class Task(models.Model):
	team_id = models.ForeignKey(Team, on_delete=models.CASCADE)#many to one relationship
	task_id = models.AutoField(primary_key=True)
	assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
	priority = models.CharField(max_length=4)#high,med,low
	task_name = models.CharField(max_length = 50)
	progress = models.IntegerField(#might not work
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
     )
	column = models.IntegerField(#might not work
        default=1,
        validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
        ]
     )