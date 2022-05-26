from django.db import models
from django.contrib.auth.models import User


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

    # retorno da função, retorna titulo ao invés do objeto
    def __str__(self):
        return self.titulo
