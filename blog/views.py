from .models import Post
from django.views.generic import ListView, DetailView

class PostListView(ListView):
    model = Post
    template_name = 'read.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'details.html'

