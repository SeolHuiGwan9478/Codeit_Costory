from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator
from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView
)
from django.urls import reverse
#from django.views import View
class PostListView(ListView):
    model = Post
    #template_name = 'posts/post_list.html'
    #context_object_name = 'posts'
    ordering = ['-dt_created']
    paginate_by = 6
    #page_kwarg = 'page'

class PostDetailView(DetailView):
    model = Post
    #template_name = 'posts/post_detail.html'
    #context_object_name = 'post'
    #pk_url_kwarg = 'post_id'    

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk':self.object.id})

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse('post_detail', kwarg={'pk': self.object.id})

class PostDeleteView(DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('post-list')
    
class IndexRedirectView(RedirectView):
    pattern_name = 'post-list'