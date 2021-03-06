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

def simulation(params, label, colony, sizes, crewhrs_list, startDay):
    
    pregCounter = 0
    day = startDay
    
    while True:
        
        # initial crew
        if (day == 0):
            colony = colony + arrivalFromEarth(params)
        
        # regular arrivals
        if (len(params.getARRIVAL_TIMES_REGULAR()) > 0):
            for item in params.getARRIVAL_TIMES_REGULAR():
                if (day % item == 0):
                    colony = colony + arrivalFromEarth(params)
        
        # one-off arrivals
        if (len(params.getARRIVAL_TIMES_ONEOFF()) > 0):
            noArrivals = params.getARRIVAL_TIMES_ONEOFF().count(day)
            if (noArrivals > 0):
                colony = colony + arrivalFromEarth(params)*noArrivals
                
        new_colonists = []
        crewhours = 0
        for x in colony:
            # increase age of everybody by 1 day
            x.incAgeDay()
            
            # check dead
            if (x.getAge() > params.getDEATH_THRESH()):
                if util.checkDeathProb(x.getAge()):
                    # THIS IS NOW CHECKING EVERY DAY AFTER DEATH_THRESH BIRTHDAY, LEADS TO EARLY DEATHS
                    x.setDead()
            
            # model infant death?
            
            #check if new generation is due
            try:
                newgen = (day % params.getNEWGEN_PERIOD() < params.getNEWGEN_WINDOW())
            except:
                # catch division by 0, in which case the pregnancies are unregulated
                if (params.getNEWGEN_PERIOD() == 0):
                    newgen = True
                else:
                    # never here
                    newgen = False
                    print("Warning: newgen false in except?")
            
            # check for pregnancies
            if (x.getSex() == "f" and x.getAge() < params.getPREG_AGE_MAX() and x.getAge() > params.getPREG_AGE_MIN()):
                
                # if PREG_THRESHOLD days have passed, check if a new colonist is born
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
                
            # sum crewhours of work
            crewhours = crewhours + x.getWorkHours()
                
        # remove dead
        colony[:] = [x for x in colony if not x.isDead()]
            
            
        colony = colony + new_colonists
        sizes = sizes + [len(colony)]
        crewhrs_list = crewhrs_list + [crewhours]
        
        # if specify sim length
        label.setText("Progress: " + str(day+1-startDay) + " of " + str(params.getSIM_LENGTH()))
        # else
        # label.setText("Progress: " + str(day)))
        
        day = day + 1
        if (day >= startDay + params.getSIM_LENGTH()): # AND specify sim length
            break
            
        # if specify target pop AND target len(colony) >= params.getTARGET_POP():
        #   break
        
    for x in colony:
        print(x.getAge(), x.getSex(), x.getName())
        
    print(max(sizes))
    
    return colony, sizes, crewhrs_list
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