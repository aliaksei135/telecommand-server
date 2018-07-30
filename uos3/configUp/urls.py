from django.urls import path

from . import views

app_name = 'configUp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('config.html', views.ConfigView.as_view(), name='config'),
    path('configThanks.html', views.ThanksView(type=0).as_view(), name='configThanks'),
    path('listConfigs.html', views.ListConfigsView.as_view(), name='listConfigs'),
    path('configDel.html', views.DelView.as_view(), name='del'),
    path('delThanks.html', views.ThanksView(type=1).as_view(), name='delThanks')
]