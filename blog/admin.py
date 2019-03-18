from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Category, Post

# Actions

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'state', 'pub_date']
    ordering = ['title']
    actions = ['make_published','make_unpublished','make_draft']

    def make_draft(self, request, queryset):
        queryset.update(state=1)
    make_draft.short_description = _('admin_post_state_draft')

    def make_published(self, request, queryset):
        queryset.update(state=2)
    make_published.short_description = _('admin_post_state_publish')

    def make_unpublished(self, request, queryset):
        queryset.update(state=3)
    make_unpublished.short_description = _('admin_post_state_unpublish')


# Register your models here.
admin.site.register(Category)
admin.site.register(Post, PostAdmin)