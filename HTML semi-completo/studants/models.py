from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Studant(models.Model):
    COURSES = (
        ('Ciência da Computação', 'Ciência da Computação'),
        ('Sistemas de Informação', 'Sitemas de Informação'),
        ('Física', 'Física'),
        ('Enfermagem', 'Enfermagem'),
        ('Engenharia Civil', 'Engenharia Civil'),
        ('Arquitetura', 'Arquitetura'),
        ('Química', 'Química'),
    )
    name = models.CharField('Nome',max_length=30)
    birth_date = models.DateField('Data  de Nasimento')
    city = models.CharField('Cidade',max_length=50,default="Viçosa do Ceará")
    phone = models.CharField('Telefone',max_length=11)
    cpf = models.CharField('CPF',max_length=11)
    course = models.CharField('Curso',max_length=50, choices=COURSES)
    email = models.EmailField('E-mail')
    
    