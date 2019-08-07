from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys
import threading

import matplotlib.pyplot as plt

import simulation as sim
import colonysim_params as ps

global params
params = ps.Sim_params()

global final_list
global col_sizes

class MyWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(MyWindow,self).__init__()

        self.ui = uic.loadUi('colonysim.ui',self)
    
        #Pre-fill lineEdits with defaults
        self.ui.lineEdit_simLength.setText(str(params.getSIM_LENGTH()))
        self.ui.lineEdit_capacity.setText(str(params.getSHIP_CAPACITY()))
        self.ui.lineEdit_transit.setText(str(params.getTRAVEL_TIME()))
        self.ui.lineEdit_deathThresh.setText(str(params.getDEATH_THRESH()))
        self.ui.lineEdit_cooldown.setText(str(params.getCOOLDOWN()))
        self.ui.lineEdit_maxPreg.setText(str(params.getMAX_PREG()))
        self.ui.lineEdit_newGenPeriod.setText(str(params.getNEWGEN_PERIOD()))
        self.ui.lineEdit_newGenWindow.setText(str(params.getNEWGEN_WINDOW()))
        self.ui.lineEdit_pregThresh.setText(str(params.getPREG_THRESH()))
        self.ui.lineEdit_reproMinAge.setText(str(params.getPREG_AGE_MIN()))
        self.ui.lineEdit_reproMaxAge.setText(str(params.getPREG_AGE_MAX()))
        
        # Text change functions
        self.calcYears()
        self.ui.lineEdit_simLength.textChanged.connect(self.calcYears)
        
        # Button functions
        self.ui.pushButtonStart.clicked.connect(self.pushButtonStartClicked)
        
    def set_params(self):
        params.setSIM_LENGTH(int(self.ui.lineEdit_simLength.text()))
        params.setSHIP_CAPACITY(int(self.ui.lineEdit_capacity.text()))
        params.setTRAVEL_TIME(int(self.ui.lineEdit_transit.text()))
        params.setDEATH_THRESH(int(self.ui.lineEdit_deathThresh.text()))
        params.setCOOLDOWN(int(self.ui.lineEdit_cooldown.text()))
        params.setMAX_PREG(int(self.ui.lineEdit_maxPreg.text()))
        params.setNEWGEN_PERIOD(int(self.ui.lineEdit_newGenPeriod.text()))
        params.setNEWGEN_WINDOW(int(self.ui.lineEdit_newGenWindow.text()))
        params.setPREG_THRESH(int(self.ui.lineEdit_pregThresh.text()))
        params.setPREG_AGE_MIN(int(self.ui.lineEdit_reproMinAge.text()))
        params.setPREG_AGE_MAX(int(self.ui.lineEdit_reproMaxAge.text()))
    
    def plot_thread(self):
        plt.plot(range(0, params.getSIM_LENGTH()), col_sizes)
        #plt.ion()
        plt.show()
        #plt.pause(0.001)
    
    def simulation_thread(self):
            self.ui.pushButtonStart.setEnabled(False)
            self.ui.listFinalPop.clear()
            
            self.set_params()
            
            global final_list
            global col_sizes
            final_list, col_sizes = sim.simulation(params, self.ui.label_progress)
            
            for x in final_list:
                self.ui.listFinalPop.addItem(str(x.getAge())+" "+str(x.getSex())+", "+str(x.getName()))
            self.ui.pushButtonStart.setEnabled(True)
            
            plotTh = threading.Thread(target=self.plot_thread, args=[])
            plotTh.start()
        
    
    def pushButtonStartClicked(self):
    
        th = threading.Thread(target=self.simulation_thread, args=[])
        th.start()
        
    def calcYears(self):
        text = self.ui.lineEdit_simLength.text()
        
        if text:
            yrs = int(text)/365.0
            self.ui.label_simYears.setText("= " + str(round(yrs, 2)) + " years")
        else: 
            self.ui.label_simYears.setText("= N/A")
        
if __name__== '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show() 

    sys.exit(app.exec_())
