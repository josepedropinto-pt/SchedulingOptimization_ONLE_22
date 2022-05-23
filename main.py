#!/usr/bin/python3
import random as rnd
import sys
import numpy as np
import pandas as pd
import prettytable
import math

from matplotlib import pyplot as plt
import time
from mpl_toolkits.mplot3d import Axes3D

POPULATION_SIZE = 50
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 10
MUTATION_RATE = 0.1
start_time = time.time()


# sys.stdout = open("test.txt", "w")


class Aula:

    def __init__(self, id, grupo, uc):
        self.aula_id = id
        self.aula_grupo = grupo
        self.aula_uc = uc
        self._professor = None
        self._bloco = None
        self._sala = None

    def get_id(self):
        return self.aula_id

    def get_grupo(self):
        return self.aula_grupo

    def get_uc(self):
        return self.aula_uc

    def get_professor(self):
        return self._professor

    def get_bloco(self):
        return self._bloco

    def get_sala(self):
        return self._sala

    def set_professor(self, professor):
        self._professor = professor

    def set_bloco(self, bloco):
        self._bloco = bloco

    def set_sala(self, sala):
        self._sala = sala

    def __str__(self) -> str:
        return str(self.get_grupo().get_nome()) + ',' + str(self.get_uc().get_id()) + ',' + \
               str(self.get_sala().get_nome()) + ',' + str(self.get_professor().get_nome()) + ',' + str(
            self.get_bloco().get_id())


class Grupo:
    def __init__(self, id, lotacao, UCs):
        self.grupo_id = id
        self.grupo_lotacao = lotacao
        self.grupo_UCs = UCs

    def get_nome(self):
        return self.grupo_id

    def get_ucs(self):
        return self.grupo_UCs

    def get_grupo_lotacao(self):
        return self.grupo_lotacao


class UC:

    def __init__(self, id, nome, professor, tuc):
        self._id = id
        self._nome = nome
        self._professor = professor
        self._tuc = tuc

    def get_id(self):
        return self._id

    def get_nome(self):
        return self._nome

    def get_tuc(self):
        return self._tuc

    def get_professor(self):
        return self._professor

    def __str__(self):
        return self._nome


class Professor:

    def __init__(self, nome, atendimento):
        self._nome = nome
        self._atendimento = atendimento

    def get_nome(self):
        return self._nome

    def get_atendimento(self):
        return self._atendimento

    def __str__(self):
        return self._nome


class Sala:

    def __init__(self, nome, tuc, lotacao, dist):
        self._nome = nome
        self._tuc = tuc
        self._lotacao = lotacao
        self._distancia = dist

    def get_nome(self):
        return self._nome

    def get_tuc(self):
        return self._tuc

    def get_lotacao(self):
        return self._lotacao

    def get_distancia(self):
        return self._distancia


class Bloco:

    def __init__(self, id, hora):
        self._id = id
        self._hora = hora

    def get_id(self):
        return self._id

    def get_hora(self):
        return self._hora


class Data:
    Salas = [['S1', 0, 40, 15], ['S2', 0, 40, 20],
             ['S3', 0, 30, 10], ['S4', 2, 35, 32],
             ['S5', 1, 35, 30], ['S6', 1, 50, 35],
             ['S7', 2, 60, 50], ['S8', 0, 25, 10],
             ['S9', 0, 50, 100]]

    Blocos = [['B0', 'Seg 09:00 - 11:00'],
              ['B1', 'Seg 11:00 - 13:00'],
              ['B2', 'Seg 14:00 - 16:00'],
              ['B3', 'Seg 16:00 - 18:00'],
              ['B4', 'Ter 09:00 - 11:00'],
              ['B5', 'Ter 11:00 - 13:00'],
              ['B6', 'Ter 14:00 - 16:00'],
              ['B7', 'Ter 16:00 - 18:00'],
              ['B8', 'Qua 09:00 - 11:00'],
              ['B9', 'Qua 11:00 - 13:00'],
              ['B10', 'Qua 14:00 - 16:00'],
              ['B11', 'Qua 16:00 - 18:00'],
              ['B12', 'Qui 09:00 - 11:00'],
              ['B13', 'Qui 11:00 - 13:00'],
              ['B14', 'Qui 14:00 - 16:00'],
              ['B15', 'Qui 16:00 - 18:00'],
              ['B16', 'Sex 09:00 - 11:00'],
              ['B17', 'Sex 11:00 - 13:00'],
              ['B18', 'Sex 14:00 - 16:00'],
              ['B19', 'Sex 16:00 - 18:00']]

    Professores = [['bastos', 2],
                   ['rui', 5],
                   ['balaco', 12],
                   ['robert', 7],
                   ['ricardo', 13],
                   ['gil', 10],
                   ['jalex', 9],
                   ['ramos', 19],
                   ['rosario', 14],
                   ['festas', 3],
                   ['vitor', 6],
                   ['riem', 9],
                   ['jps', 8],
                   ['cruz', 20],
                   ['semnome', 17],
                   ['descalco', 4]]

    def __init__(self):
        self._salas = []
        self._blocos = []
        self._professores = []

        for i in range(len(self.Salas)):
            self._salas.append(Sala(self.Salas[i][0], self.Salas[i][1], self.Salas[i][2], self.Salas[i][3]))

        for i in range(len(self.Blocos)):
            self._blocos.append(Bloco(self.Blocos[i][0], self.Blocos[i][1]))

        for i in range(len(self.Professores)):
            self._professores.append(Professor(self.Professores[i][0], self.Professores[i][1]))

        unidade_curricular1 = UC("uc1", "tpl", [self._professores[0]], 2)
        unidade_curricular2 = UC("uc2", "dem", [self._professores[0], self._professores[1]], 0)
        unidade_curricular3 = UC("uc3", "estruturas", [self._professores[2]], 0)
        unidade_curricular4 = UC("uc4", "desenho", [self._professores[1], self._professores[6]], 0)
        unidade_curricular5 = UC("uc5", "ipm", [self._professores[2], self._professores[7]], 0)
        unidade_curricular6 = UC("uc6", "solidos", [self._professores[3], self._professores[4]], 0)
        unidade_curricular7 = UC("uc7", "iem", [self._professores[3], self._professores[5]], 0)
        unidade_curricular8 = UC("uc8", "spt", [self._professores[4]], 1)
        unidade_curricular9 = UC("uc9", "onle", [self._professores[5], self._professores[6]], 0)
        unidade_curricular10 = UC("uc10", "cfac", [self._professores[7]], 1)
        unidade_curricular11 = UC("uc11", "emag", [self._professores[8]], 1)
        unidade_curricular12 = UC("uc12", "sistemas", [self._professores[2]], 0)
        unidade_curricular13 = UC("uc13", "tecmec", [self._professores[9]], 2)
        unidade_curricular14 = UC("uc14", "seminarios", [self._professores[10], self._professores[6]], 0)
        unidade_curricular15 = UC("uc15", "visao", [self._professores[11]], 0)
        unidade_curricular16 = UC("uc16", "automacao1", [self._professores[12]], 0)
        unidade_curricular17 = UC("uc17", "mecaplicada", [self._professores[13], self._professores[4]], 0)
        unidade_curricular18 = UC("uc18", "psr", [self._professores[11]], 0)
        unidade_curricular19 = UC("uc19", "algebra", [self._professores[14]], 0)
        unidade_curricular20 = UC("uc20", "calculo", [self._professores[15]], 0)
        unidade_curricular21 = UC("uc21", "automacao2", [self._professores[13]], 1)
        unidade_curricular22 = UC("uc22", "automacao1", [self._professores[11], self._professores[12]], 1)
        unidade_curricular23 = UC("uc23", "adpe", [self._professores[1], self._professores[5]], 0)
        unidade_curricular24 = UC("uc24", "maquinastermicas", [self._professores[6]], 0)

        self._ucs = [unidade_curricular1, unidade_curricular2, unidade_curricular3,
                     unidade_curricular4, unidade_curricular5, unidade_curricular6,
                     unidade_curricular7, unidade_curricular8, unidade_curricular9,
                     unidade_curricular10, unidade_curricular11, unidade_curricular12,
                     unidade_curricular13, unidade_curricular14, unidade_curricular15,
                     unidade_curricular16, unidade_curricular17, unidade_curricular18,
                     unidade_curricular19, unidade_curricular20, unidade_curricular21,
                     unidade_curricular22, unidade_curricular23, unidade_curricular24]

        grupo1 = Grupo("g1", 25, [unidade_curricular1, unidade_curricular2,
                                  unidade_curricular3, unidade_curricular5,
                                  unidade_curricular6, unidade_curricular21,
                                  unidade_curricular22, unidade_curricular10])

        grupo2 = Grupo("g2", 35, [unidade_curricular13, unidade_curricular12,
                                  unidade_curricular19, unidade_curricular9,
                                  unidade_curricular4, unidade_curricular16,
                                  unidade_curricular23, unidade_curricular2])

        grupo3 = Grupo("g3", 30, [unidade_curricular18, unidade_curricular7,
                                  unidade_curricular1, unidade_curricular4,
                                  unidade_curricular12, unidade_curricular20,
                                  unidade_curricular24, unidade_curricular17])

        grupo4 = Grupo("g4", 50, [unidade_curricular8, unidade_curricular10,
                                  unidade_curricular11, unidade_curricular15,
                                  unidade_curricular17, unidade_curricular5,
                                  unidade_curricular14, unidade_curricular19])

        self._grupos = [grupo1, grupo2, grupo3, grupo4]
        self._numeroAulas = 0

        for i in range(len(self._grupos)):
            self._numeroAulas += len(self._grupos[i].get_ucs())

    def get_salas(self):
        return self._salas

    def get_professores(self):
        return self._professores

    def get_ucs(self):
        return self._ucs

    def get_grupos(self):
        return self._grupos

    def get_blocos(self):
        return self._blocos


class Horario:

    def __init__(self):
        self._data = data
        self._aulas = []
        self._numdeIncompatibilidades = 0
        self._fitness = -1
        self._classNumb = 0
        self._isFitnessChanged = True
        self.total_distance = 0
        self.distance = []
        self.blocos = []
        self.distg4 = 0
        self.distg1 = 0
        self.distg2 = 0
        self.distg3 = 0

    def get_aulas(self):
        self._isFitnessChanged = True
        return self._aulas

    def get_numdeIncompatibilidades(self):
        return self._numdeIncompatibilidades

    def get_fobjetivo(self):
        if self._isFitnessChanged:
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False

        return self._fitness

    def initialize(self):
        grupos = self._data.get_grupos()
        for i in range(len(grupos)):
            ucs = grupos[i].get_ucs()
            for j in range(len(ucs)):
                nova_aula = Aula(self._classNumb, grupos[i], ucs[j])
                self._classNumb += 1
                nova_aula.set_bloco(data.get_blocos()[rnd.randrange(0, len(data.get_blocos()))])
                nova_aula.set_sala(data.get_salas()[rnd.randrange(0, len(data.get_salas()))])
                nova_aula.set_professor(
                    ucs[j].get_professor()[rnd.randrange(0, len(ucs[j].get_professor()))])
                self._aulas.append(nova_aula)

        return self

    def calculate_fitness(self):
        self.distance = []
        self.blocos = []
        self.distg0 = 0
        self.distg1 = 0
        self.distg2 = 0
        self.distg3 = 0

        self._numdeIncompatibilidades = 0
        self.total_distance = 0
        aulas = self.get_aulas()
        for i in range(len(aulas)):
            if aulas[i].get_sala().get_lotacao() < aulas[i].get_grupo().get_grupo_lotacao():
                self._numdeIncompatibilidades += 1
            if aulas[i].get_sala().get_tuc() != aulas[i].get_uc().get_tuc():
                self._numdeIncompatibilidades += 1

            if aulas[i].get_bloco().get_id() == aulas[i].get_professor().get_atendimento():
                self._numdeIncompatibilidades += 1

            for j in range(len(aulas)):
                if j >= i:
                    if aulas[i].get_bloco() == aulas[j].get_bloco() \
                            and aulas[i].get_id() != aulas[j].get_id():

                        if aulas[i].get_sala() == aulas[j].get_sala():
                            self._numdeIncompatibilidades += 1

                        if aulas[i].get_professor() == aulas[j].get_professor():
                            self._numdeIncompatibilidades += 1

                # lista_de_blocos = ['g1', 'g2', 'g3', 'g4']

                # for m in range(4):
                #     if aulas[i].get_grupo().get_nome() == lista_de_blocos[m]:
                #         globals()['distance%s' % m] = aulas[i].get_sala().get_distancia()
                #         globals()['bloco%s' % m] = aulas[i].get_bloco().get_id()
                #
                #         globals()['self.blocos%s' % m].append(globals()['bloco%s' % m])
                #         globals()['self.distance%s' % m].append(globals()['distance%s' % m])
                #
                #         globals()['zipped_lists%s' % m] = zip(globals()['bloco%s' % m], globals()['distance%s' % m])
                #         globals()['sorted_zipped_lists%s' % m] = sorted(globals()['zipped_lists%s' % m], reverse=False)
                #         globals()['order_distance%s' % m] = []
                #         for b, dist in (globals()['sorted_zipped_lists%s' % m]):
                #             globals()['order_distance%s' % m].append(dist)
                #         globals()['dist_final%s' % m] = []
                #         for n in range(len(globals()['order_distance%s' % m])):
                #             #     if n and n + 1:
                #             globals()['calc%s' % m] = abs(globals()['order_distance%s' % m][n] - globals()['order_distance%s' % m][n - 1])
                #             globals()['dist_final%s' % m].append(globals()['calc%s' % m])
                #         globals()['self.distg%s' % m] = sum(globals()['dist_final%s' % m])

                # if aulas[i].get_grupo().get_nome() == 'g2':
                #     distance = aulas[i].get_sala().get_distancia()
                #     bloco = aulas[i].get_bloco().get_id()
                #     self.blocos2.append(bloco)
                #     self.distance2.append(distance)
                #     zipped_lists = zip(self.blocos2, self.distance2)
                #     sorted_zipped_lists = sorted(zipped_lists, reverse=False)
                #     order_distance = []
                #     for b, dist in sorted_zipped_lists:
                #         order_distance.append(dist)
                #     dist_final = []
                #     for n in range(len(order_distance)):
                #         calc = abs(order_distance[n] - order_distance[n - 1])
                #         dist_final.append(calc)
                #     self.distg2 = sum(dist_final)
                #
                if aulas[i].get_grupo().get_nome() == 'g1':
                    distance = aulas[i].get_sala().get_distancia()
                    bloco = aulas[i].get_bloco().get_id()
                    self.blocos.append(bloco)
                    self.distance.append(distance)
                    zipped_lists = zip(self.blocos, self.distance)
                    sorted_zipped_lists = sorted(zipped_lists, reverse=False)
                    order_distance = []
                    for b, dist in sorted_zipped_lists:
                        order_distance.append(dist)
                    dist_final = []
                    for n in range(len(order_distance)):
                        #     if n and n + 1:
                        calc = abs(order_distance[n] - order_distance[n - 1])
                        dist_final.append(calc)
                    self.distg1 = sum(dist_final)

                if aulas[i].get_grupo().get_nome() == 'g2':
                    distance = aulas[i].get_sala().get_distancia()
                    bloco = aulas[i].get_bloco().get_id()
                    self.blocos.append(bloco)
                    self.distance.append(distance)
                    zipped_lists = zip(self.blocos, self.distance)
                    sorted_zipped_lists = sorted(zipped_lists, reverse=False)
                    order_distance = []
                    for b, dist in sorted_zipped_lists:
                        order_distance.append(dist)
                    dist_final = []
                    for n in range(len(order_distance)):
                        #     if n and n + 1:
                        calc = abs(order_distance[n] - order_distance[n - 1])
                        dist_final.append(calc)
                    self.distg2 = sum(dist_final)

                if aulas[i].get_grupo().get_nome() == 'g3':
                    distance = aulas[i].get_sala().get_distancia()
                    bloco = aulas[i].get_bloco().get_id()
                    self.blocos.append(bloco)
                    self.distance.append(distance)
                    zipped_lists = zip(self.blocos, self.distance)
                    sorted_zipped_lists = sorted(zipped_lists, reverse=False)
                    order_distance = []
                    for b, dist in sorted_zipped_lists:
                        order_distance.append(dist)
                    dist_final = []
                    for n in range(len(order_distance)):
                        #     if n and n + 1:
                        calc = abs(order_distance[n] - order_distance[n - 1])
                        dist_final.append(calc)
                    self.distg3 = sum(dist_final)

                if aulas[i].get_grupo().get_nome() == 'g4':
                    distance = aulas[i].get_sala().get_distancia()
                    bloco = aulas[i].get_bloco().get_id()
                    self.blocos.append(bloco)
                    self.distance.append(distance)
                    zipped_lists = zip(self.blocos, self.distance)
                    sorted_zipped_lists = sorted(zipped_lists, reverse=False)
                    order_distance = []
                    for b, dist in sorted_zipped_lists:
                        order_distance.append(dist)
                    dist_final = []
                    for n in range(len(order_distance)):
                        #     if n and n + 1:
                        calc = abs(order_distance[n] - order_distance[n - 1])
                        dist_final.append(calc)
                    self.distg4 = sum(dist_final)

                # lista_blocos = ['g1', 'g2', 'g3', 'g4']

            self.total_distance = self.distg4 + self.distg1 + self.distg2 + self.distg3
            # self.total_distance =self.distg2

        return self.total_distance + math.exp(7 * self._numdeIncompatibilidades)

        # return self.total_distance

    def __str__(self):
        return_value = ''
        for i in range(len(self._aulas) - 1):
            return_value += str(self._aulas[i]) + ', '

        return_value += str(self._aulas[len(self._aulas) - 1])

        return return_value


class Population:
    def __init__(self, size):
        self._size = size
        self._data = data
        self._horarios = []
        for i in range(size):
            self._horarios.append(Horario().initialize())

    def get_horarios(self):
        return self._horarios


class GeneticAlgorithm:
    def evolve(self, population):
        return self._mutate_population(self._crossover_population(population))

    def _crossover_population(self, pop):
        crossover_pop = Population(0)
        for i in range(NUMB_OF_ELITE_SCHEDULES):
            crossover_pop.get_horarios().append(pop.get_horarios()[i])

        i = NUMB_OF_ELITE_SCHEDULES

        while i < POPULATION_SIZE:
            schedule1 = self._select_tournament_population(pop).get_horarios()[0]
            schedule2 = self._select_tournament_population(pop).get_horarios()[0]
            crossover_pop.get_horarios().append(self._crossover_schedule(schedule1, schedule2))

            i += 1

        return crossover_pop

    def _mutate_population(self, population):
        for i in range(NUMB_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            self._mutate_schedule(population.get_horarios()[i])

        return population

    def _crossover_schedule(self, schedule1, schedule2):
        self.is_not_used()
        crossover_schedule = Horario().initialize()
        for i in range(0, len(crossover_schedule.get_aulas())):
            if rnd.random() > 0.5:
                crossover_schedule.get_aulas()[i] = schedule1.get_aulas()[i]
            else:
                crossover_schedule.get_aulas()[i] = schedule2.get_aulas()[i]

        return crossover_schedule

    def _mutate_schedule(self, mutateSchedule):
        self.is_not_used()
        horario = Horario().initialize()
        for i in range(len(mutateSchedule.get_aulas())):
            if MUTATION_RATE > rnd.random():
                mutateSchedule.get_aulas()[i] = horario.get_aulas()[i]
        return mutateSchedule

    def _select_tournament_population(self, pop):
        self.is_not_used()
        tournament_pop = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_pop.get_horarios().append(pop.get_horarios()[rnd.randrange(0, POPULATION_SIZE)])
            i += 1

        tournament_pop.get_horarios().sort(key=lambda x: x.get_fobjetivo(), reverse=False)

        return tournament_pop

    def is_not_used(self):
        pass


class DisplayMgr:

    def print_available_data(self):
        self.is_not_used()
        print("> All Available Data")
        self.print_dept()
        self.print_course()
        self.print_room()
        self.print_instructor()
        self.print_meeting_times()

    def print_dept(self):
        self.is_not_used()
        grupos = data.get_grupos()
        available_grupos_table = prettytable.PrettyTable(['nome', 'UCs', 'Lotacao'])

        for i in range(len(grupos)):
            ucs = grupos.__getitem__(i).get_ucs()
            temp_str = "["

            for j in range(len(ucs) - 1):
                temp_str += ucs[j].__str__() + ", "
            temp_str += ucs[len(ucs) - 1].__str__() + "]"
            available_grupos_table.add_row([grupos.__getitem__(i).get_nome(),
                                            temp_str, str(grupos.__getitem__(i).get_grupo_lotacao())])

        print(available_grupos_table)

    def print_course(self):
        self.is_not_used()
        available_ucs_table = prettytable.PrettyTable(['id', 'nome', 'professores', 'tuc'])
        ucs = data.get_ucs()

        for i in range(len(ucs)):
            professores = ucs[i].get_professor()
            temp_str = ""

            for j in range(len(professores) - 1):
                temp_str += professores[j].__str__() + ", "
            temp_str += professores[len(professores) - 1].__str__()
            available_ucs_table.add_row(
                [ucs[i].get_id(), ucs[i].get_nome(), temp_str, str(ucs[i].get_tuc())]
            )
        print(available_ucs_table)

    def print_room(self):
        self.is_not_used()
        availableRoomsTable = prettytable.PrettyTable(['nome', 'tuc', 'lotacao', 'dist'])
        salas = data.get_salas()
        for i in range(len(salas)):
            availableRoomsTable.add_row([str(salas[i].get_nome()), str(salas[i].get_tuc()),
                                         str(salas[i].get_lotacao()), str(salas[i].get_distancia())])
        print(availableRoomsTable)

    def print_instructor(self):
        self.is_not_used()
        available_instructor_table = prettytable.PrettyTable(['nome', 'atendimento'])
        professores = data.get_professores()

        for i in range(len(professores)):
            available_instructor_table.add_row([professores[i].get_nome(), str(professores[i].get_atendimento())])
        print(available_instructor_table)

    def print_meeting_times(self):
        self.is_not_used()
        availableMeetingTimeTable = prettytable.PrettyTable(['id', 'horario'])
        blocos = data.get_blocos()

        for i in range(len(blocos)):
            availableMeetingTimeTable.add_row([blocos[i].get_id(), blocos[i].get_hora()])
        print(availableMeetingTimeTable)

    def print_generation(self, population):
        self.is_not_used()
        table1 = prettytable.PrettyTable(['Horario #', 'Função Objetivo', '# de Incompatibilidades',
                                          'Aulas [Grupo,UC,Sala,Professor,bloco]'])
        horarios = population.get_horarios()

        for i in range(len(horarios)):
            table1.add_row(
                [str(i + 1), round(horarios[i].get_fobjetivo(), 3), horarios[i].get_numdeIncompatibilidades(),
                 horarios[i].__str__()])

        print(table1)

    def print_schedule_as_table(self, schedule):
        self.is_not_used()
        table1 = prettytable.PrettyTable(
            ['Aula #', 'Grupo (Lotacao)', 'UC (Nome, Tipologia)', "Sala (Lotacao, Tipologia, Distancia)",
             "Professor (Atendimento)", "Bloco (Horario)", ])
        aulas = schedule.get_aulas()

        for i in range(len(aulas)):
            uc = aulas[i].get_uc().get_id() + " (" + aulas[i].get_uc().get_nome() + ", " + \
                 str(aulas[i].get_uc().get_tuc()) + ")"

            professor = aulas[i].get_professor().get_nome() + " (" + str(
                aulas[i].get_professor().get_atendimento()) + ")"

            sala = aulas[i].get_sala().get_nome() + " (" + str(aulas[i].get_sala().get_lotacao()) \
                   + ", " + str(aulas[i].get_sala().get_tuc()) + ", " + str(aulas[i].get_sala().get_distancia()) + ")"

            bloco = aulas[i].get_bloco().get_id() + " (" + aulas[i].get_bloco().get_hora() + ")"

            table1.add_row(
                [aulas[i].get_id(),
                 aulas[i].get_grupo().get_nome() + " (" + str(aulas[i].get_grupo().get_grupo_lotacao()) + ")",
                 uc, sala, professor, bloco]
            )

        print(table1)

    def is_not_used(self):
        pass


data = Data()
display = DisplayMgr()
display.print_available_data()

generation_number = 0
print("\n> Generation #", generation_number)

population = Population(POPULATION_SIZE)
# population.get_horarios().sort(key=lambda x: x.get_fitness(), reverse=True)
population.get_horarios().sort(key=lambda x: x.get_fobjetivo(), reverse=False)
display.print_generation(population)
geneticAlgorithm = GeneticAlgorithm()

i = 0
# new_dist =
# print('okay' + str(new_dist))
dist_gra = []
dist_old = 0
dist_max = []
dist_mean = []
dists = []
while population.get_horarios()[0].get_fobjetivo() > dist_old or \
        population.get_horarios()[0].get_numdeIncompatibilidades() != 0:

    new_dist = population.get_horarios()[0].get_fobjetivo()
    max_dist = population.get_horarios()[-1].get_fobjetivo()
    dists = []
    for y in range(49):
        distancia = population.get_horarios()[y].get_fobjetivo()
        dists.append(distancia)

    dist_mean.append(sum(dists)/len(dists))

    if new_dist < dist_old:
        new_dist = dist_old

    generation_number += 1
    print("\n> Iteração #", generation_number)
    population = geneticAlgorithm.evolve(population)
    # population.get_horarios().sort(key=lambda x: x.get_fitness(), reverse=True)
    population.get_horarios().sort(key=lambda x: x.get_fobjetivo(), reverse=False)
    display.print_generation(population)
    display.print_schedule_as_table(population.get_horarios()[0])

    print('Resultado Função Objetivo - Distancia Total: ' + str(new_dist))
    dist_gra.append(new_dist)
    dist_max.append(max_dist)

    # display.print_mean(population)
    # display.print_std(population)
    i += 1
    if i >= 10:
        break

# sys.stdout.close()
# print(new_dist)

    distancia_min = dist_gra
    iteracao = list(range(0, generation_number))
    distancia_max = dist_max
    distancia_mean = dist_mean

    df = pd.DataFrame({
        'x_axis': iteracao,
        'y_axis': distancia_min})

    df_max = pd.DataFrame({
        'x_axis': iteracao,
        'y_axis': distancia_max})

    df_mean = pd.DataFrame({
        'x_axis': iteracao,
        'y_axis': distancia_mean})

    plt.autoscale(enable=True, axis='both', tight=None)
    plt.plot('x_axis', 'y_axis', data=df, linestyle='-', marker='o', color='r', label='Min dist')
    plt.plot('x_axis', 'y_axis', data=df_max, linestyle='-', marker='o', color='g', label='Max dist')
    plt.plot('x_axis', 'y_axis', data=df_mean, linestyle='-', marker='o', color='b', label='Mean dist')
    plt.yscale('log')
    plt.xscale('log')
    plt.title('Minimização distâncias percorridas em horários')
    plt.xlabel('No de Iterações')
    plt.ylabel('Função Objetivo (m)')

    plt.pause(0.05)

end_time = time.time()
tempo = (end_time - start_time)/60
print('Elapsed time is ' + str(tempo) + ' minutes')
# plt.legend()
plt.show()
