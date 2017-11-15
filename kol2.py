# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

# !/usr/bin/python



class Student:

    def __init__(self, name, surname, nr_of_classes):
        self.name = name
        self.surname = surname
        self.list_of_classes = []
        self.classes_dictionary = {}
        self.attendance_in_classes = [nr_of_classes]
        self.class_nr = 0

    def add_class(self, name):
        self.classes_dictionary[name] = self.class_nr
        self.class_nr = self.class_nr + 1
    
    def add_score( self, class_name, score):
        if class_name in self.classes_dictionary.keys():
            my_class = self.classes_dictionary[class_name]
            print my_class
            self.list_of_classes[int(my_class)].append(score)


if __name__ == '__main__':
    studentA = Student("Jan","Kowalski", 5)
    studentA.add_class("Math")
    studentA.add_score("Math",5.)
