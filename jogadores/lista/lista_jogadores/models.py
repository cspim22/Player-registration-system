from django.db import models

# Create your models here.

#Cria um modelo, para banco de dados sem escrever em sql


class Melhores_Do_Brasil(models.Model):
    nome = models.TextField()
    time_principal = models.TextField()
    gols_na_carreira = models.FloatField()
    principal_titulo = models.TextField()
    ainda_joga = models.BooleanField()
    extras = models.TextField() 

class Melhores_Da_Historia(models.Model):
    nome = models.TextField()
    time_principal = models.TextField(default= 250)
    gols_na_carreira = models.FloatField()
    principal_titulo = models.TextField(default=250)
    ainda_joga = models.BooleanField(default= True)
    info = models.TextField(default= 250)

    
    