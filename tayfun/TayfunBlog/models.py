from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
#pillow
#django
#django-ckeditor

class Post(models.Model):
   title = models.CharField(max_length=255)
   title_tag= models.CharField(max_length=255, default = "")
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   body = RichTextField(blank=True, null=True)
   #body = models.TextField()
   postDate = models.DateField(auto_now_add=True)
   category = models.CharField(max_length=255, default='not-categorized')
   snippet = models.TextField()
   header_img = models.ImageField(null = True,blank = True, upload_to="img/")
   likes = models.ManyToManyField(User, related_name='blog_post')
   
   def __str__(self):
       return self.title + ' | '+ str(self.author)
   
   def get_absolute_url(self):
     
       return reverse('home')
   
   def total_likes(self):
       return self.likes.count()
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
      
        return reverse('home')
    
class Comment(models.Model):
    post =  models.ForeignKey(Post,related_name = "comments" ,on_delete=models.CASCADE)
    name =  models.CharField(max_length=255)
    body =  models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)
    
    
    