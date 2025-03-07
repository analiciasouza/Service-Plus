from django.db import models

# Create your models here.
# categorias

class Categoria(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Servico(models.Model):
    title = models.CharField(max_length=255)
    professional = models.CharField(max_length=255)
    
    def __str__(self):
       return self.title 