from django.contrib import admin

# Register your models here.

#Registramos aqui as classes
from core.models import Evento

# na administração do evento mostra colunas
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')
    list_filter = ('titulo',) # criamos filtro de acordo com o campo da tabela

admin.site.register(Evento, EventoAdmin)
