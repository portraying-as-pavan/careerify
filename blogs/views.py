from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from .models import Post
from .forms import PostForm
from django.utils import timezone

# Create your views here.

def post_list(request):
	posts=Post.objects.order_by('-created_on')
	return render(request,'blogs/post_list.html',{'posts':posts})    


def post_detail(request,pk):
	post=get_object_or_404(Post,pk=pk)
	return render(request,'blogs/post_detail.html',{'post':post})


def post_new(request):
	if request.method=="POST":
		form=PostForm(request.POST)

		if form.is_valid():
			post=form.save(commit=False)
			post.created_on = timezone.now()
			post.save()
			return redirect('post_detail',pk=post.pk)
	else:
		form=PostForm()
	return render(request,'blogs/post_edit.html',{'form':form})

def post_edit(request,pk):
	post=get_object_or_404(Post,pk=pk)
	if request.method=="POST":
		form=PostForm(request.POST, instance=post)
		if form.is_valid():
			post=form.save(commit=False)
			post.updated_on=timezone.now()
			post.save()
			return redirect('post_detail',pk=post.pk)
	else:
		form=PostForm(instance=post)
	return render(request,'blogs/post_edit.html',{'form':form})
     