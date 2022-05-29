from datetime import datetime, timedelta

from django.conf.urls import handler404
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http.response import Http404, JsonResponse

# Create your views here.
from core import models
from core.models import Evento


def localEvento(request, localEvento):
    local = Evento.retornaLocal(localEvento)
    return HttpResponse('<h1> Local do evento {} : {} '.format(localEvento, local))

@login_required(login_url='/login/') #quando não encontra login, redireciona, quando não colocamos / antes, ele concatena
def listaEventos(request):
    usuario = request.user
    data_atual = datetime.now() - timedelta(hours=1) #intervalo, hora atual menos 1 hr
    try:
        evento  = Evento.objects.filter(usuario = usuario,
                                        data_evento__gt=data_atual) #__gt quer dizer que seja maior ou igual, LT data menor
    except:
        evento = None
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')
def lista_eventos_passados(request):
    usuario = request.user
    data_atual = datetime.now()
    try:
        eventos = Evento.objects.filter(usuario = usuario)
    except:
        eventos =  None

    eventos_retorno=[]
    for evento in eventos:
        if(evento.data_evento <datetime.now()):
            eventos_retorno.append(evento)
    print(eventos_retorno)
    dados = {'eventos': eventos_retorno}
    return render(request, 'agenda.html', dados)



def login_user(request):
    return render(request, 'Login.html')

def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST: #Verifica se é post
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(username=usuario, password=senha)
        if( user is not None):
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuario ou senha incorreto') #// manda essa mensagem ao html
    return redirect('/')

@login_required(login_url= '/login')
def evento(request):
    id=request.GET.get('id')
    dados ={}
    if(id):
        dados['evento'] = Evento.objects.get(id = id)
    return render(request, 'evento.html', dados)

@login_required(login_url= '/login')
def submit_evento(request):
    if(request.POST):
        id_evento = request.POST.get('id_evento')
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        local =  request.POST.get('local')
        usuario = request.user
        print("ID: ", end='')
        print(id_evento)
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if(evento.usuario== usuario):
                Evento.objects.filter(id=id_evento).update(titulo=titulo,
                                                       data_evento=data_evento,
                                                       descricao=descricao,
                                                       local=local)
        else:
            Evento.objects.create(titulo=titulo,
                              data_evento=data_evento,
                              descricao=descricao,
                              usuario=usuario,
                              local=local)
    return redirect('/')

@login_required(login_url= '/login/')
def delete_evento(request, id_evento):
    try:
        evento = Evento.objects.get(id=id_evento)
    except:
        raise Http404()
    if (request.user == evento.usuario):
        evento.delete()
    else:
        raise Http404()
    return redirect('/')

@login_required(login_url= '/login/')
def json_lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario).values('id', 'titulo')  #nome campos
    return JsonResponse(list(evento), safe=False)
