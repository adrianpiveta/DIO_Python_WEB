from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


# Create your models here.
# Aqui cria-se tabelas

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    local = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de registro')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # se excluir usuario, se excui todo conteudo dele

    # cria com nome próprio a tabela, caso não queira o padrão
    class Meta:
        db_table = 'evento'

    def retornaLocal(titulo):
        try:
            localEvento = Evento.objects.get(titulo=titulo).local
        except:
            localEvento = "Evento não encontrado"
        return localEvento

    def get_data_evento (self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M HRS') # formatacao horario

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M') #padrão que o navegador necessita no input

    # retorno da função, retorna titulo ao invés do objeto
    def __str__(self):
        return self.titulo

    def get_evento_atrasado(self):
        if(self.data_evento < datetime.now()):
            return True

    def get_evento_proximo(self):
        if(self.data_evento > (datetime.now())
                and self.data_evento < (datetime.now() + timedelta(hours=1))):
            print(self.data_evento, datetime.now())
            print((datetime.now() + timedelta(hours=1)))
            return True
