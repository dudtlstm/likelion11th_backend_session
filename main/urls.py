from django.urls import path
from .views import * # main 앱의 views를 이용하기 위해 작성하는 코드

app_name="main"
urlpatterns = [
    path('', mainpage, name="mainpage"),
    path('second/', secondpage, name="secondpage"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('<int:id>', detail, name="detail"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
]