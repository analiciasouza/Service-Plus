from django.contrib import admin
from home.models.categorias import Categoria
from home.models.servicos import Servico
from home.models.profissionais import Profissional


# Register your models here.
admin.site.register(Categoria)
admin.site.register(Servico)
admin.site.register(Profissional)
