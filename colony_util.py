import random
import numpy as np


# Functions used to calculate probabilities
def checkDeathProb(age):
    
    # See the shape of the function here (explonential):
    # https://www.desmos.com/calculator/8keivyyfqk
    MAX_AGE = 100 # this age is never exceeded, as probablity of death == 1, TODO: make an adjustable parameter?
    THRESH = 55 # #TODO:replace with DEATH_THRESHOLD
    k = (MAX_AGE - THRESH)^2 
    # TODO: tie function to DEATH_THRESHOLD
    prob = ((age - THRESH)^2) / MAX_AGE
    
    # draw a random decimal between 0 and 1
    # return true if smaller than the resulting probability
    rand = random.random()
    result = rand < prob
    #print("DEATH", result, rand, prob)
    return result

def checkBirthProb(preg):
    
    # See the shape of the function here (logarithmic):
    #https://www.desmos.com/calculator/1jpwftgju8
    k = 1/35
    a = 295 # translation - x at which probability = 1
    # TODO: tie function to PREG_THRESHOLD
    prob = np.log(k*(preg-a) + np.e)
    
    # draw a random decimal between 0 and 1
    # return true if smaller than the resulting probability
    rand = random.random()
    result = rand < prob
    #print("PREG", result, rand, prob)
    return result
    
def ratioCalculator(capacity, ratio):

    male_crew = int((ratio/(ratio + 1)) * capacity)
    female_crew = capacity - male_crew
    
    return male_crew, female_crew
