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
global TRAVEL_TIME  # how many days between arrivals
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
'''      
    
# Class holding all the parameters
class Sim_params:
    
    #defaults
    
    def __init__(self):
        self.SHIP_CAPACITY = 80
        self.TRAVEL_TIME = 200 
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
    #getters
    
    def getSHIP_CAPACITY(self):
        return self.SHIP_CAPACITY
        
    def getTRAVEL_TIME(self):
        return self.TRAVEL_TIME
    
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
    
    # setters
    
    def setSHIP_CAPACITY(self, cap):
        self.SHIP_CAPACITY = cap
        
    def setTRAVEL_TIME(self, time):
        self.TRAVEL_TIME = time
        
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