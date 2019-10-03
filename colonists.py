# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 17:30:50 2019

@author: matej
"""

# Module gonverning the attributes of the colonists

import random
from random import randint

class Colonist:
    
    def __init__(self, age, sex, params):
        self.age = age
        self.sex = sex
        self.pregnant = -1
        self.dead = False
        self.cooldown = 0
        self.params = params
    
    def getAge(self):
        return self.age
    
    def getSex(self):
        return self.sex
    
    def incAge(self):
        self.age = self.age+1
    
    def incPregnant(self):
        self.pregnant = self.pregnant+1
        
    def getPregnant(self):
        return self.pregnant
    
    def startPregnant(self):
        self.pregnant = 0
    
    def birth(self):
        self.pregnant = -1
        self.cooldown = self.params.getCOOLDOWN()
        
    def isChild(self):
        return self.age<18
    
    def setDead(self):
        self.dead = True
    
    def isDead(self):
        return self.dead
    
    def setCooldown(self, cool):
        self.cooldown = cool
    
    def getCooldown(self):
        return self.cooldown
    
    def decCooldown(self):
        self.cooldown = self.cooldown-1
    
class Astronaut(Colonist):
    
    def __init__(self, sex, params):
        Colonist.__init__(self, randint(params.getASTRO_MIN_AGE(),params.getASTRO_MAX_AGE()), sex, params)
        
    def getName(self):
        return "Astronaut"
    
class Martian(Colonist):
    
    def __init__(self, params):
        Colonist.__init__(self, 0, random.choice(["m", "f"]), params)
        
    def getName(self):
        return "Martian"