# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:20:52 2019

@author: matej
"""

import random
from random import randint
import matplotlib.pyplot as plt
import numpy as np

global SHIP_CAPACITY # how many astronauts come every 2 years from earth
global TRAVEL_TIME  # travel time from Earth to Mars (unused for now)
global COOLDOW  # how long betweeen maximum allowed pregnancies by a colonist
global MAX_PREGNANCIES # maximum concurrent pregnancies are allowed by the colony
global NEWGEN_PERIOD # regularise cohorts of newborns to the colony (e.g. if colony only allows offspring every 3 years, for easier control?)
global NEWGEN_WINDOW # no. of days within which new pregnancies can be started each NEWGEN_PERIOD

global pregCounter

SHIP_CAPACITY = 80
TRAVEL_TIME = 200 
COOLDOWN = 365
MAX_PREGNANCIES = 100
NEWGEN_PERIOD = 365 * 6
NEWGEN_WINDOW = 30

pregCounter = 0

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
        self.cooldown = COOLDOWN
        
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
        
        
def toDays(years):
    return years * 365

def toYears(days):
    return days//365

def checkProb(prob):
    return random.random() < prob

def landing():
    crew = []
    global SHIP_CAPACITY
    for x in range(0, SHIP_CAPACITY//2):
        a = Astronaut("m")
        b = Astronaut("f")
        crew.append(a)
        crew.append(b)
    
    return crew

colony = []
sizes = []

RUN = 365 * 50
days = range(0, RUN)

for day in days:
    if (day % (26*30) == 0):
        colony = colony + landing()
            
    new_colonists = []
    for x in colony:
        # increase age of everybody by 1
        if (day % 365 == 0 and day > 0):
            x.incAge()
        
        # check dead
        if (x.getAge() > 55):
            
            # https://www.desmos.com/calculator/8keivyyfqk
            k = 1/25 #  vertical strech of function - larger denominator = larger strech
            a = 95 # translation at which prob = 1
            prob = np.log(k*(x.getAge()-a) + np.e)
            if checkProb(prob):
                x.setDead()
        
        # model infant death?
        
        #check if new generation is due
        newgen = (day % NEWGEN_PERIOD < NEWGEN_WINDOW)
        
        # check for pregnancies
        if (x.getSex() == "f" and x.getAge() < 50 and x.getAge() > 30):
            
            # if 260 days have passed, check if a new colonist is born (logarithmic probabilty, see graph)
            #https://www.desmos.com/calculator/1jpwftgju8
            if (x.getPregnant() >= 260):
                k = 1/35 #  vertical strech of function - larger denominator = larger strech
                a = 295 # translation at which prob = 1
                prob = np.log(k*(x.getPregnant()-a) + np.e)
                if checkProb(prob):
                    x.birth()
                    pregCounter = pregCounter - 1
                    new = Martian()
                    new_colonists = new_colonists + [new]             
            elif (x.getCooldown() == 0):
                if (x.getPregnant() != -1):
                    x.incPregnant()                
                elif (x.getPregnant() == -1):
                    if (newgen and pregCounter < MAX_PREGNANCIES):
                        x.startPregnant()
                        pregCounter = pregCounter + 1
            else:
                x.decCooldown()
            
    # remove dead
    colony[:] = [x for x in colony if not x.isDead()]
        
        
    colony = colony + new_colonists
    sizes = sizes + [len(colony)]


plt.plot(days, sizes)
plt.show()


for x in colony:
    print(x.getAge(), x.getSex(), x.getName())
    
print(max(sizes))
'''
x = Astronaut("m")
y = Astronaut("f")

a = Martian()
b = Martian()
c = Martian()

print(x.getAge(), x.getSex(), x.getName())
print(y.getAge(), y.getSex(), y.getName())
print(a.getAge(), a.getSex(), a.isChild(), a.getName())
print(b.getAge(), b.getSex(), b.isChild(), b.getName())
print(c.getAge(), c.getSex(), c.isChild(), c.getName())
'''