from django.urls import path

from . import views

app_name = 'contact'

urlpatterns = [

    # Basic route
    path('', views.ContactIndex.as_view(), name='index'),
    path('send', views.send, name='send'),
    path('thanks', views.thanks, name='thanks'),

]