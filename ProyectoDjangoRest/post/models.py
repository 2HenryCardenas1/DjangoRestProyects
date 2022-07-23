from django.db import models
from django.db.models import SET_NULL
from users.models import User
from categories.models import Category


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    miniature = models.ImageField(upload_to='post/images')
    # auto_now_add es para que cada que se cree un post se cree la fecha de creacion
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    #ForeingKeys
    # SET_NULL sirve para mantener el POST aun asi si el usuario ya ha sido elimindo
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.title
