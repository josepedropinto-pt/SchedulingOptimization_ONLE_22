#!/usr/bin/python3

from classes import Professor, Course, Student
from data import *
from colorama import Fore, Back, Style


class Schedule:
    def __init__(self):
        # <----------------------------------------------------------------------------->
        # <----------------------Variable Initialization-------------------------------->
        # <----------------------------------------------------------------------------->

        self.studentsList = []
        self.professorsList = []
        self.coursesList = []
        self.blocksList = []
        self.roomsList = []
        self.dataSetup()

    def dataSetup(self):
        self.studentsList = creatStudents()
        self.professorsList = creatProfessors()
        self.coursesList = creatCourses()
        self.blocksList = creatBlocks()
        self.roomsList = creatRooms()

        for n in range(0, len(self.coursesList)):
            for m in range(0, len(self.professorsList)):
                if self.coursesList[n].course_professor in self.professorsList[m].professor_name:
                    print('found it')
                    print(str(self.professorsList[m].professor_name))
                    break

        for n in range(0, len(self.coursesList)):
            for m in range(0, len(self.roomsList)):
                if str(self.coursesList[n].course_tuc) in str(self.roomsList[m].room_tuc):
                    print('i found a room for course ' + str(self.coursesList[n].course_name)
                          + ' : ' + str(self.roomsList[m].room_name))
                else:
                    print('didn\'t found anything')
        self.terminalPrints()
        # for n in range(0, len(professorsList)):
        #     print('My name is Professor ' + str(professorsList[n].professor_name) +
        #           ' and I have can lesson ' + str(professorsList[n].professor_classes))

    def terminalPrints(self):

        print('im inside')

        # while self.professorsList:
        #     print(Fore.BLUE + str('Ainda há professor por atribuir') + Fore.RESET)


def main():
    # ------------------------------------------------------
    # Execution
    # ------------------------------------------------------
    Schedule()


if __name__ == '__main__':
    main()
