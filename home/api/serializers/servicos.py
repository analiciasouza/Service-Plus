from rest_framework import serializers
from home.models.servicos import Servico

class ServicoSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
            fields = ['title' , 'profissional' , 'categoria' , 'image' ,'descricao']