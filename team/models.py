from django.db import models
from django.conf import settings
# Create your models here.

class Team(models.Model):
	team_id = models.IntegerField(primary_key=True,default = 1)
	team_name = models.CharField(max_length = 30)
	team_description = models.TextField(max_length = 500)

	def __str__(self):
		return "%d %s %s" % (self.team_id,self.team_name,self.team_description,)

	#team_members = models.ManyToManyField(settings.AUTH_USER_MODEL)
	#team_members = models.ForeignKey(settings.AUTH_USER_MODEL)
	'''team_mem_1 = models.ForeignKey(CustomUser, related_name='team_mem_1', on_delete=models.CASCADE)
	team_mem_2 = models.ForeignKey(CustomUser, related_name='team_mem_2', on_delete=models.CASCADE)
	team_mem_3 = models.ForeignKey(CustomUser, related_name='team_mem_3', on_delete=models.CASCADE)
	team_mem_4 = models.ForeignKey(CustomUser, related_name='team_mem_4', on_delete=models.CASCADE)
	'''