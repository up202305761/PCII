# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2021)
#objective: ex02 - test class VetorR3

"""""
from vetorR3 import VetorR3 

v1 = VetorR3.from_string('1,2,3')
v1.x = 2
print (v1.x+1)
nor = v1.norma()
print('Norma de v1 =', nor)
v2 = VetorR3(4,5,6)
esc = v1.escalar(v2)
print('Produto escalar=', esc)
vec = v1.vetorial(v2)
print('Produto vetorial=', vec)