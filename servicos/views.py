from django.shortcuts import render
from home.models.servicos import Servico


def list_servicos(request):
    servicos = Servico.objects.all()
    context = {
        'servicos' : servicos
    }
    return render(request, 'servicos/secao-servicos.html', context )


def detail_servico(request, servico_id):
    servico = Servico.objects.get(pk=servico_id)
    context = {
        'servico': servico
    }
    return render(request, 'servicos/servico.html', context)
