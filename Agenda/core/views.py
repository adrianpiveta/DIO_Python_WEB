from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
from core.models import Evento


def localEvento(request, localEvento):
    local = Evento.retornaLocal(localEvento)
    return HttpResponse('<h1> Local do evento {} : {} '.format(localEvento, local))

@login_required(login_url='/login/') #quando não encontra login, redireciona, quando não colocamos / antes, ele concatena
def listaEventos(request):
    usuario = request.user
    try:
        evento  = Evento.objects.filter(usuario = usuario)
    except:
        evento = None
    dados = {'eventos': evento}
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
    return render(request, 'evento.html')

@login_required(login_url= '/login')
def submit_evento(request):
    if(request.POST):
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        Evento.objects.create(titulo=titulo,
                              data_evento=data_evento,
                              descricao=descricao,
                              usuario=usuario)
    return redirect('/')

"""
def index(request):
    return (redirect('/agenda/'))
"""