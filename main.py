#!/usr/bin/python3

from classes import Professor, Course, Student
from data import *


def main():
    studentsList = creatStudents()
    professorsList = creatProfessor()
    coursesList = creatCourse()
    blocksList = creatBlocks()

    for n in range(0, len(studentsList)):
        print('My name is ' + str(studentsList[n].student_name) +
              ' and I have this classes ' + str(studentsList[n].student_classes))

    for n in range(0, len(professorsList)):
        print('My name is Professor ' + str(professorsList[n].professor_name) +
              ' and I have can lesson ' + str(professorsList[n].professor_classes))

    for n in range(0, len(coursesList)):
        print('This is ' + str(coursesList[n].course_name) +
              ' with this tipology ' + str(coursesList[n].course_tuc) +
              ' and can be lesson by professor ' + str(coursesList[n].course_professor))

    print(blocksList)


if __name__ == "__main__":
    main()
