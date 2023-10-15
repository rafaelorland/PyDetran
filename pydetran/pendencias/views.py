from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.db.models import Q
from .models import Pendencia
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
         
         return render(request, 'components/sucesso.html', {'message': 'Pendência  com sucesso.'})

      except ValidationError as e:
         return render(request, 'components/erro.html', {'error': str(e)})
      
      except IntegrityError as e:
         return render(request, 'components/erro.html', {'error': 'Erro de integridade de dados.'})
      
      except Exception as e:
         return render(request, 'components/erro.html', {'error': 'Erro interno no servidor.'})

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
   if request.method == 'POST':
      pendencia.status = not pendencia.status
      pendencia.save()
      return render(request, 'page/mostrar_pendencia.html', {'pendencia': pendencia})

   return render(request, 'page/mostrar_pendencia.html', {'pendencia': pendencia})