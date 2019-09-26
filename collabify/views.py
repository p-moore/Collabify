from django.shortcuts import render

'''
def redirect(request):
    return redirect('Collabify/')
'''

def home(request):
    return render(request, 'index.html')

'''
def home(request):
	context = {
		Users.objects.all() #this would import all users from database
	}
'''