from django.db import models


# Create your models here.
class Cliente(models.Model):
    SEX_CHOICES = (
        ('', 'Escolha uma opção',),
        ('F', 'Feminino',),
        ('M', 'Masculino',),
    )
    ESTADO_CIVIL_CHOICES = (
        ('', 'Escolha uma opção',),
        ('S', u'Solteiro'),
        ('C', u'Casado'),
        ('D', u'Divorciado'),
        ('V', u'Viúvo'),
    )
    nome = models.CharField(max_length=250,blank=False)
    cpf = models.CharField(max_length=15, blank=False, null=True)
    email = models.CharField(max_length=150, default='', blank=True)
    sexo = models.CharField(max_length=1,choices=SEX_CHOICES)
    telefone = models.CharField(max_length=18, blank=False)  # validators should be a list
    status_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL_CHOICES, verbose_name='Estado civil')
    endereco = models.CharField(max_length=250)
    data_nascimento = models.DateField()
    salario= models.CharField(max_length=20)
    idade = models.CharField(max_length=3)

def __str__(self):
    return self.nome