from django.shortcuts import render
from django.http import HttpResponse

from .models import Pytanie
# Create your views here.

def index(request):
    lista_pytan = Pytanie.objects.order_by('-data_publikacji')[:5]
    tekst = ',\n '.join([p.tekst_pytania for p in lista_pytan])
    return HttpResponse(f'Witaj w Ankietach cukierni! {tekst}')

def detale(request, pytanie_id):
    return HttpResponse(f'Wybrałeś szczegóły pytania { pytanie_id }')

def wyniki(request, pytanie_id):
    return HttpResponse(f'Oglądasz wyniki głosowaniania dla pytyania  { pytanie_id }')

def glosuj(request, pytanie_id):
    return HttpResponse(f'Głosujesz na pytanie  { pytanie_id }')