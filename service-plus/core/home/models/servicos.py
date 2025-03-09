from django.db import models
from django.urls import reverse
from home.models.categorias import Categoria

class Servico(models.Model):

    def get_absolute_url(self):
        return reverse("servicos:detail_servico", kwargs={"servico_id": self.pk})
    
    title = models.CharField(max_length=255)
    professional = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, default=1)
    image = models.ImageField(upload_to='servicos/', null=True, blank=True)
    
    def __str__(self):
       return self.title 