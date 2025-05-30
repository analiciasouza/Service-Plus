from rest_framework import serializers
from home.models.categorias import Categoria

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
          model = Categoria
          fields = ['nome' , 'imagem']
    