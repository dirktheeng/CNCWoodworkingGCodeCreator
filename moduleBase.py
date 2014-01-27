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
        self.loadSetupHTML()
        self.setupXYComboBox()
        self.util = utilities() # this is here so the methods appear in text completion
        cmd = 'self.util = utilities(parent = self.parent.ui.tab_'+name+')'
        exec(cmd)
        self.parentUtil = utilities(parent=parent)
        self.parentUtil.setAllLineEditValidator2Double(listLineEdit = self.util.getQObjectNames(QtGui.QLineEdit))
        self.loadModuleEntries()
        
    def loadSetupHTML(self):
        try:
            with open(self.name+'_Setup.htm','r') as htmlFile:
                htmlText = htmlFile.read()
        except:
            QtGui.QMessageBox.information(self.parent,'File Error',self.name+'_Setup.htm was not found')
            htmlText = None
        if htmlText != None:
            cmd = 'self.parent.ui.textBrowser_'+self.name+'_Setup.setHtml(htmlText)'
            try:
                exec(cmd)
            except:
                pass
            
    def setupXYComboBox(self):
        try:
            cmd = 'self.parent.ui.comboBox_'+self.name+'_SelectXYAxis.addItems(["X Axis","Y Axis"])'
            exec(cmd)
        except:
            pass
                
    def saveModuleEntries(self):
        fileName = self.name+'_ModuleEntries.txt'
        self.buildModuleDict()
        self.util.dumpSettings(fileName,settingsDict = self.moduleDict)
        
    def buildModuleDict(self):
        moduleEntryDict = self.util.getQObjectDict(QtGui.QLineEdit)
        moduleComboDict = self.util.getQObjectDict(QtGui.QComboBox)
        moduleSpinBox = self.util.getQObjectDict(QtGui.QSpinBox)
        self.moduleDict = dict(moduleEntryDict.items() + moduleComboDict.items() + moduleSpinBox.items())
        
    def loadModuleEntries(self):
        fileName = self.name+'_ModuleEntries.txt'
        self.parentUtil.populateInfo(fileName)
        self.buildModuleDict()
        
    def produceGCode(self):
        '''
        This function handles producing the g-code for all modules
        '''
        self.buildModuleDict()
        machineSettings = self.util.getSettings('machineSettings.txt')
        gridSettings = self.util.getSettings('gridSettings.txt')
        Table_Offset = (float(machineSettings["bedXOffsetLineEdit"]),float(machineSettings["bedYOffsetLineEdit"]),0)
        motion = gMotion(Table_Offset=Table_Offset, parent = self)
        gcode = ''
        gcode = motion.addPreamble()
        for k,v in self.moduleDict.items():
            k = k.split('LineEdit')[0]
            k = k.split('SpinBox')[0]
            if k.rfind("_"+self.name+"_") != -1:
                k = k.split("_"+self.name+"_")[1]
            cmd = k + " = float(" + str(v) + ')'
            print k, v
            exec(cmd)  
        if self.name == 'Jointer':
            startAxiDist = distFromOrigin + materialLength + overTravel
            finishAxiDist = distFromOrigin - overTravel
            
            cutPasses = int(cutPasses)
            if cutPasses > 0:
                cutPassDZ = (materialThickness -  zAxisOffset)/ (cutPasses)
                if SelectXYAxis == 0:
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
                    gcode += motion.rapid(startXYZ_cut,safeZ = safeZHeight)
                    gcode += motion.lineFeed(endXYZ_cut)
                    
            
            if SelectXYAxis == 0:
                startXYZ_final = [startAxiDist,finalOffset - toolDiameter/2.0,zAxisOffset]
                endXYZ_final = [finishAxiDist,finalOffset - toolDiameter/2.0,zAxisOffset]
            else:
                startXYZ_final = [finalOffset - toolDiameter/2.0,finishAxiDist,zAxisOffset]
                endXYZ_final = [finalOffset - toolDiameter/2.0,startAxiDist,zAxisOffset]
            
            gcode += motion.addFeedandSpeed(feedrate = finalPassFeedRate, speed = finalPassSpindleSpeed)
            for i in range(int(finalPasses)):
                gcode += motion.rapid(startXYZ_final,safeZ = safeZHeight)
                gcode += motion.lineFeed(endXYZ_final)
                
            gcode += motion.addPostamble()
            
            print gcode
            
            
        else:
            return None