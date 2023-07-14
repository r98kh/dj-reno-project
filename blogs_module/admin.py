from django.contrib import admin
from . import models
# Register your models here.


class BlogsAdmin(admin.ModelAdmin):
    # list_filter =  ['is_active']
    list_display = ['title', 'demonstrable']


admin.site.register(models.Blogs, BlogsAdmin)