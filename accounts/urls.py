from django.urls import path # Django에서 URL 패턴 매칭을 처리하기 위해 사용되는 함수
from .views import *

app_name = "accounts"
urlpatterns =[
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('signup/', signup, name="signup"),
]