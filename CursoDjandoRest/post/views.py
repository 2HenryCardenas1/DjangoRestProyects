from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from post.models import Post


class HelloWorld(View):
    def get(self, request):
        post = Post.objects.all()

        return render(request, 'index.html', {'list' : post})
