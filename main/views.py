from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone

# Create your views here.
def mainpage(request): # 'mainpage'라는 이름 함수 선언
    blogs = Blog.objects.all() # blogs 라는 변수에 Blog의 모든 객체를 저장 = blogs에 모든 게시물 저장
    return render(request, 'main/mainpage.html', {'blogs':blogs})

def secondpage(request): # 'secondpage'라는 이름 함수 선언
    return render(request, 'main/secondpage.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.pub_date = timezone.now()
    new_blog.body = request.POST['body']

    new_blog.save()

    return redirect('detail', new_blog.id)

def new(request):
    return render(request, 'main/new.html')

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'main/detail.html', {'blog':blog})