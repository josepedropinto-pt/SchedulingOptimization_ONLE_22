#!/usr/bin/python3

class Professor:
    def __init__(self, name, classes):
        self.professor_name = name
        self.professor_classes = classes


class Course:
    def __init__(self, name, tuc, professor):
        self.course_name = name
        self.course_tuc = tuc
        self.course_professor = professor


class Student:
    def __init__(self, name, classes):
        self.student_name = name
        self.student_classes = classes

