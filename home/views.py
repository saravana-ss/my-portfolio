from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    #return render(request, 'home.html')
    context = {'name' : 'Saravana', 'course' : 'Django'}
    return render(request, 'home.html', context)

def about(request):
    context = {'name' : 'Saravana', 'course' : 'Django'}
    return render(request, 'about.html', context)

def contact(request):
    context = {'name' : 'Saravana', 'course' : 'Django'}
    return render(request, 'contact.html', context)

def projects(request):
    context = {'name' : 'Saravana', 'course' : 'Django'}
    return render(request, 'projects.html', context)

    