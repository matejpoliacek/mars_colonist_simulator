# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:20:52 2019

@author: matej
"""

import matplotlib.pyplot as plt
import numpy as np

import mars_constants as MC
import colonists as col


global pregCounter

pregCounter = 0

def landing():
    crew = []
    for x in range(0, MC.SHIP_CAPACITY//2):
        a = col.Astronaut("m")
        b = col.Astronaut("f")
        crew.append(a)
        crew.append(b)
    
    return crew

colony = []
sizes = []

days = range(0, MC.SIM_LENGTH)

for day in days:
    if (day % (26*30) == 0):
        colony = colony + landing()
            
    new_colonists = []
    for x in colony:
        # increase age of everybody by 1
        if (day % 365 == 0 and day > 0):
            x.incAge()
        
        # check dead
        if (x.getAge() > MC.DEATH_THRESH):
            if MC.checkDeathProb(x.getAge()):
                x.setDead()
        
        # model infant death?
        
        #check if new generation is due
        newgen = (day % MC.NEWGEN_PERIOD < MC.NEWGEN_WINDOW)
        
        # check for pregnancies
        if (x.getSex() == "f" and x.getAge() < 50 and x.getAge() > 30):
            
            # if 260 days have passed, check if a new colonist is born (logarithmic probabilty, see graph)
            if (x.getPregnant() >= MC.PREG_THRESH):
                if MC.checkBirthProb(x.getPregnant()):
                    x.birth()
                    pregCounter = pregCounter - 1
                    new = col.Martian()
                    new_colonists = new_colonists + [new]             
            elif (x.getCooldown() == 0):
                if (x.getPregnant() != -1):
                    x.incPregnant()                
                elif (x.getPregnant() == -1):
                    if (newgen and pregCounter < MC.MAX_PREGNANCIES):
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