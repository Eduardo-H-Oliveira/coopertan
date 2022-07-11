from django.db import models
from django.db.models.fields import CharField


class UnidadeDeMedida(models.Model):
    unidadedemedida = CharField(
        max_length=30, verbose_name="Unidade De Medida")

    def __str__(self) -> str:
        return self.unidadedemedida


class Papelao(models.Model):
    quantidade = models.IntegerField(max_length=10)
    unidadedemedida = models.ForeignKey(
        UnidadeDeMedida, on_delete=models.PROTECT)
    dt_criacao = models.DateField(auto_now=False)
    observacao = models.CharField(max_length=256, verbose_name="Observações")

    def __str__(self) -> str:
        return "{} {}".format(self.quantidade, self.unidadedemedida)


class Papel(models.Model):
    quantidade = models.IntegerField(max_length=10)
    unidadedemedida = models.ForeignKey(
        UnidadeDeMedida, on_delete=models.PROTECT)
    dt_criacao = models.DateField(auto_now=False)
    observacao = models.CharField(max_length=256, verbose_name="Observações")

    def __str__(self) -> str:
        return "{} {}".format(self.quantidade, self.unidadedemedida)


class Plastico(models.Model):
    quantidade = models.IntegerField(max_length=10)
    unidadedemedida = models.ForeignKey(
        UnidadeDeMedida, on_delete=models.PROTECT)
    dt_criacao = models.DateField(auto_now=False)
    observacao = models.CharField(max_length=256, verbose_name="Observações")

    def __str__(self) -> str:
        return "{} {}".format(self.quantidade, self.unidadedemedida)


class Aluminio(models.Model):
    quantidade = models.IntegerField(max_length=10)
    unidadedemedida = models.ForeignKey(
        UnidadeDeMedida, on_delete=models.PROTECT)
    dt_criacao = models.DateField(auto_now=False)
    observacao = models.CharField(max_length=256, verbose_name="Observações")

    def __str__(self) -> str:
        return "{} {}".format(self.quantidade, self.unidadedemedida)


class Usuario(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome Empresa")
    email = models.EmailField(max_length=255)
    cnpj = models.IntegerField(max_length=15)
    telefone = models.IntegerField(max_length=15)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=9)
    bairro = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255)
    cep = models.IntegerField(max_length=15)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=50)



class Despesa(models.Model):
    valor = models.FloatField(max_length=9)
    dt_criacao = models.DateField(auto_now=False)
    observacao = models.CharField(max_length=256, verbose_name="Observações")
    
