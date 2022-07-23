from django.db import models
from django.db.models import SET_NULL, CASCADE
from users.models import User
from post.models import Post


# Create your models here.

class Comment(models.Model):
    content = models.TextField()
    created_At = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=CASCADE, null=True)


