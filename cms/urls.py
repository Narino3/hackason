from django.urls import path
from . import views1, views2, views3, views4


#ユーザがトップページにアクセスしたらIndexViewを表示
urlpatterns = [
    path('', views1.list, name='recruit1'),
    path('oubo/', views2.OuboPutView.as_view(), name='book'),
    path('bosyu/', views3.BosyuView.as_view(), name='book'),
    path('zibun/', views4.ZibunView, name='book'),
    path('oubofin/', views2.OuboFinView.as_view(), name='book'),
    path('Top/', views2.TopView.as_view(), name='book'),
    path('bosyufin/', views3.BosyuFinView.as_view(), name='book'),
    path('hyouzi/', views3.ModelList.as_view(), name='book'),
    path('hyouziE/', views3.ModelEList.as_view(), name='book'),
    path('set_tag/', views3.setView.as_view(), name='book'), # 職種を作るためのurl
]