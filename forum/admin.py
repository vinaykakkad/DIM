from django.contrib import admin
from .models import Post, Tags, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_on", "slug")
    search_fields = ["title", "text"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Tags)
admin.site.register(Comment)
