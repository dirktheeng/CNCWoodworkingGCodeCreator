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
from prepostamble import prePostAmbleDialog
from setOriginFromGrid import setOriginFromGridDialog
from moduleBase import moduleBase


class CNCWWCreator(QtGui.QMainWindow):
    '''
    The is the main program class
    '''
    def __init__(self,parent=None):
        self.util = utilities(parent = self)
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connectActions()
        self._defaultGCodeDirectory = self.util.readDefaultGCodeDirectory()
        self._machineSettings = self.util.getSettings('machineSettings.txt')
        self._gridSettings = self.util.getSettings('gridSettings.txt')
        self._moduleList = []
        self._origin = [0,0]
        self._moduleDict = {}
        for i in range(1000):
            mName = str(self.ui.moduleTabWidget.tabText(i))
            if mName == '':
                break
            else:
                self._moduleList.append(mName.replace(' ',''))
        for mod in self._moduleList:
            self._moduleDict[mod] = moduleBase(mod,parent = self)

         
    def connectActions(self):
        """
        Connect the user interface controls to the logic
        """
        self.ui.actionMachine.triggered.connect(self.machineSettinsDialog)
        self.ui.actionGrid.triggered.connect(self.gridSettinsDialog)
        self.ui.actionExit.triggered.connect(self.mainQuit)
        self.ui.generateGCode_pushButton.clicked.connect(self.onGenerateGCodePressed)
        self.ui.actionPostamble.triggered.connect(self.postDialog)
        self.ui.actionPreamble.triggered.connect(self.preDialog)
        self.ui.actionDefault_GCode_Folder.triggered.connect(self.setDefaultGCodeFolder)
        QButtons = self.findChildren(QtGui.QPushButton)
        QButtonNames = self.util.getQObjectNames(QtGui.QPushButton)
        for i,BName in enumerate(QButtonNames):
            BName = BName.split('_')[0].upper()
            if BName == 'SETORIGINFROMGRID':
                QButtons[i].clicked.connect(self.setOriginFromGrid)
        self.ui.climbCutCheckBox.clicked.connect(self.climbCheck)
        
    def climbCheck(self):
        if self.ui.climbCutCheckBox.isChecked():
            self.util.setToFalseIfTrue(self.ui.conventionalCutCheckBox)
        
    
    def setDefaultGCodeFolder(self):
       folder =  QtGui.QFileDialog.getExistingDirectory(directory = self._defaultGCodeDirectory)
       if folder != '':
           self._defaultGCodeDirectory = folder
           self.util.saveTextFile('defaultGCodeDirectory.txt',folder)
        
    def machineSettinsDialog(self):
        '''
        enstantiates an instance of the machine settings dialog and calls the gui
        '''
        machineSettings = machineSettingsDialog(parent = self)
        machineSettings.exec_()
        
    def setOriginFromGrid(self):
        '''
        enstantiates an instance of the set origin from grid dialog and calls the gui
        '''
#        currentModuleIndex = self.ui.moduleTabWidget.currentIndex()
#        currentModule = str(self.ui.moduleTabWidget.tabText(currentModuleIndex)).replace(' ','')
        currentModule = self.util.getCurrentModuleName()
        setOriginFromGrid = setOriginFromGridDialog(parent = self, currentModule = currentModule)
        setOriginFromGrid.exec_()
        
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
        for k,v in self._moduleDict.items():
            v.saveModuleEntries()
    
    def onGenerateGCodePressed(self):
        '''
        reads the current module, commands it to save the entries and then produce
        g-code
        '''
        currentModuleIndex = self.ui.moduleTabWidget.currentIndex()
        currentModule = str(self.ui.moduleTabWidget.tabText(currentModuleIndex)).replace(' ','')
        self._moduleDict[currentModule].saveModuleEntries()
        gcode, setupGCode = self._moduleDict[currentModule].produceGCode()
        self.util.saveGCode(gcode, setupGCode, ModuleName = currentModule, folderPath = self._defaultGCodeDirectory)
        

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    mainapp = CNCWWCreator()
    mainapp.show()
    sys.exit(app.exec_())
