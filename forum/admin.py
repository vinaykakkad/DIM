from django.contrib import admin
from .models import Post, Tags

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','created_on','slug')
    list_filter = ("status",)
    search_fields = ['title', 'text']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Post, PostAdmin)
admin.site.register(Tags)
