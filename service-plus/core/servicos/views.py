from django.shortcuts import render
# from django.http import HttpResponse

def detail_servico(request):
    return render(request, 'servicos/detail_servico.html')
