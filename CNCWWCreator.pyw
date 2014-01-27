# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:02:18 2014

@author: Dirk Van Essendelft
"""

import sys, os, csv, json
from PyQt4 import QtGui, QtCore
from main import Ui_MainWindow
from utilities import utilities
from machineSettings import machineSettingsDialog
from gridSettings import gridSettingsDialog
from prepostambel import prePostAmbleDialog
from moduleBase import moduleBase


class CNCWWCreator(QtGui.QMainWindow):
    '''
    The is the main program class
    '''
    def __init__(self,parent=None):
        util = utilities(self)
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.vars = globalVars()
        self.connectActions()
        self.vars.machineSettings = util.getSettings('machineSettings.txt')
        self.vars.gridSettings = util.getSettings('gridSettings.txt')
        self.vars.moduleList = []
        for i in range(1000):
            mName = str(self.ui.moduleTabWidget.tabText(i))
            if mName == '':
                break
            else:
                self.vars.moduleList.append(mName.replace(' ',''))
        for mod in self.vars.moduleList:
            cmd = 'self.'+mod+' = moduleBase("'+mod+'",parent = self)'
            exec(cmd)
        
    def connectActions(self):
        """
        Connect the user interface controls to the logic
        """
        self.ui.actionMachine.triggered.connect(self.machineSettinsDialog)
        self.ui.actionGrid.triggered.connect(self.gridSettinsDialog)
        self.ui.actionExit.triggered.connect(self.mainQuit)
        self.ui.generateGCodePushButton.clicked.connect(self.onGenerateGCodePressed)
        self.ui.actionPostamble.triggered.connect(self.postDialog)
        self.ui.actionPreamble.triggered.connect(self.preDialog)
        
    def machineSettinsDialog(self):
        '''
        enstantiates an instance of the machine settings dialog and calls the gui
        '''
        machineSettings = machineSettingsDialog(parent = self)
        machineSettings.exec_()
        
    def gridSettinsDialog(self):
        '''
        enstantiates an instance of the grid settings dialog and calls the gui
        '''
        gridSettings = gridSettingsDialog(parent = self)
        gridSettings.exec_()
        
    def postDialog(self):
        '''
        enstantiates an instance of the prepost dialog and calls the gui
        '''
        prePostDialog = prePostAmbleDialog("Postamble",parent = self)
        prePostDialog.exec_()
        
    def preDialog(self):
        '''
        enstantiates an instance of the prepost dialog and calls the gui
        '''
        prePostDialog = prePostAmbleDialog("Preamble",parent = self)
        prePostDialog.exec_()
        
    def mainQuit(self):
        '''
        handles actions on exit
        '''
        pass
    
    def onGenerateGCodePressed(self):
        '''
        reads the current module, commands it to save the entries and then produce
        g-code
        '''
        currentModuleIndex = self.ui.moduleTabWidget.currentIndex()
        currentModule = str(self.ui.moduleTabWidget.tabText(currentModuleIndex)).replace(' ','')
        cmd = 'self.'+currentModule+'.saveModuleEntries()'
        exec(cmd)
        cmd = 'self.'+currentModule+'.produceGCode()'
        exec(cmd)
            
            
class globalVars():
    '''
    This is a dummy class to hold vars separate from other vars and functions
    '''
    def __init__(self,parent=None):
        self.parent = parent
        

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    mainapp = CNCWWCreator()
    mainapp.show()
    sys.exit(app.exec_())
