#!/usr/bin/python3
from classes import *


def criarAlunos():
    a1 = Aluno(nome='jose', UCs=['algebra', 'calculo'])
    a2 = Aluno(nome='carlos', UCs=['ingles', 'espanhol'])
    alunos = [a1, a2]
    return alunos


def criarUCs():
    u1 = UC(nome='tpl', tuc=2, professor=['bastos'])
    u2 = UC(nome='dem', tuc=0, professor=['bastos', 'rui'])
    u3 = UC(nome='estruturas', tuc=0, professor=['balaco'])
    u4 = UC(nome='desenho', tuc=0, professor=['jalex', 'rui'])
    u5 = UC(nome='ipm', tuc=0, professor=['balaco', 'ramos'])
    u6 = UC(nome='solidos', tuc=0, professor=['robert', 'ricardo'])
    u7 = UC(nome='iem', tuc=0, professor=['robert', 'gil'])
    u8 = UC(nome='spt', tuc=1, professor=['ricardo'])
    u9 = UC(nome='onle', tuc=0, professor=['gil', 'jalex'])
    u10 = UC(nome='cfac', tuc=1, professor=['ramos'])

    UCs = [u1, u2, u3, u4, u5, u6, u7, u8, u9, u10]
    return UCs


def criarProfessores():
    p1 = Professor(nome='bastos', UCs=['tpl', 'dem'], atendimento=2)
    p2 = Professor(nome='rui', UCs=['desenho', 'dem'], atendimento=5)
    p3 = Professor(nome='balaco', UCs=['estruturas', 'ipm'], atendimento=12)
    p4 = Professor(nome='robert', UCs=['solidos', 'iem'], atendimento=7)
    p5 = Professor(nome='ricardo', UCs=['solidos', 'spt'], atendimento=15)
    p6 = Professor(nome='gil', UCs=['iem', 'onle'], atendimento=10)
    p7 = Professor(nome='jalex', UCs=['onle', 'desenho'], atendimento=9)
    p8 = Professor(nome='ramos', UCs=['ipm', 'cfac'], atendimento=19)

    professores = [p1, p2, p3, p4, p5, p6, p7, p8]
    return professores


def criarBlocos():
    b1 = Bloco(id=0, dia='Segunda', hora='9-11')
    b2 = Bloco(id=1, dia='Segunda', hora='11-13')
    b3 = Bloco(id=2, dia='Segunda', hora='13-14')
    b4 = Bloco(id=3, dia='Segunda', hora='14-16')
    b5 = Bloco(id=4, dia='Segunda', hora='16-18')

    b6 = Bloco(id=5, dia='Terca', hora='9-11')
    b7 = Bloco(id=6, dia='Terca', hora='11-13')
    b8 = Bloco(id=7, dia='Terca', hora='13-14')
    b9 = Bloco(id=8, dia='Terca', hora='14-16')
    b10 = Bloco(id=9, dia='Terca', hora='16-18')

    b11 = Bloco(id=10, dia='Quarta', hora='9-11')
    b12 = Bloco(id=11, dia='Quarta', hora='11-13')
    b13 = Bloco(id=12, dia='Quarta', hora='13-14')
    b14 = Bloco(id=13, dia='Quarta', hora='14-16')
    b15 = Bloco(id=14, dia='Quarta', hora='16-18')

    b16 = Bloco(id=15, dia='Quinta', hora='9-11')
    b17 = Bloco(id=16, dia='Quinta', hora='11-13')
    b18 = Bloco(id=17, dia='Quinta', hora='13-14')
    b19 = Bloco(id=18, dia='Quinta', hora='14-16')
    b20 = Bloco(id=19, dia='Quinta', hora='16-18')

    b21 = Bloco(id=20, dia='Sexta', hora='9-11')
    b22 = Bloco(id=21, dia='Sexta', hora='11-13')
    b23 = Bloco(id=22, dia='Sexta', hora='13-14')
    b24 = Bloco(id=23, dia='Sexta', hora='14-16')
    b25 = Bloco(id=24, dia='Sexta', hora='16-18')

    blocos = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23,
              b24, b25]

    return blocos


def criarSalas():
    s1 = Sala(nome=1, tuc=0, lotacao=40, dist=15)
    s2 = Sala(nome=2, tuc=0, lotacao=40, dist=20)
    s3 = Sala(nome=3, tuc=0, lotacao=30, dist=10)
    s4 = Sala(nome=4, tuc=2, lotacao=35, dist=30)
    s5 = Sala(nome=5, tuc=1, lotacao=35, dist=30)

    salas = [s1, s2, s3, s4, s5]
    return salas


def criarGrupos():
    g1 = Grupo(id=0, lotacao=25, UCs=['tpl', 'dem', 'estruturas', 'ipm', 'solidos'])
    g2 = Grupo(id=1, lotacao=35, UCs=['iem', 'spt', 'onle', 'desenho', 'cfac'])
    g3 = Grupo(id=2, lotacao=30, UCs=['tpl', 'estruturas', 'solidos', 'spt', 'desenho'])

    grupos = [g1, g2, g3]
    return grupos
