from django.contrib import admin
from home.models.categorias import Categoria
from home.models.servicos import Servico


# Register your models here.
admin.site.register(Categoria)
admin.site.register(Servico)
