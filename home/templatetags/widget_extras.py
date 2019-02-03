from django import template
from django.template.loader import render_to_string
from blog.models import Post
import uuid

register = template.Library()

@register.simple_tag(takes_context=True)
def widget_extras(context, item):
    try:
        q = Post.objects.filter(cat=item.content.identy, state=3)
        posts = q.random(5)
    except NoReverseMatch:
        posts = 'Database error'
    return render_to_string('home/widget/sidebar_widget.html',{ 'posts':posts, 'category': item })