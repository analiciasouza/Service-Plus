from django.db import models

class Profissional(models.Model):
    nome_completo = models.CharField(max_length=255)
    profissao = models.CharField(max_length=255)
    data_de_nascimento = models.DateField()
    image = models.ImageField(upload_to='profissionais/', null=True, blank=True)

    def __str__(self):
       return f'{self.nome_completo}-{self.profissao}'