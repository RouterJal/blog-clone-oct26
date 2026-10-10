from .models import Post
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView

class PostListView(ListView):
    model = Post
    template_name = 'read.html'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post-update.html'
    fields = ['title', 'content']

class PostDetailView(DetailView):
    model = Post
    template_name = 'details.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post-create.html'
    fields = ['title', 'content', 'author']