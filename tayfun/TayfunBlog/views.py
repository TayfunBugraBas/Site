from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category,  Comment
from .forms import FormPost, FormPostUpdate,AddComment
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


#def home(request):
 #   return render(request, 'home.html', {})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-details', args=[str(pk)]))



class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-postDate']
    
    def get_context_data(self, *args, **kwargs):
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
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArtDetail,self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        return context
    
    
    
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
    
    
class AddCommentView(CreateView):
    model = Comment
    form_class = AddComment
    template_name = 'add_comment.html'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    #fields = '__all__'
    success_url = reverse_lazy('home')

# Create your views here.
