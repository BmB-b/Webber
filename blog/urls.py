from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [

    # Display all posts
    path('', views.BlogIndex.as_view(), name='index'),

    # Add new post
    path('add/', views.PostCreate.as_view(), name='create'),
    
    # View post detail
    path('<slug:slug>-<int:pk>/', views.PostView.as_view(), name='view'),
    
    # Update exists post
    path('<slug:slug>-<int:pk>/edit', views.PostEdit.as_view(), name='edit'),
    
    # Delete exists post
    path('<slug:slug>-<int:pk>/delete', views.PostDelete.as_view(), name='delete'),
]