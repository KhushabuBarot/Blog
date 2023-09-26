from typing import Any
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import AddPostForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect

# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model=Post
    template_name= 'home.html'
    ordering=['-post_date']
    #ordering=[ '-id']


class ArticleDetailView(DetailView):
    model=Post
    template_name='article_details.html'
    context_object_name='post'

    def get_context_data(self, **kwargs):
         context=super(ArticleDetailView,self).get_context_data(**kwargs)
         stuff=get_object_or_404(Post, id = self.kwargs['pk'])
         total_likes = stuff.total_likes()
         context = total_likes
         return context
        
        
       
   
     

class AddPostView(CreateView):
    model=Post
    template_name='add_post.html'
    fields='__all__'
    
    def get_success_url(self):
            return reverse_lazy('article_details',kwargs={'pk': self.object.pk})
    
class UpdatePostView(UpdateView):
    model=Post
    template_name= 'update_post.html'
    fields= ['title','title_tag','body']
    
    def get_success_url(self):
            return reverse_lazy('article_details',kwargs={'pk': self.object.pk})

class DeletePostView(DeleteView):
    model=Post
    template_name= 'delete_post.html'
    success_url=reverse_lazy('home')
    # def get_success_url(self):
    #         return reverse_lazy('article_details',kwargs={'pk': self.object.pk})
    
def LikeView(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    post.like.add(request.user) 
    return HttpResponseRedirect(reverse('article_details', args=[str (pk)]))



# def AddPost(request):
#     submit=False

#     if request.method == "POST":
#         form=AddPostForm(request.POST)
        
#         if form.is_valid():
#            form.save()
#            submit =True
#            form=AddPostForm
#           # return  render (request,'add_post.html',{'form':form,'submit':submit})
#            #return reverse_lazy('add_post',kwargs={'pk': submit })
#            add_post_url =reverse('home.html')
#            return HttpResponseRedirect(add_post_url +'? submitted=True')
#     else:
       
#        form=AddPostForm
       
#        return render(request,'add_post.html',{'form':form})
       


