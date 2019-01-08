from django.urls import path

from . import views

app_name = 'contact'

urlpatterns = [

    # Basic route
    path('', views.ContactIndex.as_view(), name='index'),
    path('thanks', views.ContactSuccess.as_view(), name='thanks'),

]