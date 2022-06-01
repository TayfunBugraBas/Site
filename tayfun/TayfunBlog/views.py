from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import FormPost, FormPostUpdate
from django.urls import reverse_lazy


#def home(request):
 #   return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']
class ArtDetail(DetailView):
    model = Post
    template_name = 'artDet.html'
    
class AddPostView(CreateView):
    model = Post
    form_class = FormPost
    template_name = 'Post-add.html'
    #fields = '__all__'
    
class UpdatePost(UpdateView):
    model = Post
    template_name = 'updatePost.html'
    form_class = FormPostUpdate
    #fields = ['title', 'title_tag', 'body']
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    
    




# Create your views here.
