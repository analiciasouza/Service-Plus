from rest_framework import serializers
from home.models.profissionais import Profissional


class ProfissionalSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
        model = Profissional
        fields = ['nome_completo' , 'profissao' , 'data_de_nescimento' , 'image']
