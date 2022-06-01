from django.urls import path
from . import views
from .views import HomeView, ArtDetail, AddPostView, UpdatePost, DeletePostView








urlpatterns = [
   # path('',views.home, name = "home" ),
   path('',HomeView.as_view(),name='home'),
   path('article/<int:pk>',ArtDetail.as_view(),name='article-details'),
   path('MakePost/',AddPostView.as_view(), name = 'Make'),
   path('article/edit/ArticleId/<int:pk>', UpdatePost.as_view(), name = 'update_post' ),
   path('article/delete/ArticleId/<int:pk>', DeletePostView.as_view(), name = 'delete_post' ),
]

