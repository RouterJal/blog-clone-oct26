from django.urls import reverse_lazy
from .models import Post
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
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

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post-delete.html'
    success_url = reverse_lazy('post_list')