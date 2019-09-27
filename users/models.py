from django.db import models
from django.contrib.auth.models import User, AbstractUser
from team.models import Team
from django.dispatch import receiver
from django.db.models.signals import post_save

#this works
class CustomUser(AbstractUser):
	team = models.ForeignKey(Team, to_field='team_id', on_delete=models.CASCADE, default=0)

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)

@receiver(post_save, sender=CustomUser)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()