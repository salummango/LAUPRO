from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404

# Create your views here.
# def home(request):
#     return render(request, 'index.html')

def post_list(request):
    posts=Post.published.all()
    return render(request,'list.html',{'posts':posts})

def post_detail(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    return render(request,'detail.html',{'post':post})