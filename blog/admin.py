from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter=('datetime','title')
    list_display=('datetime','title', 'author')

admin.site.register(Post, PostAdmin)