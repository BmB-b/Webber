from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [

    # Basic route
    path('', views.home, name='index'),

]