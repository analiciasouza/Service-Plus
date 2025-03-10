from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from servicos.views import detail_servico


urlpatterns = [path("<int:servico_id>/", detail_servico, name="detail_servico")]
