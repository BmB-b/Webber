from django.shortcuts import render

# Other route
def about(request):
    return render(request, 'webber/about.html')