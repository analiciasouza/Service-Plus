from django.urls import path
from servicos.views import detail_servico

urlpatterns = [
    path('', detail_servico, name="Servico"),
]
