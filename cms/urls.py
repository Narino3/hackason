from django.urls import path
from . import views1, views2, views3, views4


#ユーザがトップページにアクセスしたらIndexViewを表示
urlpatterns = [
    path('', views1.IndexView.as_view(), name='book'),
    path('oubo/', views2.OuboView.as_view(), name='book'),
    path('bosyu/', views3.BosyuView.as_view(), name='book'),
    path('zibun/', views4.ZibunView, name='zibun'),
]