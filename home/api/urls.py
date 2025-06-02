from django.urls import path
from home.api import views

urlpatterns = [
    path('categorias', views.CategoriaList.as_view(), name='categorias'),
    path('profissionais', views.ProfissionalList.as_view(), name='profissionais'),
    path('profissional/<int:pk>', views.ProfissionalDetail.as_view(), name='profissional'),
    path('servicos', views.ServicoList.as_view(), name='servicos'),
    path('servico/<int:pk>', views.ServicoDetail.as_view(), name='servico')
    ]