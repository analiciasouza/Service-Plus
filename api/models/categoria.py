from django.db import models

class Categoria(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categorias/', null=True, blank=True)

    def __str__(self):
        return self.name