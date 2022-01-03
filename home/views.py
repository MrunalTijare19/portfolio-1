from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse('This is about me')

def projects(request):
    pass

def work(request):
    pass

def education(request):
    pass





