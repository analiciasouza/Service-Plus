from django.db import models
from home.models.categorias import Categoria

class Servico(models.Model):
    title = models.CharField(max_length=255)
    professional = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, default=1)
    image = models.ImageField(upload_to='servicos/', null=True, blank=True)
    
    def __str__(self):
       return self.title 