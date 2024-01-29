# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2021)
#objective: ex01 - test class Person

"""""
from pessoa import Pessoa

# Creates two object with arguments: name, date of birthday
p1 = Pessoa("Carlos Sousa", "1958-03-23")
p2 = Pessoa.from_string("Joana Pinto, 1980-04-27")
# Print objects
print(p1)
print(p2)
# print attributes
print('Name:', p1.name)
print('Date of birth:', p1.dob)
print('age:', p1.age)
# Use methods
print('Apelido:', p1.apelido())
print('Nome próprio:', p1.nomeproprio())