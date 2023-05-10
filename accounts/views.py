from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User 
from .models import Profile
# auth 라이브러리를 상속받는 코드
# Django의 'contrib.auth' 앱에서 'auth' 모듈을 가져오는 코드
# 'authenticate()', 'login()', 'logout()' 함수 등 제공

# Create your views here.
# 로그인 함수
def login(request):
    if request.method == 'POST':
    # 사용자가 로그인 폼을 요청하면 GET 메서드를 통해 로그인 폼을 전송하고, 사용자가 로그인 정보를 입력
        username = request.POST['username']
        password = request.POST['password']
        # 사용자가 로그인 폼에서 입력한 'username'과 'password' 값을 가져옴
        # 이 값들은 'request.POST'에 저장되어 있으며, 딕셔너리 형태로 접근할 수 있음

        user = auth.authenticate(request, username=username, password=password)
        # authenticate 함수를 호출하여 사용자 인증 진행
        # auth 모듈에서 제공되는 함수로서 'request'객체와 username, password값을 인자로 받음
        # 'authenticate' 함수는 'username'과 'password' 값을 확인하여 해당 사용자가 인증될 수 있는지를 검사하고, 인증된 사용자 객체를 반환.
        # 인증에 실패한 경우에는 'None' 값을 반환

        if user is not None:
            auth.login(request, user) # auth.login 함수를 통해 해당 사용자 로그인시킴, request객체와 인증된 사용자 객체를 인자로 받음
            return redirect('main:mainpage') # 이동할 페이지 지정(main의 mainpage라는 url패턴으로 이동)

        else:
            return render(request, 'accounts/login.html') # 다시 로그인 폼을 보여줌

        # redirect와 render
        # main:mainpage의 url 브라우저로 이동시키는 역할, 로그인 성공 후에 사용자가 이동하는
        # 페이지이기 때문에 바로 이동시켜줌. 브라우저를 다른 페이지로 이동시킴
        # render은 주어진 템플릿 파일을 렌더링하여 html 페이지 생성, 템플릿 파일을 렌더링하여
        # html 페이지를 생성하고 이를 사용자에게 보여줌. 다시 로그인 폼을 보여주어야 하기 떄문에 render함수 사용
        # render함수는 html페이지를 생성하여 보여주는 역할을 함

    elif request.method == 'GET':
        return render(request, 'accounts/login.html')
    # HTTP 요청의 메서드가 GET인 경우 'accounts/login.html' 템플릿을 렌더링하여 클라이언트에게 전달
    # POST 메서드를 통해 로그인 정보를 처리하는 기능을 구현하고자 할 때 사용하는 함수

# 로그아웃 함수
def logout(request): # 현재 요청(request)에 대해 인증된 사용자를 로그아웃 시키는 함수
    auth.logout(request)
    return redirect('main:mainpage')

# 회원가입 함수
def signup(request):
    if request.method == 'POST':
        
        if request.POST['password'] == request.POST['confirm']:
            # 사용자가 입력한 비밀번호와 비밀번호 확인 값이 일치하는지 확인
            user = User.objects.create_user( # User 모델을 이용해 새로운 사용자를 생성
                username = request.POST['username'],
                password = request.POST['password']
            )
        # create_user 함수는 인자로 전달된 사용자 이름과 비밀번호로 새로운 사용자를 생성하며, 생성된 사용자 객체를 반환
            nickname = request.POST['nickname']
            department = request.POST['department']

            profile = Profile(user=user, nickname=nickname, department=department)
            profile.save()

            auth.login(request, user) # 새로운 사용자 객체로 로그인
            return redirect('/') # 사용자를 메인 페이지로 리다이렉트
    return render(request, 'accounts/signup.html') # 요청 방식이 POST가 아닐 경우, 회원가입 페이지를 렌더링