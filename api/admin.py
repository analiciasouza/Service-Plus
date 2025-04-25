from django.contrib import admin
from api.models.categoria import Categoria
from api.models.servico import Servico
from api.models.profissional import Profissional

admin.site.register(Categoria)
admin.site.register(Servico)
admin.site.register(Profissional)
