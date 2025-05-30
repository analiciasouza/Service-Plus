from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from servicos.views import detail_servico, list_servicos

app_name = 'servicos'

urlpatterns = [
    path("<int:servico_id>/", detail_servico, name="detail_servico"),
    path("", list_servicos, name='list_servicos')
    ]