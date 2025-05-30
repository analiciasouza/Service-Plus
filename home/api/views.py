from rest_framework import generics
from home.models.categorias import Categoria
from home.api.serializers.categorias import CategoriaSerializer
from home.models.profissionais import Profissional
from home.api.serializers.profissionais import ProfissionalSerializer
from home.models.servicos import Servico
from home.api.serializers.servicos import ServicoSerializer

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProfissionalList(generics.ListCreateAPIView):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer


class ProfissionalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer


class ServicoList(generics.ListCreateAPIView):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

    
class ServicoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer






