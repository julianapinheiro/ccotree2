from django.shortcuts import render
from .models import Disciplina

# Create your views here.

def matriz(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'grade/lista_disc.html', {'disciplinas': disciplinas})

