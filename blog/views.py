from django.urls import reverse_lazy
from .models import Post
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class PostListView(ListView):
    model = Post
    template_name = 'read.html'

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post-update.html'
    fields = ['title', 'content']

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'details.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post-create.html'
    fields = ['title', 'content', 'author']

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post-delete.html'
    success_url = reverse_lazy('post_list')
