from django.shortcuts import render
from home.models.categorias import Categoria 
from home.models.servicos import Servico


# Create your views here.
def home_view(request):
    categorias = Categoria.objects.all()
    servico = Servico.objects.all()
    context = {
        'categorias' : categorias,
        'servico' : servico }
    
    return render(request, 'home/home.html', context)