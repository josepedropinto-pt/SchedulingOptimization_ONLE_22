#!/usr/bin/python3

from classes import Professor, Course, Student
from data import *
from colorama import Fore, Back, Style


class Schedule:
    def __init__(self):
        # <---------------------------------------------------------------------->
        # <-------------------Variable Initialization---------------------------->
        # <---------------------------------------------------------------------->
        self.studentsList = []
        self.professorsList = []
        self.coursesList = []
        self.blocksList = []
        self.roomsList = []
        self.groupsList = []
        self.decision_variable_x1 = False
        self.decision_variable_x2 = False
        self.decision_variable_y1 = False
        self.constrain1_valid = False
        self.constrain2_valid = False
        self.constrain3_valid = False
        self.constrain4_valid = False


        self.dataSetup()
        self.scheduling()

    def dataSetup(self):
        self.studentsList = creatStudents()
        self.professorsList = creatProfessors()
        self.coursesList = creatCourses()
        self.blocksList = creatBlocks()
        self.roomsList = creatRooms()
        self.groupsList = creatGroups()

    def scheduling(self):

        # Correr as UC's
        for course in self.coursesList:
            print(course.course_name)

            # Correr todos os Grupos
            for group in self.groupsList:
                if course.course_name in group.group_classes:
                    print(f"encontrei o grupo {group.group_id} para a uc {course.course_name} ")

                    # Correr todas as salas
                    for room in self.roomsList:
                        self.constrain1(room.room_tuc, course.course_tuc)
                        self.constrain2(room.room_capacity, group.group_capacity)
                        if self.constrain1_valid and self.constrain2_valid:
                            print(f"Encontrei a sala {room.room_name} com tuc {room.room_tuc} "
                                  f"igual ao tuc da uc {course.course_tuc} "
                                  f" e com lotação de {room.room_capacity} "
                                  f"superior à lotação do grupo {group.group_capacity}")

                            # Correr Todos os Professores
                            for professor in self.professorsList:
                                self.constrain3(professor.professor_classes, course.course_name)
                                if self.constrain3_valid:
                                    print(f"O professor {professor.professor_name} "
                                          f"pode lecionar a cadeira {course.course_name}")

                                    # Correr todos os blocos horários
                                    for block in self.blocksList:
                                        # self.constrain4(professor.professor_atendimento, block.block_id)
                                        if self.constrain4_valid:
                                            print(f"Aloquei o bloco {block.block_id} que "
                                                  f"não condiciona o atendimento no bloco "
                                                  f"{professor.professor_atendimento} do professor")

                                break

                    break
            break

    # # A tipologia da sala deve ser igual à tipologia da UC
    # def constrain4(self, roomTuc, courseTuc):
    #     if roomTuc == courseTuc:
    #         self.constrain1_valid = True
    #     else:
    #         self.constrain1_valid = False

    # A tipologia da sala deve ser igual à tipologia da UC
    def constrain1(self, roomTuc, courseTuc):
        if roomTuc == courseTuc:
            self.constrain1_valid = True
        else:
            self.constrain1_valid = False

    # A lotação da sala deve ser igual ou superior à do grupo
    def constrain2(self, roomCapacity, groupCapacity):
        if roomCapacity >= groupCapacity:
            self.constrain2_valid = True
        else:
            self.constrain2_valid = False

    # Cada professor só pode lecionar as uc's em que está registado
    def constrain3(self, professorClasses, courseName):
        for n in range(0, len(professorClasses)):
            if courseName in professorClasses[n]:
                self.constrain3_valid = True
                break
            else:
                self.constrain3_valid = False

    # Um Professor não pode lecionar no seu bloco de atendimento
    def constrain4(self, professorAtendimento, blockId):
        for n in range(0, len(blockId)):
            if professorAtendimento in blockId[n]:
                self.constrain4_valid = False
            else:
                self.constrain4_valid = True
                break





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

    def assignClass(self, room, professor, course, block, group):
        pass


def main():
    # ------------------------------------------------------
    # Execution
    # ------------------------------------------------------
    Schedule()


if __name__ == '__main__':
    main()
