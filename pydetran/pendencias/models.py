from django.db import models
from django.core.exceptions import ValidationError
import re

def validate_cpf(value):
    if not re.match(r'^[0-9]{11}$', value):
        raise ValidationError('CPF inválido')

class Pendencia(models.Model):
    nome_pessoa = models.CharField(max_length=100, help_text='Nome da pessoa relacionada à pendência')
    cpf = models.CharField(max_length=11, validators=[validate_cpf], help_text='CPF da pessoa')
    codigo_pa = models.CharField(max_length=10, unique=True, help_text='Código único do processo')
    descricao = models.TextField(help_text='Descrição detalhada da pendência')
    status = models.BooleanField(default=False, help_text='Status da pendência (resolvida ou não)')
    data_de_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_pessoa

class Historico(models.Model):
    nome_user = models.CharField(max_length=100)
    nome_pendencia = models.CharField(max_length=100)
    ACOES = [
        ("I", "Inseriu Pendência"),
        ("S", "Troca de Status"),
        ("E", "Excluiu a Pendência"),
    ]
    acao = models.CharField(max_length=1, choices=ACOES)
    data_de_execucao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome_user} realizou a ação de {self.get_acao_display()} em "{self.data_de_execucao}"'

    @classmethod
    def registrar_acao(cls, nome_user, nome_pendencia, acao):
        historico = cls(
            nome_user=nome_user,
            nome_pendencia=nome_pendencia,
            acao=acao
        )
        historico.save()