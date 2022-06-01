from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

#def home(request):
 #   return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    
class ArtDetail(DetailView):
    model = Post
    template_name = 'artDet.html'
    
class AddPostView(CreateView):
    model = Post
    template_name = 'Post-add.html'
    fields = '__all__'

# Create your views here.
