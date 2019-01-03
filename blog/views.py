from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.shortcuts import render, redirect
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
        filter_set = Post.objects.all()
        counter = filter_set.count()
        
        if self.request.GET.get('filter'):
            query = self.request.GET.get('filter')

            # Simple secure
            if query in str(range(1,3)):
                filter_set = filter_set.filter(state=query)
                counter = filter_set.count()
            else:
                redirect('blog:index')

        context['counter'] = counter
        context['filter'] = filter_set
        return context

class PostCreate(CreateView):
    model = Post
    fields = ['title','body','pub_date','state','cat','thumb']
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreate,self).form_valid(form)



class PostView(DetailView):
    model = Post

class PostEdit(UpdateView):
    model = Post
    fields = ['title','body','pub_date','state','author','cat','thumb']

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')