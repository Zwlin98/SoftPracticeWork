from django.urls import path
from . import views

app_name = 'hotel'

# TODO 添加urlpattern
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('regeister/', views.CustomerRegisterView.as_view(), name='register'),
    path('leave/', views.CustomerLogOutView.as_view(), name='leave'),
    path('manage/', views.RoomManageView.as_view(), name='manage')
]
