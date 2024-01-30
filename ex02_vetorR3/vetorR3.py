# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2021)
#objective: class VetorR3

"""""
import math

class VetorR3:
    
    def __init__(self, x=0, y=0, z=0):
        self._x = float(x)
        self._y = float(y)
        self._z = float(z)
        
    # Class method to implement constructor overloading
    @classmethod
    def from_string(cls, vetor_str):
        vetor_coord = vetor_str.split(",")
        return cls(vetor_coord[0], vetor_coord[1], vetor_coord[2])

    # Properties
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @property
    def z(self):
        return self._z
    
    # Methods
    def norma(self):
        vetnorma = math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        return vetnorma
    
    def escalar(self, other):
        esc = self.x * other.x + self.y * other.y +self.z * other.z
        return esc
    
    def vetorial(self, other):
        vetprod = VetorR3()
        vetprod._x = self.y * other.z - self.z * other.y
        vetprod._y = self.z * other.x - self.x * other.z
        vetprod._z = self.x * other.y - self.y * other.x
        return vetprod
    
    def __str__(self):
        return f'{self.x},{self.y},{self.z}'
