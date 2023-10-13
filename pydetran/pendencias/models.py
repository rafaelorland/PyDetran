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

    def __str__(self):
        return self.nome_pessoa
