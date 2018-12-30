from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Post

# Create your views here.
class BlogIndex(ListView):
    model = Post
    template_name = 'blog/blog_index.html'
    context_object_name = 'context'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(BlogIndex, self).get_context_data(**kwargs)
        context['counter'] = Post.objects.count()
        return context

class PostCreate(CreateView):
    model = Post
    fields = ['title','body','pub_date','state','author','cat','thumb']
    success_url = reverse_lazy('blog:index')

class PostView(DetailView):
    model = Post

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')