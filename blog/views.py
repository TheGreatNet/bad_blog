from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse
from .models import Post,Category
import markdown
from comments.forms import CommentForm

# Create your views here.
def index(request):
    post_list=Post.objects.all()
    return render_to_response("blog/index.html",context={"post_list":post_list})

def detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.body=markdown.markdown(post.body,extensions=['extra','codehilite','toc',])
    form=CommentForm()
    comment_list=post.comment_set.all()
    context={'post':post,'form':form,'comment_list':comment_list}
    return render(request,'blog/detail.html',context)

def archives(request,year,month):
    post_list=Post.objects.filter(created_time__year=year,created_time__month=month)
    return render_to_response('blog/index.html',{'post_list':post_list})

def category(request,pk):
    cate=get_object_or_404(Category,pk=pk)
    post_list=Post.objects.filter(category=cate)
    return render_to_response('blog/index.html',context={'post_list':post_list})