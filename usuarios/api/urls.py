from django.urls import path
from usuarios.api import views

urlpatterns = [
    path('', views.UserList.as_view(), name='usuarios'),
    path('<int:pk>', views.UserDetail.as_view(), name='usuario'),
    ]