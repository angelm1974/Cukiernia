from django.db import models

# Create your models here.

class Pytanie(models.Model):
    tekst_pytania=models.CharField(max_length=300)
    data_publikacji=models.DateTimeField()
    
    def __str__(self):
        return self.tekst_pytania
    
    class Meta:
        verbose_name="Pytanie"
        verbose_name_plural="Pytania"

class Wybor(models.Model):
    pytanie = models.ForeignKey(Pytanie,on_delete=models.CASCADE)
    tekst_odpowiedzi=models.CharField(max_length=300)
    glosy=models.IntegerField(default=0)

    def __str__(self):
        return self.tekst_odpowiedzi
    
    class Meta:
        verbose_name="Wybór"
        verbose_name_plural="Wybory"