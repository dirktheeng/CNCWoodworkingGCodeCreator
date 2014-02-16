# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:02:18 2014

@author: Dirk Van Essendelft

The product of this software is text files which contain gcode that may or may 
not be suitable to use with CNC machines and equipment. If gcode is not suitable 
for a CNC machine or equipment, it can cause damage to equipment and parts as 
well as personnel injuries which can vary in severity and could include death. 
Determination of the suitability of the product gcode for use on any CNC machines 
or equipment is solely the responsibility of the users of this software (you). 
This means that the users of this software (you) should carefully inspect the 
gcode produced from this software and know every aspect of the gcode BEFORE you 
use it on any CNC equipment. Because there are aspects of gcode which are 
specific to each CNC machine or equipment, gcode should never be directly 
transferred from one machine to another. Users of this software should only 
use gcode from this software on the same machine for which the software is setup.
The authors of this software offer no warranty and no guarantee for any of the 
gcode produced from this software. 

By using this software, you are agreeing that the authors of this software are 
to be held free from any and all liability related to the use of the gcode 
produced from this software on any CNC machine or equipment. In Addition should
you using this software, you agree to take complete liability for the use of 
the gcode you produce from this software which includes any and all equipment 
and/or part damage and/or injury and/or death to yourself and/or others due to 
improper gcode statements which make the gcode unsuitable for use with CNC 
equipment or machines. Further, by using this software, you agree not to 
transfer and product gcode to any other equipment but that which has been 
properly setup in the software. Finally, by using this software, you are 
agreeing not to remove this liability statement from the software.

If you cannot agree to these liability terms, you must not use software or any 
part of it in any way, shape, or form.

The software copyright is held by Dirk Van Essendelft and all rights are reserved.

The software is licensed under the GNU GPL v3 license.

The software is free for non-commercial use. If the software is used
for commercial purposes, a modest fee of $50 should be paid to the developers.
Payment arrangements can be made by contacting the copyright holder by email at
dirktheeng@gmail.com

"""

# Core Imports
import sys, os #, csv, json

# Get this file path, make sure it is in the python path for the imports to work
# if the project is outside of python's site-packages
sys.path.append(os.path.dirname(sys.argv[0]))

# import qt warapper
from utilities.QtWrapper import QtGui, QtCore, QtLoadUI, variant

# import custom libraries
from utilities.utilities import utilities
from dialogs.machineSettings import machineSettingsDialog
from dialogs.gridSettings import gridSettingsDialog
from dialogs.prepostamble import prePostAmbleDialog
from dialogs.liabilityWaver import liabilityWaversDialog
from dialogs.setOriginFromGrid import setOriginFromGridDialog
from utilities.moduleBase import moduleBase

class CNCWWCreator(QtGui.QMainWindow):
    '''
    This is the main program class
    '''
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        # Load uifile
        self.ui = QtLoadUI('./uiFiles/Main.ui', self)
        
        self.util = utilities(parent = self)
        
        self._liabilityQuit = True
        self.liabilityDialog()
        if self._liabilityQuit:
            sys.exit(app.exec_())
        self._defaultGCodeDirectory = self.util.readDefaultGCodeDirectory()
        self._machineSettings = self.util.getSettings('machineSettings.txt')
        self._gridSettings = self.util.getSettings('gridSettings.txt')
        self._moduleList = []
        self._origin = [0,0]
        self._moduleDict = {}
        
        for i in range(self.ui.moduleTabWidget.count()):
            mName = str(self.ui.moduleTabWidget.tabText(i))
            if mName == '':
                break
            else:
                self._moduleList.append(mName.replace(' ',''))
        for mod in self._moduleList:
            self._moduleDict[mod] = moduleBase(mod,parent = self)
        
        self.connectActions()
        self.horizontalNibbleChecks()
         
    def connectActions(self):
        """
        Connect the user interface controls to the logic
        """
        self.ui.actionMachine.triggered.connect(self.machineSettinsDialog)
        self.ui.actionGrid.triggered.connect(self.gridSettinsDialog)
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
        for k,v in self._moduleDict.items():
            if v._climbCutObject != None:
                v._climbCutObject.clicked.connect(self.climbCheck)
                v._conventionalCutObject.clicked.connect(self.conventionalCheck)
        self._moduleDict['StraightCut']._checkBoxes['horizontalNibble'].clicked.connect(self.horizontalNibbleChecks)
        
        
    def horizontalNibbleChecks(self):
        hNibbleVal = self._moduleDict['StraightCut']._getCheckBoxVal('horizontalNibble')
        if self._moduleDict['StraightCut']._getCheckBoxVal('onVector'):
            QtGui.QMessageBox.warning(self,'Settings Conflict','Horizontal Nibble cannot be used with On Vector')
            hNibbleVal = False
            self._moduleDict['StraightCut']._checkBoxes['horizontalNibble'].setChecked(False)
        if hNibbleVal:
            self._moduleDict['StraightCut']._spinBoxes['cutPasses'].setMinimum(1)
        else:
            self._moduleDict['StraightCut']._spinBoxes['cutPasses'].setMinimum(0)
            
        
    def climbCheck(self):
        currentModuleName = self.util.getCurrentModuleName()
        conventionalCutObject = self._moduleDict[currentModuleName]._conventionalCutObject
        climbCutObject = self._moduleDict[currentModuleName]._climbCutObject
        if climbCutObject.isChecked():
            self.util.setToFalseIfTrue(conventionalCutObject)
            
    def conventionalCheck(self):
        currentModuleName = self.util.getCurrentModuleName()
        conventionalCutObject = self._moduleDict[currentModuleName]._conventionalCutObject
        climbCutObject = self._moduleDict[currentModuleName]._climbCutObject
        if conventionalCutObject.isChecked():
            self.util.setToFalseIfTrue(climbCutObject)
        
    
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
        
    def closeEvent(self,event):
        '''
        handles actions on exit
        '''
        for k,v in self._moduleDict.items():
            print 'Saving ' +k+ ' Module Entries'
            v.saveModuleEntries()
        
    def liabilityDialog(self):
        liabilityDialog = liabilityWaversDialog(parent = self)
        liabilityDialog.exec_()
    
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
    try:
        sys.exit(app.exec_())
    except:
        pass
