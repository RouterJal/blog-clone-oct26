from .models import Post
from django.views.generic import ListView

class PostListView(ListView):
    model = Post
    template_name = 'read.html'

