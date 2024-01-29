# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2021)
#objective: class Person

"""""
#%% Class Pessoa
import datetime
class Pessoa:
    
    pp = 0
    # Constructor: Called when an object is instantiated
    def __init__(self, name, dob):
        # Object attributes
        self._name = name
        doblist = list(map(int, dob.split('-')))
        self._dob = datetime.date(doblist[0], doblist[1], doblist[2])
        Pessoa.pp += 1
    # Class method to implement constructor overloading
    @classmethod
    def from_string(cls, person_data):
        args_list = person_data.split(",")
        return cls(args_list[0], args_list[1])
    
    @staticmethod
    def abc(valor):
        return valor*2
        
    
    # name property getter method
    @property
    def name(self):
        return self._name
    # dob property getter method
    @property
    def dob(self):
        return self._dob
    # age property getter method
    @property
    def age(self):
        tday = datetime.date.today()
        age = tday.year - self.dob.year
        if tday.month < self.dob.month or \
            (tday.month == self.dob.month and tday.day < self.dob.day):
            age -= 1
        return age
    # Method to return the surname
    def apelido(self):
        names = self._name.split(' ')
        return names[-1]
    # Method to return the first name
    def nomeproprio(self):
        names = self._name.split(' ')
        return names[0]
    # Method to return object info
    def __str__(self):
        return f'{self.name}, {self.dob}, {self.age}'



p1 = Pessoa("Carlos Sousa", "1958-03-23")
p1 = Pessoa("Carlos Sousa", "1958-03-23")
p1 = Pessoa("Carlos Sousa", "1958-03-23")
print (p1.pp)