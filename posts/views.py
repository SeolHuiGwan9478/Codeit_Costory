from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse
#from django.views import View
class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    ordering = ['-dt_created']
    paginate_by = 6
    page_kwarg = 'page'

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'    

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_list.html'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'post_id':self.object.id})

def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('post-detail', post.id)
    else:
        post_form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': post_form})

def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":   
        post.delete()
        return redirect('post-list')
    else:
        return render(request, 'posts/post_confirm_delete.html', {'post':post})
    
def index(request):
    return redirect('post-list')