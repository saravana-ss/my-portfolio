from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    #return render(request, 'home.html')
    context = {'name' : 'Saravana', 'course' : 'Django'}
    return render(request, 'home.html', context)

def about(request):
    return HttpResponse("This is my homepage(/)")

def contact(request):
    return HttpResponse("This is my homepage(/)")

def projects(request):
    #return HttpResponse("This is my homepage(/)")
    return render(request, 'projects.html')

    