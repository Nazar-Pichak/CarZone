from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def contacts(request):
    return render(request, 'pages/contacts.html')
        