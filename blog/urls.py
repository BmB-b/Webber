from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    # Index
    path('', views.BlogIndex.as_view(), name='index'),

    # Add
    path('add/', views.PostCreate.as_view(), name='add'),
]