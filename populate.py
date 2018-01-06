'''
    Módulo/script para preencher o banco de dados com as disciplinas 
    obrigatórias de CCO.
    A classe Disc foi necessária porque o dict currículo foi reusado de outro
    projeto. (github.com/gabriellmuller/grafoscurriculo)
    
    TO-DO: link da ementa.
'''

import os, sys, django, json
from collections import namedtuple

class Disc():
    def __init__(self, nome, horas, fase, requisitos):
        self.nome = nome
        self.horas = horas
        self.fase = fase
        self.requisitos = requisitos

def populate():
    # Por algum motivo (?) não criava INE5404 no loop
    add_disc(id="INE5402", nome="Programação Orientada a Objetos I",
        fase=1, horas=6, requisitos={})
    add_disc(id="INE5404", nome="Programação Orientada a Objetos II",
        fase=2, horas=6, requisitos={"INE5402"})

    for disciplina in curriculo:
        if disciplina is not "INE5404":
            add_disc(id=disciplina, nome=curriculo[disciplina].nome, 
                fase=curriculo[disciplina].fase, 
                horas=curriculo[disciplina].horas, 
                requisitos=curriculo[disciplina].requisitos)

def add_disc(id, nome, fase, horas, requisitos):
    print("----------------------------")

    d = Disciplina.objects.create(id=id, 
        nome=nome, fase=fase, horas=horas)
    print(d.id)
    for req in requisitos:
        print("req ", req)
        d.requisitos.add((Disciplina.objects.get(id=req)))
    d.save()

curriculo = {
    #"INE5402": Disc("Programação Orientada a Objetos I", 6, 1, {}),
    #"INE5404": Disc("Programação Orientada a Objetos II", 6, 2, {
    #    "INE5402"
    #}),
    "INE5403": Disc("Matemática Discreta para Computação", 6, 1, {}),
    "MTM3100": Disc("Cálculo 1", 4, 1, {}),
    "EEL5105": Disc("Circuitos e Técnicas Digitais", 5, 1, {}),
    "INE5401": Disc("Introdução à Computação", 2, 1, {}),
    "INE5405": Disc("Probabilidade e Estatística", 5, 2, {
        "MTM3100"
    }),
    "MTM3102": Disc("Cálculo 2", 4, 2, {
        "MTM3100"
    }),
    "MTM5512": Disc("Geometria Analítica", 4, 2, {}),
    "INE5406": Disc("Sistemas Digitais", 5, 2, {
        "EEL5105"
    }),
    "INE5407": Disc("Ciência, Tecnologia e Sociedade", 3, 2, {}),
    "INE5408": Disc("Estruturas de Dados", 6, 3, {
        "INE5404"
    }),
    "INE5410": Disc("Programação Concorrente", 4, 3, {
        "INE5404"
    }),
    "INE5409": Disc("Cálculo Numérico para Computação", 4, 3, {
        "MTM3102", "MTM5512"
    }),
    "MTM5245": Disc("Álgebra Linear", 4, 3, {
        "MTM5512"
    }),
    "INE5411": Disc("Organização de Computadores", 6, 3, {
        "INE5406"
    }),
    "INE5417": Disc("Engenharia de Software I", 5, 4, {
        "INE5408"
    }),
    "INE5413": Disc("Grafos", 4, 4, {
        "INE5408", "INE5403"
    }),
    "INE5415": Disc("Teoria da Computação", 4, 4, {
        "INE5408", "INE5403"
    }),
    "INE5416": Disc("Paradigmas de Programação", 5, 4, {
        "INE5408"
    }),
    "INE5412": Disc("Sistemas Operacionais I", 4, 4, {
        "INE5410", "INE5411"
    }),
    "INE5414": Disc("Redes de Computadores I", 4, 4, {
        "INE5404"
    }),
    "INE5419": Disc("Engenharia de Software II", 4, 5, {
        "INE5417"
    }),
    "INE5423": Disc("Banco de Dados I", 4, 5, {
        "INE5408"
    }),
    "INE5421": Disc("Linguagens Formais e Compiladores", 4, 5, {
        "INE5415"
    }),
    "INE5420": Disc("Computação Gráfica", 4, 5, {
        "INE5408", "MTM3102", "MTM5245"
    }),
    "INE5418": Disc("Computação Distribuída", 4, 5, {
        "INE5412", "INE5414"
    }),
    "INE5422": Disc("Redes de Computadores II", 4, 5, {
        "INE5414"
    }),
    "INE5453": Disc("Introdução ao TCC", 1, 6, {
        "INE5417"
    }),
    "INE5427": Disc("Planejamento e Gestão de Projetos", 4, 6, {
        "INE5417"
    }),
    "INE5426": Disc("Construção de Compiladores", 4, 6, {
        "INE5421"
    }),
    "INE5425": Disc("Modelagem e Simulação", 4, 6, {
        "INE5405"
    }),
    "INE5430": Disc("Inteligência Artificial", 4, 6, {
        "INE5405", "INE5413", "INE5416"
    }),
    "INE5424": Disc("Sistemas Operacionais II", 4, 6, {
        "INE5412"
    }),
    "INE5433": Disc("Trabalho de Conclusão de Curso I (TCC)", 6, 7, {
        "INE5453", "INE5427"
    }),
    "INE5432": Disc("Banco de Dados II", 4, 7, {
        "INE5423"
    }),
    "INE5429": Disc("Segurança em Computação", 4, 7, {
        "INE5403", "INE5414"
    }),
    "INE5431": Disc("Sistemas Multimídia", 4, 7, {
        "INE5414"
    }),
    "INE5428": Disc("Informática e Sociedade", 4, 7, {
        "INE5407"
    }),
    "INE5434": Disc("Trabalho de Conclusão de Curso II (TCC)", 9, 8, {
        "INE5433"
    })
}

if __name__ == '__main__':
    print ("Starting Grade population script...")
    sys.path.append('PATH_TO_APP/')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    django.setup()
    from grade.models import Disciplina
    Disciplina.objects.all().delete()
    populate()