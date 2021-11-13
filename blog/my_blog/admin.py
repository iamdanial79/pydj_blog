from django.contrib import admin
from .models import *

class advancesuserprofile(admin.ModelAdmin):
    list_display = ['user','description']

admin.site.register(userprofile,advancesuserprofile)
    

class advancecategory(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
admin.site.register(Category,advancecategory)


class advancearticle(admin.ModelAdmin):
    search_filed = ['title','author']
    list_display = ['title','category', 'created_at']
admin.site.register(article,advancearticle)
