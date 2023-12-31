from django.contrib import admin
from .models import Pendencia, Historico

# Register your models here.
class PendenciaAdmin(admin.ModelAdmin):
    list_display = ('nome_pessoa', 'cpf', 'codigo_pa', 'status', 'data_de_criacao')

admin.site.register(Pendencia, PendenciaAdmin)

admin.site.register(Historico)