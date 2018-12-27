from django.shortcuts import render

def index(request):
    return render(request, 'webber/index.html')

def about(request):
    return render(request, 'webber/about.html')