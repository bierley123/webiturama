import requests, bs4, os

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, DetailView
from pessoa.models import Funcionario, Exame
from website.forms import InsereFuncionarioForm
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.conf import settings


# PÁGINA PRINCIPAL
# ----------------------------------------------


# AQUI DEFINO QUAL NUMERO VOU FILTRAR
def pegarNroOrdem():
    path = os.path.split(os.path.abspath(__file__))[0]
    path = path + "\\atual.txt"
    with open(path) as arquivo:
        tudo = arquivo.read()
    return tudo


NroOrdem = 123001
NroOrdemCertidao = 123000
NroOrdemExame = 123000


def home(request):
    return render(request, "website/index.html", {})


class IndexTemplateView(TemplateView):
    template_name = "website/index.html"


# LISTA DE FUNCIONÁRIOS
# ----------------------------------------------
class ListExameView(ListView):
    template_name = "website/listaExame.html"
    model = Funcionario
    context_object_name = "funcionarios"

    # queryset = Funcionario.objetos.filter(tempo_de_servico=NroOrdemExame)


class ListCertidaoView(ListView):
    template_name = "website/listaCertidao.html"
    model = Funcionario
    context_object_name = "funcionarios"


# class FuncionarioDetailView(TemplateView):
#     model = Funcionario
#
#     def get(self, request, *args, **kwargs):
#         return render()


class FuncionarioListView(TemplateView):
    template_name = "website/lista.html"
    model = Funcionario

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request):
        protocolo = request.POST.get('protocolo', 0)
        if protocolo:
            protocolo = int(protocolo)
            funcionarios = Funcionario.objects.filter(tempo_de_servico=protocolo)
            return render(request, self.template_name, {'funcionarios': funcionarios, 'url_ftp': settings.URL_FTP})
        return render(request, self.template_name)


class FuncionarioListViewCertidao(ListView):
    template_name = "website/listaCertidao.html"
    model = Funcionario
    context_object_name = "funcionarios"

    queryset = Funcionario.objects.filter(tempo_de_servico=NroOrdemCertidao)


class FuncionarioListViewExame(ListView):
    template_name = "website/listaExame.html"
    # model = Exame
    # context_object_name = "exames"
    model = Funcionario
    context_object_name = "funcionarios"

    queryset = Funcionario.objects.filter(tempo_de_servico=NroOrdemExame)


# CADASTRAMENTO DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioCreateView(CreateView):
    template_name = "website/cria.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("website:lista_funcionarios")


# ATUALIZAÇÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioUpdateView(UpdateView):
    # template_name = "atualiza.html"
    template_name = "website/atualiza.html"
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'

    def get_object(self, queryset=None):
        funcionario = None

        # Os campos {pk} e {slug} estão presentes em self.kwargs 
        id = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)

        if id is not None:
            # Busca o funcionario apartir do id 
            funcionario = Funcionario.objects.filter(id=id).first()
        elif slug is not None:
            # Pega o campo slug do Model 
            campo_slug = self.get_slug_field()
            # Busca o funcionario apartir do slug 
            funcionario = Funcionario.objects.filter(**{campo_slug: slug}).first()

        # Retorna o objeto encontrado 
        return funcionario


class ExameUpdateView(UpdateView):
    template_name = "website/atualizaexame.html"
    model = Exame
    fields = '__all__'
    # context_object_name = 'exame'
    success_url = reverse_lazy("website:lista_exame")


# EXCLUSÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy("website:lista_funcionarios")
