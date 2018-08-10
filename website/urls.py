from website.views import IndexTemplateView, FuncionarioListView, FuncionarioCreateView, \
    FuncionarioDeleteView, FuncionarioListViewCertidao, FuncionarioListViewExame, ExameUpdateView, ExameUpdateView, \
    ListCertidaoView, ListExameView

from django.urls import path

app_name = 'website'

urlpatterns = [
    # GET /
    path('', IndexTemplateView.as_view(), name="index"),

    # GET /funcionario/cadastrar
    path('funcionario/cadastrar', FuncionarioCreateView.as_view(), name="cadastra_funcionario"),

    # GET /funcionarios
    path('funcionarios',      FuncionarioListView.as_view(), name="lista_funcionarios"),
    path('funcionarios/<pk>',   FuncionarioListView.as_view(), name="lista_funcionarios"),

    # GET /funcionarios Certidao
    path('funcionario/<pk>', FuncionarioListView.as_view(), name="atualiza_funcionario"),
    path('funcionarios/certidao/', FuncionarioListViewCertidao.as_view(), name="lista_funcionarioscertidao"),
    path('funcionarios/certidao/<pk>', FuncionarioListViewCertidao.as_view(), name="lista_funcionarioscertidao"),

    # GET /funcionarios Exame
    path('funcionarios/exame/', FuncionarioListViewExame.as_view(), name="lista_funcionariosexame"),
    path('funcionarios/exame/<pk>', FuncionarioListViewExame.as_view(), name="lista_funcionariosexame"),

    # TESTE AQUI
    # path('funcionarios/<pk>',  ListCertidaoView.as_view(), name="lista_PDF"),

    # GET /funcionarios
    # path('funcionario',      FuncionarioListViewCertidao.as_view(), name="lista_protocolos"),
    # path('funcionario/<pk>', FuncionarioListViewCertidao.as_view(), name="lista_protocolos"),

    # GET/POST /funcionario/{pk}

    # path('', IndexTemplateView.as_view(), name="abrir_PDF"),

    # GET/POST /funcionarios/excluir/{pk}
    # path('funcionario/excluir/<pk>', FuncionarioDeleteView.as_view(), name="deleta_funcionario"),
]
