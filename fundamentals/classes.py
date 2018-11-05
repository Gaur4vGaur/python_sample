#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 06:34:26 2018

@author: gaurav
"""

students = []

class Student:
    
    school_name = "Good School"
    
    def __init__(self, name, student_id = 33):
        self.name = name
        self.student_id = student_id
        students.append(self)
        
    def __str__(self):
        return "Student - " + self.name
    
    def get_name_capitalize(self):
        return self.name.capitalize()
    
    # just for demonstation, school_name can be called directly
    def get_school_name(self):
        return self.school_name
    
 
''' Inheritence from Student '''
class HighSchoolStudent(Student):
    
    school_name = "Good High Shool"
    
    def get_school_name(self):
        return self.school_name

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"
