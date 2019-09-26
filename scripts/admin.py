from django.contrib import admin
#from scripts.models import attendance #commented this
#from scripts.forms import PostteamForm #commented this


#admin.site.register(attendance) #changed this

'''
#commented all of this
class teamcreationAdmin(admin.ModelAdmin):
    form = PostteamForm
    def save_model(self, request, obj, form, change):
        obj.team_created_by = request.user.username
        obj.save()
'''