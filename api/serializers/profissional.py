from api.models.profissional import Profissional
from rest_framework import serializers
    
class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = '__all__'