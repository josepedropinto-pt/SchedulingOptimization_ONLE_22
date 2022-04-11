#!/usr/bin/python3
from classes import Professor, Course, Student


def creatStudents():
    global students
    s1 = Student(name='jose', classes=['algebra', 'calculo'])
    s2 = Student(name='carlos', classes=['ingles', 'espanhol'])
    students = [s1, s2]
    return students


def creatProfessor():
    p1 = Professor(name='gil', classes=['algebra', 'espanhol'])
    p2 = Professor(name='jalex', classes=['ingles'])
    professors = [p1, p2]
    return professors


def creatCourse():
    c1 = Course(name='algebra', tuc=0, professor='gil')
    c2 = Course(name='ingles', tuc=1, professor='jalex')
    courses = [c1, c2]
    return courses


def creatBlocks():
    days = ['segunda', 'terca', 'quarta', 'quinta', 'sexta']
    hours = [1, 2, 3, 4, 5, 6]
    blocks = []
    id = 0
    for day in days:
        for hour in hours:
            block = id, (day, hour)
            blocks.append(block)
            id += 1
    return blocks
