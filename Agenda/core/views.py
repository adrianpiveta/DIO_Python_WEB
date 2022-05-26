from django.shortcuts import render, HttpResponse

# Create your views here.
from core.models import Evento


def localEvento(request, localEvento):
    local = Evento.retornaLocal(localEvento)
    return HttpResponse('<h1> Local do evento {} : {} '.format(localEvento, local))

def listaEventos(request):
    usuario = request.user
    try:
        evento  = Evento.objects.filter(usuario = usuario)
    except:
        evento = None
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)

"""
def index(request):
    return (redirect('/agenda/'))
"""




