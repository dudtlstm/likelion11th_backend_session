from django.shortcuts import render

# Create your views here.
def mainpage(request): # 'mainpage'라는 이름 함수 선언
    return render(request, 'main/mainpage.html')

def secondpage(request): # 'secondpage'라는 이름 함수 선언
    return render(request, 'main/secondpage.html')