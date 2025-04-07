from django.db import models
from django.urls import reverse
from home.models.categorias import Categoria
from home.models.profissionais import Profissional

class Servico(models.Model):

    def get_absolute_url(self):
        return reverse("servicos:detail_servico", kwargs={"servico_id": self.pk})
    
    title = models.CharField(max_length=255)
    professional = models.ForeignKey(Profissional, on_delete=models.PROTECT, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, default=1)
    image = models.ImageField(upload_to='servicos/', null=True, blank=True)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
       return self.title 