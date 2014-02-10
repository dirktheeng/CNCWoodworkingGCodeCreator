# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 20:33:02 2014

@author: Dirk
"""
from PyQt4 import QtGui, QtCore
from utilities import utilities
from gMotion import gMotion

class moduleBase():
    '''
    This class handles all functions related to the module and should only be
    enstantiated from the main program
    '''
    def __init__(self,name,parent=None):
        self.parent = parent
        self.name = name
        self.util = utilities() # this is here so the methods appear in text completion
        cmd = 'self.util = utilities(parent = self.parent.ui.tab_'+name+')'
        exec(cmd)
        self.setupXYComboBox()
        self.modUtil = utilities(parent = self)
        self._lineEdits = self.util.returnChildrenDictionary(QtGui.QLineEdit)
        self._spinBoxes = self.util.returnChildrenDictionary(QtGui.QSpinBox)
        self._checkBoxes = self.util.returnChildrenDictionary(QtGui.QCheckBox)
        self._comboBoxes = self.util.returnChildrenDictionary(QtGui.QComboBox)
        self._setupText = self.util.returnChildrenDictionary(QtGui.QTextBrowser, searchString = 'setupText')
        self.modUtil.setAllLineEditValidator2Double()
        self.loadModuleEntries()
        self.loadSetupHTML()
        
    def loadSetupHTML(self):
        try:
            with open(self.name+'_Setup.htm','r') as htmlFile:
                htmlText = htmlFile.read()
        except:
            QtGui.QMessageBox.information(self.parent,'File Error',self.name+'_Setup.htm was not found')
            htmlText = None
        if htmlText != None:
            try:
                self._setupText['setupText'].setHtml(htmlText)
            except:
                print 'Problem loading setup Text for ' + self.name
            
    def setupXYComboBox(self):
        try:
            selectXYCB = self.util.returnChildrenDictionary(QtGui.QComboBox,searchString = 'selectXYAxis')
            selectXYCB['selectXYAxis'].addItems(["X Axis","Y Axis"])
        except:
            pass
                
    def saveModuleEntries(self):
        fileName = self.name+'_ModuleEntries.txt'
        self.buildModuleDict()
        self.modUtil.dumpSettings(fileName,settingsDict = self.moduleDict)
        
    def buildModuleDict(self):
        moduleEntryDict = self.util.getQObjectDict(QtGui.QLineEdit)
        moduleComboDict = self.util.getQObjectDict(QtGui.QComboBox)
        moduleSpinBox = self.util.getQObjectDict(QtGui.QSpinBox)
        self.moduleDict = dict(moduleEntryDict.items() + moduleComboDict.items() + moduleSpinBox.items())
        
    def loadModuleEntries(self):
        fileName = self.name+'_ModuleEntries.txt'
        self.modUtil.populateInfo(fileName)
        self.buildModuleDict()
        
    def produceGCode(self):
        '''
        This function handles producing the g-code for all modules
        '''
        self.buildModuleDict()
        machineSettings = self.util.getSettings('machineSettings.txt')
        gridSettings = self.util.getSettings('gridSettings.txt')
        Table_Offset = (float(machineSettings["bedXOffsetLineEdit"]),float(machineSettings["bedYOffsetLineEdit"]),0)
        spindleOn = False
        motion = gMotion(Table_Offset=Table_Offset, parent = self)
        gcode = ''
        gcode = motion.addPreamble()
        safeZHeight          = float(self._lineEdits['safeZHeight'].text())
        homePosition = [float(self.parent._machineSettings['bedXLengthLineEdit']),float(self.parent._machineSettings['bedYLengthLineEdit']),safeZHeight]
        if self.name == 'Jointer':
            distFromOrigin          = float(self._lineEdits['distFromOrigin'].text())
            materialLength          = float(self._lineEdits['materialLength'].text())
            materialThickness       = float(self._lineEdits['materialThickness'].text())
            cutOffset               = float(self._lineEdits['cutOffset'].text())
            zAxisOffset             = float(self._lineEdits['zAxisOffset'].text())
            toolDiameter            = float(self._lineEdits['toolDiameter'].text())
            overTravel              = float(self._lineEdits['overTravel'].text())
            cutPassFeedRate         = float(self._lineEdits['cutPassFeedRate'].text())
            cutPassSpindleSpeed     = float(self._lineEdits['cutPassSpindleSpeed'].text())
            finalPassFeedRate       = float(self._lineEdits['finalPassFeedRate'].text())
            finalPassSpindleSpeed   = float(self._lineEdits['finalPassSpindleSpeed'].text())
            finalOffset             = float(self._lineEdits['finalOffset'].text())
            cutPasses               = int(self._spinBoxes['cutPasses'].text())
            finalPasses             = int(self._spinBoxes['finalPasses'].text())
            selectXYAxis            = int(self._comboBoxes['selectXYAxis'].currentIndex())
            startAxiDist            = distFromOrigin + materialLength + overTravel
            finishAxiDist           = distFromOrigin - overTravel
            if cutPasses > 0:
                cutPassDZ = (materialThickness -  zAxisOffset)/ (cutPasses)
                if selectXYAxis == 0:
                    startXYZ_cut = [startAxiDist,cutOffset - toolDiameter/2.0,zAxisOffset]
                    endXYZ_cut = [finishAxiDist,cutOffset - toolDiameter/2.0,zAxisOffset]
                else:
                    startXYZ_cut = [cutOffset - toolDiameter/2.0,finishAxiDist,zAxisOffset]
                    endXYZ_cut = [cutOffset - toolDiameter/2.0,startAxiDist,zAxisOffset]
                for i in range(cutPasses):
                    zCutHeight = materialThickness - cutPassDZ*(i+1)
                    startXYZ_cut[2] = zCutHeight
                    endXYZ_cut[2] = zCutHeight
                    gcode += motion.addFeedandSpeed(feedrate = cutPassFeedRate, speed = cutPassSpindleSpeed)
                    gcode += motion.turnSpindleOn()
                    spindleOn = True
                    gcode += motion.rapid(startXYZ_cut,safeZ = safeZHeight)
                    gcode += motion.lineFeed(endXYZ_cut)
            gcode += motion.addFeedandSpeed(feedrate = finalPassFeedRate, speed = finalPassSpindleSpeed)
            if spindleOn == False:
                gcode += motion.turnSpindleOn()
                spindleOn = True
                    
            
            if selectXYAxis == 0:
                startXYZ_final = [startAxiDist,finalOffset - toolDiameter/2.0,zAxisOffset]
                endXYZ_final = [finishAxiDist,finalOffset - toolDiameter/2.0,zAxisOffset]
            else:
                startXYZ_final = [finalOffset - toolDiameter/2.0,finishAxiDist,zAxisOffset]
                endXYZ_final = [finalOffset - toolDiameter/2.0,startAxiDist,zAxisOffset]
            
            
            for i in range(int(finalPasses)):
                gcode += motion.rapid(startXYZ_final,safeZ = safeZHeight)
                gcode += motion.lineFeed(endXYZ_final)
                
            gcode += motion.turnSpindleOff()
            spindleOn = False
            gcode += motion.rapid(homePosition,safeZ = safeZHeight)
            gcode += motion.addPostamble()
            
            setupGCode = motion.addPreamble()
            setupGCode += motion.rapid(startXYZ_final,safeZ = safeZHeight)
            setupGCode += motion.addPostamble()
            
            
            return (gcode,setupGCode)
            
            
        else:
            return None