from django.shortcuts import render
from .models import DisciplinaView

# Create your views here.

def matriz(request):
    disciplinas = DisciplinaView.objects.all()
    return render(request, 'grade/lista_disc.html', {'disciplinas': disciplinas})

