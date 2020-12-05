from django.urls import path
from . import views

from .views import IndexView, AboutView

#ユーザがトップページにアクセスしたらIndexViewを表示
urlpatterns = [
    path('', IndexView.as_view()),
    path('about/', AboutView.as_view()),
    #path('', views.MemberList.as_view(), name='book'),
]