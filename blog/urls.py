from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [

    # Display all posts
    path('', views.BlogIndex.as_view(), name='index'),

    # Add new post
    path('add/', views.PostCreate.as_view(), name='create'),
    
    # Update exists post
    #path('<int:pk>/', views.PostUpdate.as_view(), name='update'),
    
    # Delete exists post
    #path('<int:pk>/delete/', views.PostDelete.as_view(), name='delete'),
]