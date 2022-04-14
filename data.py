#!/usr/bin/python3
from classes import *


def creatStudents():
    s1 = Student(name='jose', classes=['algebra', 'calculo'])
    s2 = Student(name='carlos', classes=['ingles', 'espanhol'])
    students = [s1, s2]
    return students


def creatCourses():
    c1 = Course(name='tpl', tuc=2, professor=['bastos'])
    c2 = Course(name='dem', tuc=0, professor=['bastos', 'rui'])
    c3 = Course(name='estruturas', tuc=0, professor=['balaco'])
    c4 = Course(name='desenho', tuc=0, professor=['jalex', 'rui'])
    c5 = Course(name='ipm', tuc=0, professor=['balaco', 'ramos'])
    c6 = Course(name='solidos', tuc=0, professor=['robert', 'ricardo'])
    c7 = Course(name='iem', tuc=0, professor=['robert', 'gil'])
    c8 = Course(name='spt', tuc=1, professor=['ricardo'])
    c9 = Course(name='onle', tuc=0, professor=['gil', 'jalex'])
    c10 = Course(name='cfac', tuc=1, professor=['ramos'])

    courses = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
    return courses


def creatProfessors():
    p1 = Professor(name='bastos', classes=['tpl', 'dem'], atendimento=2)
    p2 = Professor(name='rui', classes=['desenho', 'dem'], atendimento=5)
    p3 = Professor(name='balaco', classes=['estruturas', 'ipm'], atendimento=12)
    p4 = Professor(name='robert', classes=['solidos', 'iem'], atendimento=7)
    p5 = Professor(name='ricardo', classes=['solidos', 'spt'], atendimento=15)
    p6 = Professor(name='gil', classes=['iem', 'onle'], atendimento=10)
    p7 = Professor(name='jalex', classes=['onle', 'desenho'], atendimento=9)
    p8 = Professor(name='ramos', classes=['ipm', 'cfac'], atendimento=19)

    professors = [p1, p2, p3, p4, p5, p6, p7, p8]
    return professors


# def creatBlocks():
#     days = ['segunda', 'terca', 'quarta', 'quinta', 'sexta']
#     hours = [1, 2, 3, 4, 5, 6]
#     blocks = []
#     id = 0
#     for day in days:
#         for hour in hours:
#             block = id, (day, hour)
#             blocks.append(block)
#             id += 1
#     return blocks

def creatBlocks():
    b1 = Block(id=0, day='Segunda', hour='9-11')
    b2 = Block(id=1, day='Segunda', hour='11-13')
    b3 = Block(id=2, day='Segunda', hour='13-14')
    b4 = Block(id=3, day='Segunda', hour='14-16')
    b5 = Block(id=4, day='Segunda', hour='16-18')

    b6 = Block(id=5, day='Terca', hour='9-11')
    b7 = Block(id=6, day='Terca', hour='11-13')
    b8 = Block(id=7, day='Terca', hour='13-14')
    b9 = Block(id=8, day='Terca', hour='14-16')
    b10 = Block(id=9, day='Terca', hour='16-18')

    b11 = Block(id=10, day='Quarta', hour='9-11')
    b12 = Block(id=11, day='Quarta', hour='11-13')
    b13 = Block(id=12, day='Quarta', hour='13-14')
    b14 = Block(id=13, day='Quarta', hour='14-16')
    b15 = Block(id=14, day='Quarta', hour='16-18')

    b16 = Block(id=15, day='Quinta', hour='9-11')
    b17 = Block(id=16, day='Quinta', hour='11-13')
    b18 = Block(id=17, day='Quinta', hour='13-14')
    b19 = Block(id=18, day='Quinta', hour='14-16')
    b20 = Block(id=19, day='Quinta', hour='16-18')

    b21 = Block(id=20, day='Sexta', hour='9-11')
    b22 = Block(id=21, day='Sexta', hour='11-13')
    b23 = Block(id=22, day='Sexta', hour='13-14')
    b24 = Block(id=23, day='Sexta', hour='14-16')
    b25 = Block(id=24, day='Sexta', hour='16-18')

    blocks = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13,
             b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25]

    return blocks

def creatRooms():
    r1 = Room(name=1, tuc=0, capacity=40, dist=15)
    r2 = Room(name=2, tuc=0, capacity=40, dist=20)
    r3 = Room(name=3, tuc=0, capacity=30, dist=10)
    r4 = Room(name=4, tuc=2, capacity=35, dist=30)
    r5 = Room(name=5, tuc=1, capacity=35, dist=30)

    rooms = [r1, r2, r3, r4, r5]
    return rooms


def creatGroups():
    g1 = Group(id=0, capacity=25, classes=['tpl', 'dem', 'estruturas', 'ipm', 'solidos'])
    g2 = Group(id=1, capacity=35, classes=['iem', 'spt', 'onle', 'desenho', 'cfac'])
    g3 = Group(id=2, capacity=30, classes=['tpl', 'estruturas', 'solidos', 'spt', 'desenho'])

    groups = [g1, g2, g3]
    return groups
