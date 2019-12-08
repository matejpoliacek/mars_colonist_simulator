# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 17:28:00 2019

@author: matej
"""

# Module storing all the constants used in the simulation
# This is the central place to tune the numbers to achieve the desired simulation behaivour


'''
global SIM_LENGTH # number of days for which the simulation runs

global SHIP_CAPACITY # how many astronauts come with every transit
global ARRIVAL_TIMES_ONEOFF  # when one-off arrivals reach Mars
global ARRIVAL_TIMES_REGULAR  # when regular arrivals reach Mars
global CREW_RATIO   # male to female ratio of crew

global DEATH_THRESH # age (years) after which the simulation starts checking for natural death  

global COOLDOWN  # how long between two pregnancies by a colonist
global MAX_PREG # maximum concurrent pregnancies are allowed by the colony
global NEWGEN_PERIOD # regularise cohorts of newborns to the colony (e.g. if colony only allows offspring every 3 years, for easier control?)
global NEWGEN_WINDOW # no. of days within which new pregnancies can be started each NEWGEN_PERIOD
global PREG_THRESH # days after which the simulation starts checking if birth has taken place or not
global PREG_AGE_MAX # maximum childbearing age 
global PREG_AGE_MIN # minimum childbearing age 

global START_POP # population at the start of the simulation
global TARGET_POP # population to be reached
global ASTRO_MIN_AGE # minimum age of arriving astronauts
global ASTRO_MAX_AGE # maximumx age of arriving astronauts

global COLONIST_DEPENDENT_AGE # age until which the colonist requires care
global COLONIST_PRODUCTIVE_AGE # age from which the colonist is productive
global COLONIST_ELDERLY_AGE # age from which the colonist is considered elderly

global COLONIST_DEPENDENT_WORK # hours of work provided/consumed by dependent colonist
global COLONIST_NONPROD_WORK # hours of work provided/consumed by non productive colonist
global COLONIST_PRODUCTIVE_WORK # hours of work provided/consumed by productive colonist
global COLONIST_ELDERLY_WORK # hours of work provided/consumed by elderly colonist
'''      
    
# Class holding all the parameters
class Sim_params:
    
    #defaults
    
    def __init__(self):
        self.SHIP_CAPACITY = 80
        self.ARRIVAL_TIMES_ONEOFF = [] 
        self.ARRIVAL_TIMES_REGULAR = [] 
        self.CREW_RATIO = 1.0
        self.COOLDOWN = 365
        self.MAX_PREG = 100
        self.NEWGEN_PERIOD = 365 * 6
        self.NEWGEN_WINDOW = 30
        self.SIM_LENGTH = 365 * 30
        self.PREG_THRESH = 8 * 30 #fix
        self.DEATH_THRESH = 55
        self.PREG_AGE_MAX = 50
        self.PREG_AGE_MIN = 30
        self.START_POP = 0
        self.TARGET_POP = 0
        self.ASTRO_MIN_AGE = 25
        self.ASTRO_MAX_AGE = 45
        self.COLONIST_DEPENDENT_AGE = 3
        self.COLONIST_PRODUCTIVE_AGE = 16
        self.COLONIST_ELDERLY_AGE = 65
        self.COLONIST_DEPENDENT_WORK = -16
        self.COLONIST_NONPROD_WORK = 0
        self.COLONIST_PRODUCTIVE_WORK = 16
        self.COLONIST_ELDERLY_WORK = 4
        
    #getters
    
    def getSHIP_CAPACITY(self):
        return self.SHIP_CAPACITY
        
    def getARRIVAL_TIMES_ONEOFF(self):
        return self.ARRIVAL_TIMES_ONEOFF
        
    def getARRIVAL_TIMES_ONEOFF_asString(self):
        str_list = []
        for item in self.ARRIVAL_TIMES_ONEOFF:
            str_list.append("Day " + str(item))
            
        return str_list
    
    def getARRIVAL_TIMES_REGULAR(self):
        return self.ARRIVAL_TIMES_REGULAR
        
    def getARRIVAL_TIMES_REGULAR_asString(self):
        str_list = []
        for item in self.ARRIVAL_TIMES_REGULAR:
            str_list.append("Every " + str(item) + " days")
            
        return str_list    
    
    def getCREW_RATIO(self):
        return self.CREW_RATIO
    
    def getCOOLDOWN(self):
        return self.COOLDOWN
        
    def getMAX_PREG(self):
        return self.MAX_PREG
    
    def getNEWGEN_PERIOD(self):
        return self.NEWGEN_PERIOD
        
    def getNEWGEN_WINDOW(self):
        return self.NEWGEN_WINDOW
     
    def getSIM_LENGTH(self):
        return self.SIM_LENGTH
        
    def getPREG_THRESH(self):
        return self.PREG_THRESH
        
    def getDEATH_THRESH(self):
        return self.DEATH_THRESH
        
    def getPREG_AGE_MAX(self):
        return self.PREG_AGE_MAX
        
    def getPREG_AGE_MIN(self):
        return self.PREG_AGE_MIN
    
    def getSTART_POP(self):
        return self.START_POP
    
    def getTARGET_POP(self):
        return self.TARGET_POP
    
    def getASTRO_MIN_AGE(self):
        return self.ASTRO_MIN_AGE
        
    def getASTRO_MAX_AGE(self):
        return self.ASTRO_MAX_AGE
    
    def getCOLONIST_DEPENDENT_AGE(self):
        return self.COLONIST_DEPENDENT_AGE
        
    def getCOLONIST_PRODUCTIVE_AGE(self):
        return self.COLONIST_PRODUCTIVE_AGE
        
    def getCOLONIST_ELDERLY_AGE(self):
        return self.COLONIST_ELDERLY_AGE
        
    def getCOLONIST_DEPENDENT_WORK(self):
        return self.COLONIST_DEPENDENT_WORK
        
    def getCOLONIST_NONPROD_WORK(self):
        return self.COLONIST_NONPROD_WORK
        
    def getCOLONIST_PRODUCTIVE_WORK(self):
        return self.COLONIST_PRODUCTIVE_WORK
        
    def getCOLONIST_ELDERLY_WORK(self):
        return self.COLONIST_ELDERLY_WORK
            
    # setters
    
    def setSHIP_CAPACITY(self, cap):
        self.SHIP_CAPACITY = cap
        
    def setARRIVAL_TIMES_ONEOFF(self, arrivals):
        self.ARRIVAL_TIMES_ONEOFF = arrivals

    def addARRIVAL_TIMES_ONEOFF(self, time):
        self.ARRIVAL_TIMES_ONEOFF.append(time)
        self.ARRIVAL_TIMES_ONEOFF.sort()
        
    def removeARRIVAL_TIMES_ONEOFF(self, time):
        try:
            self.ARRIVAL_TIMES_ONEOFF.remove(time)
        except ValueError:
            pass
            
    def setARRIVAL_TIMES_REGULAR(self, arrivals):
        self.ARRIVAL_TIMES_REGULAR = arrivals

    def addARRIVAL_TIMES_REGULAR(self, time):
        if not time in self.ARRIVAL_TIMES_REGULAR:
            self.ARRIVAL_TIMES_REGULAR.append(time)
            self.ARRIVAL_TIMES_REGULAR.sort()
        
    def removeARRIVAL_TIMES_REGULAR(self, time):
        try:
            self.ARRIVAL_TIMES_REGULAR.remove(time)
        except ValueError:
            pass

    def setCREW_RATIO(self, ratio):
        self.CREW_RATIO = ratio
    
    def setCOOLDOWN(self, cool):
        self.COOLDOWN = cool
        
    def setMAX_PREG(self, maxp):
        self.MAX_PREG = maxp
    
    def setNEWGEN_PERIOD(self, period):
        self.NEWGEN_PERIOD = period
        
    def setNEWGEN_WINDOW(self, window):
        self.NEWGEN_WINDOW = window
     
    def setSIM_LENGTH(self, length):
        self.SIM_LENGTH = length
        
    def setPREG_THRESH(self, pregthresh):
        self.PREG_THRESH = pregthresh
        
    def setDEATH_THRESH(self, deaththresh):
        self.DEATH_THRESH = deaththresh
        
    def setPREG_AGE_MAX(self, agemax):
        self.PREG_AGE_MAX = agemax
        
    def setPREG_AGE_MIN(self, agemin):
        self.PREG_AGE_MIN = agemin

    def setSTART_POP(self, startPop):
        self.START_POP = startPop
        
    def setTARGET_POP(self, targetPop):
        self.TARGET_POP = targetPop
        
    def setASTRO_MIN_AGE(self, minage):
        self.ASTRO_MIN_AGE = minage
        
    def setASTRO_MAX_AGE(self, maxage):
        self.ASTRO_MAX_AGE = maxage