from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here. Register them in admin.py!

class Disciplina(models.Model):
    id = models.CharField(max_length=7, primary_key=True)
    nome = models.CharField(max_length=200)
    fase = models.CharField(default=1, max_length=1)
    horas = models.PositiveSmallIntegerField(default=4,
        validators=[
            MaxValueValidator(30),
            MinValueValidator(1)
        ])
    # Requisito é uma relação não simétrica 
    # blank=True permite ser vazio
    requisitos = models.ManyToManyField("self", symmetrical=False,
        blank=True)

    def __str__(self):
        return self.id

class DisciplinaView(models.Model):
    id = models.OneToOneField('Disciplina', on_delete=models.CASCADE, 
        primary_key=True)
    posX = models.PositiveIntegerField(default=0)
    posY = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=8, default="#000000")

    def __str__(self):
        return self.id.id

