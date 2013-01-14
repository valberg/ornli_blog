from django.contrib import admin
from blog import models

class PostAdmin(admin.ModelAdmin):
    model = models.Post
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(models.Post, PostAdmin)
