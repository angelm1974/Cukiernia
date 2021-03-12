from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime

from .models import Pytanie
# Create your views here.

def index(request):
    teraz = datetime.datetime.now()
    lista_pytan = Pytanie.objects.order_by('-data_publikacji')[:5]
    contex= {'lista_pytan' : lista_pytan, 'czas': teraz,}
    return render(request,'ankieta/index.html',contex)

def detale(request, pytanie_id):
    try:
        pytanie = Pytanie.objects.get(pk = pytanie_id)
    except Pytanie.DoesNotExist:
        raise Http404('Nie ma takiego pytania!!!')
    return render(request,'ankieta/detale.html',{'pytanie':pytanie})

def wyniki(request, pytanie_id):
    return HttpResponse(f'Oglądasz wyniki głosowaniania dla pytyania  { pytanie_id }')

def glosuj(request, pytanie_id):
    return HttpResponse(f'Głosujesz na pytanie  { pytanie_id }')