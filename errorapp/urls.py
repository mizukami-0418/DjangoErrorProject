from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('trigger-500/', views.trigger_500, name='trigger500'), # 500エラーを発生させるためのルート
]

