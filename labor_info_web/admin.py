from django.contrib import admin

from .models import BlogPost, ContactRequest

admin.site.register(BlogPost)
admin.site.register(ContactRequest)
