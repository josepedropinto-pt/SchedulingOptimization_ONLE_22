#!/usr/bin/python3
from termcolor import cprint

from data import *
from colorama import Fore, Back, Style


class Horario:
    def __init__(self):
        # <---------------------------------------------------------------------->
        # <-------------------Variable Initialization---------------------------->
        # <---------------------------------------------------------------------->
        self.alunos_lista = []
        self.professores_lista = []
        self.uc_lista = []
        self.blocos_lista = []
        self.salas_lista = []
        self.grupos_lista = []
        self.aulas_atribuidas = []
        self.variavel_decisao_x1 = False
        self.variavel_decisao_x2 = False
        self.variavel_decisao_y1 = False
        self.restricao1_valida = False
        self.restricao2_valida = False
        self.restricao3_valida = False
        self.restricao4_valida = False

        self.baseDados()

    def baseDados(self):
        self.alunos_lista = criarAlunos()
        self.professores_lista = criarProfessores()
        self.uc_lista = criarUCs()
        self.blocos_lista = criarBlocos()
        self.grupos_lista = criarGrupos()
        self.salas_lista = criarSalas()
        self.selecaoHorario()

    def selecaoHorario(self):

        # while self.uc_lista: # Restricao 6, Todas as UCs tem que ter horario

            # Correr as UCs
            for uc in self.uc_lista:
                self.uc_lista.remove(uc)
                print(uc.uc_nome)

                # Correr todos os Grupos
                for grupo in self.grupos_lista:
                    if uc.uc_nome in grupo.grupo_UCs:
                        print(f"encontrei o grupo {grupo.grupo_id} para a uc {uc.uc_nome} ")

                        # Correr todas as salas
                        for sala in self.salas_lista:
                            self.restricao1(sala.sala_tuc, uc.uc_tuc)
                            self.restricao2(sala.sala_lotacao, grupo.grupo_lotacao)
                            if self.restricao1_valida and self.restricao2_valida:
                                print(f"Encontrei a sala {Fore.RED}{sala.sala_nome}{Fore.RESET} "
                                      f"com tuc {Fore.GREEN}{sala.sala_tuc}{Fore.RESET} igual ao tuc da uc "
                                      f"{Fore.GREEN}{uc.uc_tuc}{Fore.RESET} e com lotacao de "
                                      f"{Fore.BLUE}{sala.sala_lotacao}{Fore.RESET} superior à lotacao do"
                                      f" grupo {Fore.BLUE}{grupo.grupo_lotacao}{Fore.RESET}")

                                # Correr Todos os Professores
                                for professor in self.professores_lista:
                                    self.restricao3(professor.professor_UCs, uc.uc_nome)
                                    if self.restricao3_valida:
                                        print(f"O professor {professor.professor_nome} "
                                              f"pode lecionar a cadeira {uc.uc_nome}")

                                        # Correr todos os blocos horarios
                                        for bloco in self.blocos_lista:
                                            self.restricao4(professor.professor_atendimento, bloco.bloco_id)
                                            if self.restricao4_valida:
                                                print(f"Aloquei o bloco {bloco.bloco_id} que "
                                                      f"não condiciona o atendimento no bloco "
                                                      f"{professor.professor_atendimento} do professor")

                                            break
                                    break

                                break
                        break
                break
            self.atribuirAula(sala.sala_nome, professor.professor_nome, uc.uc_nome, bloco.bloco_id, grupo.grupo_id)

    def atribuirAula(self, sala, professor, uc, bloco, grupo):
        aula = (sala, professor, uc, bloco, grupo)
        cprint(f"A UC {uc} vai ser lecionada ao grupo {grupo} pelo professor {professor} "
               f"na sala {sala} durante o bloco {bloco}", color='white', on_color='on_blue', attrs=['bold'])
        self.aulas_atribuidas.append(aula)

    # A tipologia da sala deve ser igual à tipologia da UC
    def restricao1(self, salaTuc, ucTuc):
        if salaTuc == ucTuc:
            self.restricao1_valida = True
        else:
            self.restricao1_valida = False

    # A lotacao da sala deve ser igual ou superior à do grupo
    def restricao2(self, salaLotacao, grupoLotacao):
        if salaLotacao >= grupoLotacao:
            self.restricao2_valida = True
        else:
            self.restricao2_valida = False

    # Cada professor só pode lecionar as UCs em que esta registado
    def restricao3(self, professorUCs, ucNome):
        for n in range(0, len(professorUCs)):
            if ucNome in professorUCs[n]:
                self.restricao3_valida = True
                break
            else:
                self.restricao3_valida = False

    # Um Professor não pode lecionar no seu bloco de atendimento
    def restricao4(self, professorAtendimento, blocoId):
        if professorAtendimento == blocoId:
            self.restricao4_valida = False
        else:
            self.restricao4_valida = True


    # Um Grupo não pode assistir a duas aulas em simultâneo
    def constrain6(self, group, block):
        pass

    def constrain7(self):
        pass

    def objectiveFunction(self):
        pass

    def terminalPrints(self):
        print('im inside')

        # while self.professorsList:
        #     print(Fore.BLUE + str('Ainda há professor por atribuir') + Fore.RESET)

    # for n in range(0, len(self.coursesList)):
    #     for m in range(0, len(self.professorsList)):
    #         if self.coursesList[n].course_professor in self.professorsList[m].professor_name:
    #             print('found it')
    #             print(str(self.professorsList[m].professor_name))
    #             break
    #
    # for n in range(0, len(self.coursesList)):
    #     for m in range(0, len(self.roomsList)):
    #         if str(self.coursesList[n].course_tuc) in str(self.roomsList[m].room_tuc):
    #             print('i found a room for course ' + str(self.coursesList[n].course_name)
    #                   + ' : ' + str(self.roomsList[m].room_name))
    #         else:
    #             print('didn\'t found anything')

    # print(str(self.blocksList))

    # self.terminalPrints()
    # for n in range(0, len(professorsList)):
    #     print('My name is Professor ' + str(professorsList[n].professor_name) +
    #           ' and I have can lesson ' + str(professorsList[n].professor_classes))


def main():
    # ------------------------------------------------------
    # Execution
    # ------------------------------------------------------
    Horario()


if __name__ == '__main__':
    main()
