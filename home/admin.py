from django.contrib import admin

# Register your models here.
from home.models.categorias import Categoria
from home.models.servicos import Servico
from home.models.profissionais import Profissional

admin.site.register(Categoria)
admin.site.register(Servico)
admin.site.register(Profissional)