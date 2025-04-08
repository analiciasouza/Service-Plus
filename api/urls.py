from django.urls import path
from api import views


urlpatterns = [
    path('profissionais/', views.profissional_view),
    path('profissionais/<int:pk>/', views.profissional_detail)
]
