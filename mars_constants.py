# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 17:28:00 2019

@author: matej
"""

# Module storing all the constants used in the simulation
# This is the central place to tune the numbers to achieve the desired simulation behaivour

import random
import numpy as np

global SHIP_CAPACITY # how many astronauts come every 2 years from earth
global TRAVEL_TIME  # travel time from Earth to Mars (unused for now)
global COOLDOW  # how long betweeen maximum allowed pregnancies by a colonist
global MAX_PREGNANCIES # maximum concurrent pregnancies are allowed by the colony
global NEWGEN_PERIOD # regularise cohorts of newborns to the colony (e.g. if colony only allows offspring every 3 years, for easier control?)
global NEWGEN_WINDOW # no. of days within which new pregnancies can be started each NEWGEN_PERIOD
global PREG_THRESH # days after which the simulation starts checking if birth has taken place or not
global DEATH_THRESH # age (years) after which the simulation starts checking for natural death

SHIP_CAPACITY = 80
TRAVEL_TIME = 200 
COOLDOWN = 365
MAX_PREGNANCIES = 100
NEWGEN_PERIOD = 365 * 6
NEWGEN_WINDOW = 30
SIM_LENGTH = 365 * 30
DEATH_THRESH = 55

# Functions used to calculate probabilities
def checkDeathProb(age):
    
    # See the shape of the function here (logarithmic):
    # https://www.desmos.com/calculator/8keivyyfqk
    k = 1/25 #  vertical strech of function - larger denominator = larger strech
    a = 95 # translation - x at which probability = 1
    prob = np.log(k*(age-a) + np.e)
    
    # draw a random decimal between 0 and 1
    # return true if smaller than the resulting probability
    return random.random() < prob

def checkBirthProb(preg):
    
    # See the shape of the function here (logarithmic):
    #https://www.desmos.com/calculator/1jpwftgju8
    k = 1/35 #  vertical strech of function - larger denominator = larger strech
    a = 295 # translation - x at which probability = 1
    prob = np.log(k*(preg-a) + np.e)
    
    # draw a random decimal between 0 and 1
    # return true if smaller than the resulting probability
    return random.random() < prob