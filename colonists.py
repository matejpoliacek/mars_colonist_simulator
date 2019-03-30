# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 17:30:50 2019

@author: matej
"""

# Module gonverning the attributes of the colonists

import random
from random import randint

import mars_constants as MC


class Colonist:
    
    def __init__(self, age, sex):
        self.age = age
        self.sex = sex
        self.pregnant = -1
        self.dead = False
        self.cooldown = 0
    
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
        self.cooldown = MC.COOLDOWN
        
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
    
    def __init__(self, sex):
        Colonist.__init__(self, randint(25,45), sex)
        
    def getName(self):
        return "Astronaut"
    
class Martian(Colonist):
    
    def __init__(self):
        Colonist.__init__(self, 0, random.choice(["m", "f"]))
        
    def getName(self):
        return "Martian"