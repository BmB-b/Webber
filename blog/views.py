from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .choices import STATE_CHOICES  

from .models import Post

# Create your views here.
class BlogIndex(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/blog_index.html'
    context_object_name = 'context'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(BlogIndex, self).get_context_data(**kwargs)
        filter_set = Post.objects.all()
        counter = filter_set.count()
        
        # GET: ?filter
        if self.request.GET.get('filter'):
            getState = self.request.GET.get('filter')

            if int(getState) in range(1, len(STATE_CHOICES)+1):
                filter_set = filter_set.filter(state=getState)
                counter = filter_set.count()
            else:
                redirect('blog:index')
        
        # GET: ?q
        if self.request.GET.get('q'):
            getTitle = self.request.GET.get('q')

            if isinstance(getTitle, str):
                filter_set = filter_set.filter(title=getTitle)
                counter = filter_set.count()
            else:
                redirect('blog:index')

        context['counter'] = counter
        context['filter'] = filter_set
        return context

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','body','pub_date','state','cat','thumb']
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreate,self).form_valid(form)



class PostView(DetailView):
    model = Post

class PostEdit(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title','body','pub_date','state','cat','thumb']

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')