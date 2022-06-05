from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import FormPost, FormPostUpdate
from django.urls import reverse_lazy


#def home(request):
 #   return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-postDate']
    
    def get_context_date(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
        
    
def CategoryView (request, cats):  
    category_posts = Post.objects.filter(category=cats.replace('-',' '))
    return render(request, 'categories.html', {'categories':cats.title().replace(' ','-'), 'category_posts': category_posts})
    
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
    
    
class AddCategoryView(CreateView):
    model = Category
    template_name = 'Category-add.html'
    fields = '__all__'



# Create your views here.
