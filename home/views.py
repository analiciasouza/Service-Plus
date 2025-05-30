from django.shortcuts import render 
from .models.servicos import Servico
from .models.categorias import Categoria


# Create your views here.
def home(request):
    categorias = Categoria.objects.all()
    servico = Servico.objects.all()
    context = {
        'categorias' : categorias,
        'servico' : servico }
    
    return render(request, 'home/home.html', context) 