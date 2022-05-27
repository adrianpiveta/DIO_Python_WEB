from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.


def hello(request, nome, idade):
    return HttpResponse('<h1>Hello world {} {}<h1>'.format(nome, idade))  # interpreta como html, passa parametros


def soma(request, numero1, numero2):
    rsoma = float(numero2) + (float(numero1))
    return HttpResponse('<H1>A soma é {}</H1>'. format(rsoma))

def multiplicacao(request, numero1, numero2):
    rMultiplicacao = int(numero1) * int(numero2)
    return HttpResponse('<h1>Multiplicacao de {}  X {} = {}</h1>'.format(numero1, numero2, rMultiplicacao))

def divisao(request, numero1, numero2):
    rdivisao = int(numero1) / int(numero2)
    return HttpResponse('<h1>Divisão de {}  / {} = {}</h1>'.format(numero1, numero2, rdivisao))

def subtracao(request, numero1, numero2):
    resultado_subtracao = int(numero1) - int(numero2)
    return HttpResponse('<h1> Resultado da subtração de {} - {} == {} </h1>'.format(numero1, numero2, resultado_subtracao))