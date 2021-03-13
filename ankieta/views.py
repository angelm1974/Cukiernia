from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse


from .models import Pytanie, Wybor
# Create your views here.

def index(request):

    lista_pytan = Pytanie.objects.order_by('-data_publikacji')[:5]
    contex= {'lista_pytan' : lista_pytan,}
    return render(request,'ankieta/index.html',contex)

def detale(request, pytanie_id):
    try:
        pytanie = Pytanie.objects.get(pk = pytanie_id)
    except Pytanie.DoesNotExist:
        raise Http404('Nie ma takiego pytania!!!')
    return render(request,'ankieta/detale.html',{'pytanie':pytanie})

def wyniki(request, pytanie_id):
    pytanie = get_object_or_404(Pytanie,pk=pytanie_id)
    return render(request,'ankieta/wyniki.html',{'pytanie':pytanie})

def glosuj(request, pytanie_id):
    pytanie = get_object_or_404(Pytanie,pk=pytanie_id)
    try:
        wybrany=pytanie.wybor_set.get(pk=request.POST['wybor'])
    except (KeyError, Wybor.DoesNotExist):
        return render(request, 'ankieta/detale.html', {
            'pytanie':pytanie, 'error_message': "Nie wybrałeś pola wyboru!!!"
        })
    else:
        wybrany.glosy +=1
        wybrany.save()
        return HttpResponseRedirect(reverse('wyniki',args=(pytanie.id,)))
    
    