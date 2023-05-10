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
    new_blog.image = request.FILES.get('image')

    new_blog.save()

    return redirect('main:detail', new_blog.id)

def new(request):
    return render(request, 'main/new.html')

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'main/detail.html', {'blog':blog})

# 수정 화면으로 가는 코드 구현
def edit(request, id):
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'main/edit.html', {'blog' : edit_blog})

# update(수정) 기능 구현
def update(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.pub_date = timezone.now()
    update_blog.body = request.POST['body']
    update_blog.image = request.FILES.get('image', update_blog.image)
    update_blog.save()
    return redirect('main:detail', update_blog.id)

# delete(삭제) 기능 구현
def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('main:mainpage')