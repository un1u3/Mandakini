from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404
from .models import Post 
from django.contrib.auth.models  import User
from django.views.generic import ListView, DetailView,CreateView ,UpdateView,DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.
# def home(request):
   
    
#     context = {
#         'posts':Post.objects.all()
#     }
#     return render(request,'blog/home.html',context)



class PostListView(ListView):
    model = Post # Kun chai model bata data line ho 
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by= 13
    
    
class UserPostListView(ListView):
    model = Post # Kun chai model bata data line ho 
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    
    paginate_by= 7
    
    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('blog-home')
    
    


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_success_url(self):
        return reverse('blog-home')
  
  
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_success_url(self):
        return reverse('blog-home')
     


    
    
    



    
    
    

def about(request):
    return render(request,'blog/about.html')