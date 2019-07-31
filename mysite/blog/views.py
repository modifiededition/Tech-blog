from django.shortcuts import render
from django.views.genric import (TemplateView, ListView)
from .models import Post, Comment
# creating views using class

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_query(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post
