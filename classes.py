#!/usr/bin/python3

class Professor:
    def __init__(self, nome, UCs, atendimento):
        self.professor_nome = nome
        self.professor_UCs = UCs
        self.professor_atendimento = atendimento


class UC:
    def __init__(self, nome, tuc, professor):
        self.uc_nome = nome
        self.uc_tuc = tuc
        self.uc_professor = professor


class Aluno:
    def __init__(self, nome, UCs):
        self.aluno_nome = nome
        self.aluno_UCs = UCs


class Sala:
    def __init__(self, nome, tuc, lotacao, dist):
        self.sala_nome = nome
        self.sala_tuc = tuc
        self.sala_lotacao = lotacao
        self.sala_distancia = dist


class Grupo:
    def __init__(self, id, lotacao, UCs):
        self.grupo_id = id
        self.grupo_lotacao = lotacao
        self.grupo_UCs = UCs


class Bloco:
    def __init__(self, id, dia, hora):
        self.bloco_id = id
        self.bloco_dia = dia
        self.bloco_hora = hora

