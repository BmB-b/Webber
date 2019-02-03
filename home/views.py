from django.shortcuts import render
from django.http import Http404
from .models import Widget

# Create your views here.
def home(request):
    try:
        q = Widget.objects.filter(state=1)
    except Widget.DoesNotExist:
        raise Http404('Widgets disappear? Something went wrong!')
    return render(request, 'home/widget/home_slider.html', {'widgets':q}) # Temporary