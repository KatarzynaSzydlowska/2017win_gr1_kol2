#!/usr/bin/python
from __future__ import division
from collections import defaultdict
from cmd import Cmd
import json


class Diary:
    def __init__(self):
        self.class_diary = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

    def add_grade(self, name, surname, subject, grade):
        self.class_diary[name + surname][subject]["Grades"].append(float(grade))

    def mark_attendance(self, name, surname, subject, if_present):
        self.class_diary[name + surname][subject]["Attendance"].append(float(if_present))

    def get_average(self, my_list):
        return sum(my_list) / len(my_list)

    def get_subject_average(self, name, surname, subject):
        return self.get_average(self.class_diary[name + surname][subject]["Grades"])

    def get_total_average(self, name, surname):
        averages = [self.get_subject_average(name, surname, subj) for subj in self.class_diary[name + surname].keys()]
        return self.get_average(averages)

    def get_total_attendance(self, name, surname):
        attendance = [item for subj in self.class_diary[name + surname].values() for item in subj["Attendance"]]
        return self.get_average(attendance)

    def dump(self, filename):
        with open(filename, 'w') as dump_file:
            json.dump(self.__dict__, dump_file)


class MyPrompt(Cmd):
    def __init__(self, class_diary):
        Cmd.__init__(self)
        self.diary = class_diary

    def do_a(self, line):
        self.diary.add_grade(*line.split())

    def do_b(self, line):
        self.diary.mark_attendance(*line.split())

    def do_c(self, line):
        print self.diary.get_subject_average(*line.split())

    def do_d(self, line):
        print self.diary.get_total_average(*line.split())

    def do_e(self, line):
        print self.diary.get_total_attendance(*line.split())

    def do_quit(self, args):
        raise SystemExit


if __name__ == '__main__':
    diary = Diary()
    diary.add_grade("Jakub", "Nowak", "Matematyka", 5.0)
    diary.add_grade("Jakub", "Nowak", "Matematyka", 4.0)
    diary.add_grade("Jakub", "Nowak", "Fizyka", 4.0)
    diary.add_grade("Michal", "Nowak", "Matematyka", 5.0)
    diary.mark_attendance("Jakub", "Nowak", "Matematyka", True)
    diary.mark_attendance("Jakub", "Nowak", "Matematyka", True)
    diary.mark_attendance("Jakub", "Nowak", "Matematyka", False)
    diary.mark_attendance("Jakub", "Nowak", "Fizyka", False)
    print diary.class_diary["JakubNowak"]["Matematyka"]["Grades"]
    print diary.class_diary["MichalNowak"]["Matematyka"]["Grades"]
    print diary.get_subject_average("Jakub", "Nowak", "Matematyka")
    print diary.get_total_average("Jakub", "Nowak")
    print diary.get_total_attendance("Jakub", "Nowak")
    diary.dump("my_dump.json")

    prompt = MyPrompt(diary)
    prompt.prompt = '> '
    prompt.cmdloop("""Welcome to class diary! Options:
            a) Add grade (type: a <name> <surname> <subject> <grade>)
            b) Mark attendance (type: b <name> <surname> <subject> <1/0>)
            c) Get subject average (type: c <name> <surname> <subject>) 
            d) Get total average (type: d <name> <surname>)
            e) Get total attendance (type: e <name> <surname>) """)

