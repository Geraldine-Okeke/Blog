from django.contrib import admin
from .models import Post, Image

class ImageInline(admin.TabularInline):  # You can use 'admin.StackedInline' if you prefer a different display style
    model = Image
    extra = 3  # Number of empty image fields to display

class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Image)
