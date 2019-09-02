# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:20:52 2019

@author: matej
"""

import numpy as np

import colony_util as util
import colonists as col



# TODO: move to colony_utils.py
def arrivalFromEarth(params):
    crew = []
    
    male_crew,female_crew = util.ratioCalculator(params.getSHIP_CAPACITY(), params.getCREW_RATIO())
    
    for x in range(0, male_crew):
        a = col.Astronaut("m", params)
        crew.append(a)
    
    for y in range(0, female_crew):
        a = col.Astronaut("f", params)
        crew.append(a)

    return crew

def simulation(params, label):
    colony = []
    sizes = []
    pregCounter = 0

    days = range(0, params.getSIM_LENGTH())

    for day in days:
        if (day % (26*30) == 0):
            colony = colony + arrivalFromEarth(params)
                
        new_colonists = []
        for x in colony:
            # increase age of everybody by 1
            if (day % 365 == 0 and day > 0):
                x.incAge()
            
            # check dead
            if (x.getAge() > params.getDEATH_THRESH()):
                if util.checkDeathProb(x.getAge()):
                    x.setDead()
            
            # model infant death?
            
            #check if new generation is due
            newgen = (day % params.getNEWGEN_PERIOD() < params.getNEWGEN_WINDOW())
            
            # check for pregnancies
            if (x.getSex() == "f" and x.getAge() < params.getPREG_AGE_MAX() and x.getAge() > params.getPREG_AGE_MIN()):
                
                # if 260 days have passed, check if a new colonist is born (logarithmic probabilty, see graph)
                if (x.getPregnant() >= params.getPREG_THRESH()):
                    if util.checkBirthProb(x.getPregnant()):
                        x.birth()
                        pregCounter = pregCounter - 1
                        new = col.Martian(params)
                        new_colonists = new_colonists + [new]             
                elif (x.getCooldown() == 0):
                    if (x.getPregnant() != -1):
                        x.incPregnant()                
                    elif (x.getPregnant() == -1):
                        if (newgen and (pregCounter < params.getMAX_PREG() or params.getMAX_PREG() == -1)):
                            x.startPregnant()
                            pregCounter = pregCounter + 1
                else:
                    x.decCooldown()
                
        # remove dead
        colony[:] = [x for x in colony if not x.isDead()]
            
            
        colony = colony + new_colonists
        sizes = sizes + [len(colony)]
        
        label.setText("Progress: " + str(day+1) + " of " + str(max(days)+1))

    for x in colony:
        print(x.getAge(), x.getSex(), x.getName())
        
    print(max(sizes))
    
    return colony, sizes
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