from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Pendencia
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
import re

def homePagePendencias(request):
   return render(request, 'homepagependencias.html')

def inserirpendencia(request):
   if request.method == 'POST':
      nome_pessoa = request.POST.get('nome_pessoa')
      cpf = request.POST.get('cpf')
      codigo_pa = request.POST.get('codigo_pa')
      descricao = request.POST.get('descricao')
      status = request.POST.get('status', False)

      try:
       
         if Pendencia.objects.filter(cpf=cpf).exists():
            return render(request, 'erro.html', {'error': 'Já existe uma pendência com este CPF no sistema.'})
                  
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
         
         return render(request, 'sucesso.html', {'message': 'Pendência  com sucesso.'})

      except ValidationError as e:
         return render(request, 'erro.html', {'error': str(e)})
      except IntegrityError as e:
         return render(request, 'erro.html', {'error': 'Erro de integridade de dados.'})
      except Exception as e:
         return render(request, 'erro.html', {'error': 'Erro interno no servidor.'})

   return render(request, 'inserirpendencia.html')