"""Agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler404
from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('evento/<localEvento>', views.localEvento),
    path('agenda/', views.listaEventos),
    path('agenda/evento/', views.evento),
    path('agenda/lista/', views.json_lista_eventos),
    path('agenda/evento/submit', views.submit_evento),
    path('agenda/evento/delete/<int:id_evento>', views.delete_evento),
    path('', RedirectView.as_view(url='/agenda')),
    #path('/', RedirectView.as_view(url='login_user')),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout', views.logout_user),
    path('agendaPassada', views.lista_eventos_passados),
]

def handler404(request, exception):
    return render(request, '404.html')