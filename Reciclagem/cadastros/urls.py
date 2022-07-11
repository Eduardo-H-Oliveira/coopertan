from django.urls import path
from django.views.generic.base import View
from .views import PapelaoCreate, UnidadeDeMedidaCreate, PapelCreate, PlasticoCreate, AluminioCreate, UsuarioCreate, DespesaCreate
from .views import PapelUpdate, UnidadeDeMedidaUpdate, PapelaoUpdate, PlasticoUpdate, AluminioUpdate, UsuarioUpdate, DespesaUpdate
from .views import PapelDelete, UnidadeDeMedidaDelete, PapelaoDelete, PlasticoDelete, AluminioDelete, UsuarioDelete, DespesaDelete
from .views import PapelList, UnidadeDeMedidaList, PapelaoList, PlasticoList, AluminioList, UsuarioList, DespesaList

urlpatterns = [
    path('cadastrar/unidadedemedida', UnidadeDeMedidaCreate.as_view(), name="cadastrar-unidadedemedida"),
    path('cadastrar/papel', PapelCreate.as_view(), name="cadastrar-papel"),
    path('cadastrar/papelao', PapelaoCreate.as_view(), name="cadastrar-papelao"),
    path('cadastrar/plastico', PlasticoCreate.as_view(), name="cadastrar-plastico"),
    path('cadastrar/aluminio', AluminioCreate.as_view(), name="cadastrar-aluminio"),
    path('cadastrar/usuario', UsuarioCreate.as_view(), name="cadastrar-usuario"),
    path('cadastrar/despesa', DespesaCreate.as_view(), name="cadastrar-despesa"),

    path('editar/unidadedemedida<int:pk>',
         UnidadeDeMedidaUpdate.as_view(), name='editar-unidadedemedida'),
    path('editar/papel/<int:pk>', PapelUpdate.as_view(), name='editar-papel'),
    path('editar/papelao/<int:pk>', PapelaoUpdate.as_view(), name='editar-papelao'),
    path('editar/plastico/<int:pk>', PlasticoUpdate.as_view(), name='editar-plastico'),
    path('editar/aluminio/<int:pk>', AluminioUpdate.as_view(), name='editar-aluminio'),
    path('editar/usuario/<int:pk>', UsuarioUpdate.as_view(), name='editar-usuario'),
    path('editar/despesa/<int:pk>', DespesaUpdate.as_view(), name='editar-despesa'),


    path('excluir/unidadedemedida<int:pk>',
         UnidadeDeMedidaDelete.as_view(), name='excluir-unidadedemedida'),
    path('excluir/papel/<int:pk>', PapelDelete.as_view(), name='excluir-papel'),
    path('excluir/papelao/<int:pk>', PapelaoDelete.as_view(), name='excluir-papelao'),
    path('excluir/plastico/<int:pk>', PlasticoDelete.as_view(), name='excluir-plastico'),
    path('excluir/aluminio/<int:pk>', AluminioDelete.as_view(), name='excluir-aluminio'),
    path('excluir/usuario/<int:pk>', UsuarioDelete.as_view(), name='excluir-usuario'),
    path('excluir/despesa/<int:pk>', DespesaDelete.as_view(), name='excluir-despesa'),

    path('listar/unidadedemedida', UnidadeDeMedidaList.as_view(), name="listar-unidadedemedida"),
    path('listar/papel', PapelList.as_view(), name="listar-papel"),
    path('listar/papelao', PapelaoList.as_view(), name="listar-papelao"),
    path('listar/plastico', PlasticoList.as_view(), name="listar-plastico"),
    path('listar/aluminio', AluminioList.as_view(), name="listar-aluminio"),
    path('listar/usuario', UsuarioList.as_view(), name="listar-usuario"),
    path('listar/despesa', DespesaList.as_view(), name="listar-despesa"),

]
