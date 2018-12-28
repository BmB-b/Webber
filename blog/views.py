from django.views.generic import ListView

from django.shortcuts import render

from .models import Post

# Create your views here.
class BlogIndex(ListView):
    model = Post
    template_name = 'blog/blog_index.html'
    context_object_name = 'context'

    def get_context_data(self, **kwargs):
        context = super(BlogIndex, self).get_context_data(**kwargs)
        context['counter'] = Post.objects.count()
        return context

