from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys
import threading

import matplotlib.pyplot as plt

import simulation as sim
import colonysim_params as ps
import colony_util as util

global params
params = ps.Sim_params()

global final_list
final_list = []
global col_sizes
col_sizes = []
global crewhrs_list
crewhrs_list = []
global elapsed_days
elapsed_days = 0

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(MainWindow,self).__init__()

        self.ui = uic.loadUi('colonysim.ui',self)
    
        self.onlyInt = QIntValidator()
        self.onlyDouble = QDoubleValidator()
    
        #Pre-fill lineEdits with defaults
        self.ui.lineEdit_simLength.setText(str(params.getSIM_LENGTH()))
        self.ui.lineEdit_capacity.setText(str(params.getSHIP_CAPACITY()))
        self.ui.lineEdit_arrival.setText(str(params.getTRAVEL_TIME()))
        self.ui.lineEdit_crewRatio.setText(str(params.getCREW_RATIO()))
        self.ui.lineEdit_deathThresh.setText(str(params.getDEATH_THRESH()))
        self.ui.lineEdit_cooldown.setText(str(params.getCOOLDOWN()))
        self.ui.lineEdit_maxPreg.setText(str(params.getMAX_PREG()))
        self.ui.lineEdit_newGenPeriod.setText(str(params.getNEWGEN_PERIOD()))
        self.ui.lineEdit_newGenWindow.setText(str(params.getNEWGEN_WINDOW()))
        self.ui.lineEdit_pregThresh.setText(str(params.getPREG_THRESH()))
        self.ui.lineEdit_reproMinAge.setText(str(params.getPREG_AGE_MIN()))
        self.ui.lineEdit_reproMaxAge.setText(str(params.getPREG_AGE_MAX()))
        self.ui.lineEdit_AstroMinAge.setText(str(params.getASTRO_MIN_AGE()))
        self.ui.lineEdit_AstroMaxAge.setText(str(params.getASTRO_MAX_AGE()))
        
        # Set Validators
        self.ui.lineEdit_simLength.setValidator(self.onlyInt)
        self.ui.lineEdit_capacity.setValidator(self.onlyInt)
        self.ui.lineEdit_arrival.setValidator(self.onlyInt)
        self.ui.lineEdit_deathThresh.setValidator(self.onlyInt)
        self.ui.lineEdit_cooldown.setValidator(self.onlyInt)
        self.ui.lineEdit_maxPreg.setValidator(self.onlyInt)
        self.ui.lineEdit_newGenPeriod.setValidator(self.onlyInt)
        self.ui.lineEdit_newGenWindow.setValidator(self.onlyInt)
        self.ui.lineEdit_pregThresh.setValidator(self.onlyInt)
        self.ui.lineEdit_reproMinAge.setValidator(self.onlyInt)
        self.ui.lineEdit_reproMaxAge.setValidator(self.onlyInt)
        self.ui.lineEdit_AstroMinAge.setValidator(self.onlyInt)
        self.ui.lineEdit_AstroMaxAge.setValidator(self.onlyInt)
        
        self.ui.lineEdit_crewRatio.setValidator(self.onlyDouble)
        
        # Text change functions
        self.calcYears()
        self.showCrewRatios()
        self.ui.lineEdit_simLength.textChanged.connect(self.calcYears)
        self.ui.lineEdit_capacity.textChanged.connect(self.showCrewRatios)
        self.ui.lineEdit_crewRatio.textChanged.connect(self.showCrewRatios)
        self.ui.lineEdit_AstroMinAge.textChanged.connect(self.editMinAstronautAge)
        self.ui.lineEdit_AstroMaxAge.textChanged.connect(self.editMaxAstronautAge)
        
        # Button functions
        self.ui.pushButtonStart.clicked.connect(self.pushButtonStartClicked)
        self.ui.pushButtonHelp.clicked.connect(self.pushButtonHelpClicked)
        self.ui.pushButtonReset.clicked.connect(self.pushButtonResetClicked)
        
        # TODO: RadioButton fuctions
        
    def set_params(self):
        params.setSIM_LENGTH(int(self.ui.lineEdit_simLength.text()))
        params.setSHIP_CAPACITY(int(self.ui.lineEdit_capacity.text()))
        params.setTRAVEL_TIME(int(self.ui.lineEdit_arrival.text()))
        params.setDEATH_THRESH(int(self.ui.lineEdit_deathThresh.text()))
        params.setCOOLDOWN(int(self.ui.lineEdit_cooldown.text()))
        params.setMAX_PREG(int(self.ui.lineEdit_maxPreg.text()))
        params.setNEWGEN_PERIOD(int(self.ui.lineEdit_newGenPeriod.text()))
        params.setNEWGEN_WINDOW(int(self.ui.lineEdit_newGenWindow.text()))
        params.setPREG_THRESH(int(self.ui.lineEdit_pregThresh.text()))
        params.setPREG_AGE_MIN(int(self.ui.lineEdit_reproMinAge.text()))
        params.setPREG_AGE_MAX(int(self.ui.lineEdit_reproMaxAge.text()))
        params.setASTRO_MIN_AGE(int(self.ui.lineEdit_AstroMinAge.text()))
        params.setASTRO_MAX_AGE(int(self.ui.lineEdit_AstroMaxAge.text()))
        
    def plot_thread(self):
        
        global col_sizes
        global crewhrs_list
        global elapsed_days
                    
        xaxis = range(0, elapsed_days)        
        
        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.suptitle('Settlement Size and Productivity')
        ax1.plot(xaxis, col_sizes)
        ax1.set_title('Population')
        ax2.plot(xaxis, crewhrs_list, 'tab:orange')
        ax2.set_title('Productivity')
        
        plt.show()
    
    def simulation_thread(self):
            self.ui.pushButtonStart.setEnabled(False)
            self.ui.listFinalPop.clear()
            
            self.set_params()
            
            global final_list
            global col_sizes
            global crewhrs_list
            global elapsed_days
            
            initSize = len(final_list)
            
            final_list, col_sizes, crewhrs_list = sim.simulation(params, self.ui.label_progress, final_list, col_sizes, crewhrs_list, elapsed_days)
            
            finalSize = len(final_list)
            
            for x in final_list:
                colonistString = str(x.getAge())+" "+str(x.getSex())+", "+str(x.getName())
                self.ui.listFinalPop.addItem(colonistString)
                # TODO: parse colonist string to file
            
            start = elapsed_days
            elapsed_days = elapsed_days + params.getSIM_LENGTH()
            
            self.ui.listSimStages.addItem("D"+str(start)+", "+str(initSize)+" colonists -> "+str(params.getSIM_LENGTH())+" DAYS -> "+"D"+str(elapsed_days)+", "+str(finalSize) + " colonists")
            #print(len(final_list), len(col_sizes))
            self.ui.pushButtonStart.setEnabled(True)
            
            plotTh = threading.Thread(target=self.plot_thread, args=[])
            plotTh.start()
        
    
    def pushButtonStartClicked(self):
    
        th = threading.Thread(target=self.simulation_thread, args=[])
        th.start()
    
    def pushButtonHelpClicked(self):
        
        help_window = HelpWindow()
        help_window.show() 
        # TODO: prevent multiple help windows open at once
    
    def pushButtonResetClicked(self):
        
        global final_list
        global col_sizes
        global elapsed_days
        global crewhrs_list

        final_list = []
        col_sizes = []
        crewhrs_list = []
        elapsed_days = 0
        
        self.ui.listFinalPop.clear()
        self.ui.listSimStages.clear()
        
    def calcYears(self):
        text = self.ui.lineEdit_simLength.text()
        
        if text:
            yrs = int(text)/365.0
            self.ui.label_simYears.setText("= " + str(round(yrs, 2)) + " years")
        else: 
            self.ui.label_simYears.setText("= N/A")
            
    def showCrewRatios(self):
        capacity = self.ui.lineEdit_capacity.text()
        ratio = self.ui.lineEdit_crewRatio.text()
        
        if ratio and capacity:
            male_crew,female_crew = util.ratioCalculator(int(capacity), float(ratio))
            self.ui.label_crewRatioDisplay.setText("= " + str(round(male_crew, 2)) + " M, " + str(round(female_crew, 2)) + " F crew members")
        else: 
            self.ui.label_crewRatioDisplay.setText("= N/A, set ratio")

    def editMinAstronautAge(self):
        
        min = self.ui.lineEdit_AstroMinAge
        max = self.ui.lineEdit_AstroMaxAge
        
        # TODO this should happen on focus out
        
        if int(min.text()) < 0:
            min.setText("0")
        
        if int(min.text()) > int(max.text()):
            min.setText(max.text())

    def editMaxAstronautAge(self):
        
        min = self.ui.lineEdit_AstroMinAge
        max = self.ui.lineEdit_AstroMaxAge
        
        # TODO this should happen on focus out
        
        if int(max.text()) < 0:
            max.setText("0")
        
        if int(max.text()) < int(min.text()):
            max.setText(min.text())
                
    
class HelpWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(HelpWindow,self).__init__()

        self.ui = uic.loadUi('colony_help.ui',self)
            
if __name__== '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show() 

    sys.exit(app.exec_())
