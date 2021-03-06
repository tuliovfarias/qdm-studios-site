from django.contrib import admin
from .models import Post, Slide

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter=('datetime',)
    list_display=('title','datetime', 'author')

class SlideAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter=('title',)
    list_display=('title',)

admin.site.register(Post, PostAdmin)
admin.site.register(Slide, SlideAdmin)