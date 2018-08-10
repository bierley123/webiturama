from django.contrib import admin

from pessoa.models import Funcionario


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', 'remuneracao']
    search_fields = ['nome']
