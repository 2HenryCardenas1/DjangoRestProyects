from django.contrib import admin
from post.models import Post


# Aca le indicamos que el modelo POST quiero que me aparesca en DJango Admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    pass
