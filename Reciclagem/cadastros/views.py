from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic.list import ListView

from .models import Aluminio, UnidadeDeMedida, Papelao, Papel, Plastico, Usuario, Despesa

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

################# Creat ##########################


class UnidadeDeMedidaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
   # group_required - u"Administrador"
    model = UnidadeDeMedida
    fields = ['unidadedemedida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-unidadedemedida')


class PapelaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Papelao
    fields = ['quantidade', 'unidadedemedida', 'observacao', 'dt_criacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('home')
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-papelao')


class PapelCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Papel
    fields = ['quantidade', 'unidadedemedida', 'observacao', 'dt_criacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-papel')


class PlasticoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Plastico
    fields = ['quantidade', 'unidadedemedida', 'observacao', 'dt_criacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-plastico')


class AluminioCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Aluminio
    fields = ['quantidade', 'unidadedemedida', 'observacao', 'dt_criacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-aluminio')


class UsuarioCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Usuario
    fields = ['nome', 'email', 'cnpj', 'telefone', 'logradouro',
              'numero', 'bairro', 'complemento', 'cep', 'cidade', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-usuario')


class DespesaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Despesa
    fields = ['valor', 'dt_criacao', 'observacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-despesa')


####################### Upadate ################################

class UnidadeDeMedidaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = UnidadeDeMedida
    fields = ['unidadedemedida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-unidadedemedida')


class PapelaoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Papelao
    fields = ['quantidade', 'unidadedemedida', 'observacao', 'dt_criacao']
    template_name = 'cadastros/form.html'
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-papelao')


class PapelUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Papel
    fields = ['quantidade', 'unidadedemedida', 'observacao', 'dt_criacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-papel')


class PlasticoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Plastico
    fields = ['quantidade', 'unidadedemedida', 'observacao', 'dt_criacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-plastico')


class AluminioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Aluminio
    fields = ['quantidade', 'unidadedemedida', 'observacao', 'dt_criacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-aluminio')


class UsuarioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Usuario
    fields = ['nome', 'email', 'cnpj', 'telefone', 'logradouro',
              'numero', 'bairro', 'complemento', 'cep', 'cidade', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-usuario')


class DespesaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Despesa
    fields = ['valor', 'dt_criacao', 'observacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-despesa')


################################ Delete ################################

class UnidadeDeMedidaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = UnidadeDeMedida
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-unidadedemedida')


class PapelaoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Papelao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-papelao')


class PapelDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Papel
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-papel')


class PlasticoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Plastico
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-plastico')


class AluminioDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Aluminio
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-aluminio')


class UsuarioDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Usuario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-usuario')


class DespesaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Despesa
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-despesa')


################################ List ################################

class UnidadeDeMedidaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = UnidadeDeMedida
    template_name = 'cadastros/listas/unidadedemedida.html'


class PapelaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Papelao
    template_name = 'cadastros/listas/papelao.html'


class PapelList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Papel
    template_name = 'cadastros/listas/papel.html'


class PlasticoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Plastico
    template_name = 'cadastros/listas/plastico.html'


class AluminioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Aluminio
    template_name = 'cadastros/listas/aluminio.html'


class UsuarioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Usuario
    template_name = 'cadastros/listas/usuario.html'


class DespesaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Usuario
    template_name = 'cadastros/listas/despesa.html'
