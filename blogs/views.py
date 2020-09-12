from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Post
from .forms import PostForm

# Create your views here.
#def home(request):
#	return HttpResponse('Hello Folks')

#class PostList(generic.ListView):
    #queryset = Post.objects.order_by('-created_on')
   # template_name = 'index.html'

#class PostDetail(generic.DetailView):
  #  model = Post
 #   template_name = 'post_detail.html'

def post_list(request):
	posts=Post.objects.order_by('-created_on')
	return render(request,'blogs/post_list.html',{'posts':posts})    


def post_detail(request,pk):
	post=get_object_or_404(Post,pk=pk)
	return render(request,'blogs/post_detail.html',{'post':post})


def post_new(request):
	form=PostForm()
	return render(request,'blogs/post_edit.html',{'form':form})

