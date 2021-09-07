from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Cliente(models.Model):
    SEX_CHOICES = (
        ('F', 'Feminino',),
        ('M', 'Masculino',),
    )
    ESTADO_CIVIL_CHOICES = (
        ('S', u'Solteiro'),
        ('C', u'Casado'),
        ('D', u'Divorciado'),
        ('V', u'Viúvo'),
    )
    nome = models.CharField(max_length=250,blank=False)
    cpf = models.CharField(max_length=11, blank=False, null=True)
    email = models.CharField(max_length=150, default='', blank=True)
    sexo = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
    )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="O número de telefone deve ser inserido no formato: '+999999999'. Up to 15 digits allowed.")
    telefone = models.CharField(validators=[phone_regex], max_length=18, blank=False)  # validators should be a list
    endereco = models.CharField(max_length=250)
    data_nascimento = models.DateField()
    status_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL_CHOICES, verbose_name='Estado civil')
    salario= models.CharField(max_length=20)


def __str__(self):
    return self.nome