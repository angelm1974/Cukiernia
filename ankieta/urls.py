from django.urls import path

from . import views

urlpatterns =[
    path('',views.index, name='index'),
     # ex: /ankieta/5/detale
    path('detale/<int:pytanie_id>',views.detale, name='detale'),
    # ex: /ankieta/5/wyniki/
    path('<int:pytanie_id>/wyniki',views.wyniki, name='wyniki'),
    # ex: /ankieta/5/glosuj/
    path('<int:pytanie_id>/glosuj',views.glosuj, name='glosuj')
]