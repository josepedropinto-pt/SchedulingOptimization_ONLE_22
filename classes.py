#!/usr/bin/python3

class Professor:
    def __init__(self, name, classes, atendimento):
        self.professor_name = name
        self.professor_classes = classes
        self.professor_atendimento = atendimento


class Course:
    def __init__(self, name, tuc, professor):
        self.course_name = name
        self.course_tuc = tuc
        self.course_professor = professor


class Student:
    def __init__(self, name, classes):
        self.student_name = name
        self.student_classes = classes


class Room:
    def __init__(self, name, tuc, capacity, dist):
        self.room_name = name
        self.room_tuc = tuc
        self.room_capacity = capacity
        self.room_distance = dist


class Group:
    def __init__(self,id, capacity, classes):
        self.group_id = id
        self.group_capacity = capacity
        self.group_classes = classes


class Block:
    def __init__(self, id, day, hour):
        self.block_id = id
        self.block_day = day
        self.block_hour = hour

