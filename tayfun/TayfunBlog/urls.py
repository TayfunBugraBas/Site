from django.urls import path
from . import views
from .views import HomeView, ArtDetail, AddPostView








urlpatterns = [
   # path('',views.home, name = "home" ),
   path('',HomeView.as_view(),name='home'),
   path('article/<int:pk>',ArtDetail.as_view(),name='article-details'),
   path('MakePost/',AddPostView.as_view(), name = 'Make'),
]

