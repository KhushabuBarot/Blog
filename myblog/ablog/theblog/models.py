from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime,date

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 255)
    title_tag = models.CharField(max_length = 255, default="My Awesome Blog!")
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    body = models.TextField()
    post_date=models.DateField(auto_now_add='True')
    like=models.ManyToManyField(User, related_name='blog_posts')

    def __str__(self):
            return self.title + '   |   ' + str(self.author)


   
    def get_absolute_url(self):
        
          # return HttpResponseRedirect(reverse('article_details', args=[str(self.pk)]))
            return HttpResponseRedirect( reverse('update_post',args=[str(self.pk)]))




def total_likes(self):
     return self.like.count()