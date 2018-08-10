from django.db import models
from django import forms
from django.http import HttpResponseRedirect

'''
from website.RetornarNumero import *
'''

''''
try:
    variavel = int(RetornarNumero())
except:
    variavel = int(0)

class NumeroProtocolo(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(tempo_de_servico=variavel)
'''


class Funcionario(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    sobrenome = models.CharField(max_length=255, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    tempo_de_servico = models.IntegerField(default=0, null=False, blank=False)

    remuneracao = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return '%s %s' % (self.nome, self.sobrenome)

    class Meta:
        # db_table = 'nome_tabela'
        verbose_name = 'funcionario'
        verbose_name_plural = 'funcionarios'


class Exame(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    tempo_de_servico = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    remuneracao = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )
