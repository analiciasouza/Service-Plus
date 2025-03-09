from django.shortcuts import render
from home.models.servicos import Servico

def detail_servico(request, servico_id):
    servico = Servico.objects.get(pk=servico_id)
    context = {
        'servico': servico
    }
    return render(request, 'servicos/servicos.html', context)