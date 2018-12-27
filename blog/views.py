from django.views.generic import TemplateView

from django.shortcuts import render

# Create your views here.
class BlogIndex(TemplateView):
    template_name = "blog/blog_index.html"
