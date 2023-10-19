from django.shortcuts import render, get_object_or_404, HttpResponsePermanentRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.db.utils import IntegrityError
from .models import Pendencia, Historico
from django.contrib import messages 
from datetime import datetime
from datetime import date
import re

@login_required
def homePagePendencias(request):
   context = {
      'processosTotais': Pendencia.objects.count(),
      'processosPendentes': Pendencia.objects.filter(status = False).count(),
      'processosResolvidos': Pendencia.objects.filter(status = True).count(),
   }
   return render(request, 'homepagependencias.html', context)

@login_required
def inserirpendencia(request):
   if request.method == 'POST':
      nome_pessoa = request.POST.get('nome_pessoa').upper()
      cpf = request.POST.get('cpf')
      codigo_pa = request.POST.get('codigo_pa')
      descricao = request.POST.get('descricao')
      status = request.POST.get('status', False)

      try:
       
         if Pendencia.objects.filter(cpf=cpf).exists():
            return render(request, 'components/erro.html', {'error': 'Já existe uma pendência com este CPF no sistema.'})
                  
         def cpf_is_valid(cpf):
            cpf = re.sub(r'\D', '', cpf)
            if len(cpf) != 11:
               return False

            if cpf == cpf[0] * 11:
               return False

            return True
         
         if not cpf_is_valid(cpf):
               raise ValidationError('CPF inválido')

         pendencia = Pendencia(
               nome_pessoa=nome_pessoa,
               cpf=cpf,
               codigo_pa=codigo_pa,
               descricao=descricao,
               status=status
         )
                 
         pendencia.save()
               
         Historico.registrar_acao(request.user.username, nome_pessoa, cpf, 'I')
               
         return render(request, 'components/sucesso.html', {'message': 'Pendência  com sucesso.'})

      except ValidationError as e:
         return render(request, 'components/erro.html', {'error': str(e)})
      
      except IntegrityError as e:
         return render(request, 'components/erro.html', {'error': 'Erro de integridade de dados.'})

   return render(request, 'page/inserirpendencia.html')

@login_required
def consultarpendencia(request):
   resultados = None

   if request.method == 'POST':
      search_type = request.POST.get('search_type')
      search_query = request.POST.get('search_query')

      consulta = Pendencia.objects.all()
         
      if search_type == 'nome':
         consulta = consulta.filter(nome_pessoa__icontains = search_query)
      if search_type == 'cpf':
         consulta = consulta.filter(cpf__icontains = search_query)
      if search_type == 'renach':
         consulta = consulta.filter(codigo_pa__icontains = search_query)

      resultados = consulta

   return render(request, 'page/consultapendencia.html', {'resultados': resultados})

@login_required
def mostrar_pendencia(request, pendencia_id):
   pendencia = get_object_or_404(Pendencia, id=pendencia_id)
   return render(request, 'page/mostrar_pendencia.html', {'pendencia': pendencia})

@login_required
def excluir_pendencia(request, pendencia_id):
   pendencia = get_object_or_404(Pendencia, id=pendencia_id)
   if request.method == 'POST':
      password = request.POST.get('password')
      user = authenticate(request, username=request.user.username, password=password)
      if user is not None:
         excluirpendencia = Pendencia.objects.get(pk = pendencia_id)
         excluirpendencia.delete()
         Historico.registrar_acao(request.user.username, pendencia.nome_pessoa, pendencia.cpf, 'E')
         return render(request, 'components/sucessoexcluir.html', {'message': 'Pendência excluída com sucesso. Ação concluída!'})
      else:
         messages.error(request, 'Senha incorreta!!!')
   
   return render(request, 'components/excluirpendencia.html', {'pendencia': pendencia})

@login_required
def trocar_status(request, pendencia_id):
   pendencia = get_object_or_404(Pendencia, id=pendencia_id)
   if request.method == 'POST':
      password = request.POST.get('password')
      user = authenticate(request, username=request.user.username, password=password)
      if user is not None:
         pendencia.status = not pendencia.status
         pendencia.save()
         Historico.registrar_acao(request.user.username, pendencia.nome_pessoa, pendencia.cpf, 'S')
         return HttpResponsePermanentRedirect(f'/pendencias/pendencia/{pendencia_id}/')
      else:
         messages.error(request, 'Senha incorreta!!!')
   
   return render(request, 'components/trocarstatus.html', {'pendencia': pendencia})

@login_required
def historico(request):
    if request.method == 'POST':
        dia = request.POST.get('dia')
        mes = request.POST.get('mes')
        ano = request.POST.get('ano')

        try:
            dia = int(dia)
            mes = int(mes)
            ano = int(ano)

            if 1 <= mes <= 12 and 1 <= dia <= 31:
                data_pesquisa = datetime(ano, mes, dia)
                historicos = Historico.objects.filter(data_de_execucao__date=data_pesquisa).order_by('-data_de_execucao')
            else:
                return render(request, 'page/historico.html', {'error': 'Data inválida'})
        except (ValueError, TypeError):
            return render(request, 'page/historico.html', {'error': 'Data inválida'})
    else:
        data_atual = datetime.now().date()
        historicos = Historico.objects.filter(data_de_execucao__date=data_atual).order_by('-data_de_execucao')

    return render(request, 'page/historico.html', {'historicos': historicos})
