# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 20:33:02 2014

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
from PyQt4 import QtGui, QtCore
from utilities import utilities
from gMotion import gMotion
import numpy as np

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
        self._findClimbConventionalCheckboxes()
        
    def _findClimbConventionalCheckboxes(self):
        try:
            self._conventionalCutObject = self.util.returnChildrenDictionary(\
                QtGui.QCheckBox,searchString = 'conventionalCut').values()[0]
            self._climbCutObject = self.util.returnChildrenDictionary(\
                QtGui.QCheckBox,searchString = 'climbCut').values()[0]
        except:
            self._conventionalCutObject = None
            self._climbCutObject = None

    def _getLineEditFloats(self,name):
        try:
            value = float(self._lineEdits[name].text())
        except:
            value = 0.0
        return value
        
    def _getSpinBoxInt(self,name):
        return int(self._spinBoxes[name].text())
        
    def _getComboBoxIndexInt(self,name):
        return int(self._comboBoxes[name].currentIndex())
        
    def _getCheckBoxVal(self,name):
        return self._checkBoxes[name].isChecked()
    
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
                'Problem loading setup Text for ' + self.name
            
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
        moduleCheckBox = self.util.getQObjectDict(QtGui.QCheckBox)
        self.moduleDict = dict(moduleEntryDict.items() + moduleComboDict.items() \
            + moduleSpinBox.items() + moduleCheckBox.items())
        
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
        safeZHeight          = self._getLineEditFloats('safeZHeight')
        globalHomePosition = [float(self.parent._machineSettings['bedXLengthLineEdit']),float(self.parent._machineSettings['bedYLengthLineEdit']),safeZHeight]
        if self.name == 'Jointer':
            distFromOrigin          = self._getLineEditFloats('distFromOrigin')
            materialLength          = self._getLineEditFloats('materialLength')
            materialWidth           = self._getLineEditFloats('materialWidth')
            materialThickness       = self._getLineEditFloats('materialThickness')
            zAxisOffset             = self._getLineEditFloats('zAxisOffset')
            toolDiameter            = self._getLineEditFloats('toolDiameter')
            overTravel              = self._getLineEditFloats('overTravel')
            cutOffset               = self._getLineEditFloats('cutOffset')
            cutPassFeedRate         = self._getLineEditFloats('cutPassFeedRate')
            cutPassSpindleSpeed     = self._getLineEditFloats('cutPassSpindleSpeed')
            finalPassFeedRate       = self._getLineEditFloats('finalPassFeedRate')
            finalPassSpindleSpeed   = self._getLineEditFloats('finalPassSpindleSpeed')
            finalOffset             = self._getLineEditFloats('finalOffset')
            cutPasses               = self._getSpinBoxInt('cutPasses')
            finalPasses             = self._getSpinBoxInt('finalPasses')
            selectXYAxis            = self._getComboBoxIndexInt('selectXYAxis')
            startAxiDist            = distFromOrigin + materialLength + overTravel
            finishAxiDist           = distFromOrigin - overTravel
            firstCutPass = True
            if selectXYAxis == 0:
                moduleHome = [materialLength + distFromOrigin + 6,materialWidth + 6,safeZHeight]
            else:
                moduleHome = [materialWidth + 6,materialLength + distFromOrigin + 6,safeZHeight]
                
            homePosition = motion.mergeMinVectorComponents(globalHomePosition,moduleHome)
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
                    if firstCutPass:
                        gcode += motion.addFeedandSpeed(feedrate = cutPassFeedRate, speed = cutPassSpindleSpeed)
                        gcode += motion.turnSpindleOn()
                        firstCutPass = False
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
            
        if self.name == 'StraightCut':
            origin = np.asarray([self._getLineEditFloats('xOrigin'), self._getLineEditFloats('yOrigin')])
            p1 = np.asarray([self._getLineEditFloats('p1X'), self._getLineEditFloats('p1Y')])
            p2 = np.asarray([self._getLineEditFloats('p2X'), self._getLineEditFloats('p2Y')])
            materialThickness       = self._getLineEditFloats('materialThickness')
            materialXDimension      = self._getLineEditFloats('materialXDimension')
            materialYDimension      = self._getLineEditFloats('materialYDimension')
            toolDiameter            = self._getLineEditFloats('toolDiameter')
            overTravel              = self._getLineEditFloats('overTravel')
            zAxisOffset             = self._getLineEditFloats('zAxisOffset')
            cutOffset               = self._getLineEditFloats('cutOffset')
            cutPassFeedRate         = self._getLineEditFloats('cutPassFeedRate')
            cutPassSpindleSpeed     = self._getLineEditFloats('cutPassSpindleSpeed')
            finalPassFeedRate       = self._getLineEditFloats('finalPassFeedRate')
            finalPassSpindleSpeed   = self._getLineEditFloats('finalPassSpindleSpeed')
            finalOffset             = self._getLineEditFloats('finalOffset')
            horizontalNibbleOffset  = self._getLineEditFloats('horizontalNibbleOffset')
            cutPasses               = self._getSpinBoxInt('cutPasses')
            finalPasses             = self._getSpinBoxInt('finalPasses')
            cutReverseDirection     = self._getCheckBoxVal('cutReverseDirection')
            horizontalNibble        = self._getCheckBoxVal('horizontalNibble')
            
            moduleHome = [origin[0] + materialXDimension + 6,origin[1] + materialYDimension + 6,safeZHeight]
            homePosition = motion.mergeMinVectorComponents(globalHomePosition,moduleHome)
            if cutReverseDirection:
                travelVector = p1-p2
                p0 = p2
            else:
                travelVector = p2-p1
                p0 = p1
                
            travelUnitVector = motion.calcUnitVector(travelVector)
            travelVectorMag = motion.calcVectorMag(travelVector)
            
            if self._checkBoxes['rightSideOfVector'].isChecked():
                bitOffsetRotation = -np.pi/2.0
            elif self._checkBoxes['leftSideOfVector'].isChecked():
                bitOffsetRotation = np.pi/2.0
            else:
                bitOffsetRotation = None
                
            if bitOffsetRotation != None and cutReverseDirection:
                bitOffsetRotation = -bitOffsetRotation
                
            if bitOffsetRotation == None:
                bitOffsetVect = np.array([0,0])
            else:
                bitOffsetVect = motion.calc2DRotateVect(travelUnitVector,bitOffsetRotation)*toolDiameter
            
            if self._checkBoxes['onVector'].isChecked():
                hrizOffsetUnitVect = np.array([0,0])
            else:
                hrizOffsetUnitVect = motion.calcUnitVector(bitOffsetVect)
            
            startPoint = p0-travelUnitVector*overTravel + bitOffsetVect + origin
            totalMag = travelVectorMag + 2.0 * overTravel
            endPoint = startPoint + totalMag*travelUnitVector

            
            spindlOn = False            
            firstCutPass = True
            if horizontalNibble:
                if cutPasses > 0:
                    startCutXY = startPoint + hrizOffsetUnitVect * horizontalNibbleOffset
                    endCutXY = endPoint + hrizOffsetUnitVect * horizontalNibbleOffset
                    cutPassDXYMag = (cutOffset - horizontalNibbleOffset) / (cutPasses)
                    cutPassDXY = hrizOffsetUnitVect * cutPassDXYMag
                    startXYZ_cut = [startCutXY[0],startCutXY[1],zAxisOffset]
                    endXYZ_cut = [endCutXY[0],endCutXY[1],zAxisOffset]
                    for i in range(cutPasses+1):
                        if firstCutPass:
                            gcode += motion.addFeedandSpeed(feedrate = cutPassFeedRate, speed = cutPassSpindleSpeed)
                            gcode += motion.turnSpindleOn()
                            firstCutPass = False
                            spindleOn = True
                        gcode += motion.rapid(startXYZ_cut,safeZ = safeZHeight)
                        gcode += motion.lineFeed(endXYZ_cut)
                        startXYZ_cut = motion.translatePointOrVect(startXYZ_cut,cutPassDXY)
                        endXYZ_cut = motion.translatePointOrVect(endXYZ_cut,cutPassDXY)
                        print startXYZ_cut
            else:
                if cutPasses > 0:
                    startCutXY = startPoint + hrizOffsetUnitVect * cutOffset
                    endCutXY = endPoint + hrizOffsetUnitVect * cutOffset
                    cutPassDZ = (materialThickness -  zAxisOffset)/ (cutPasses)
                    startXYZ_cut = [startCutXY[0],startCutXY[1],materialThickness]
                    endXYZ_cut = [endCutXY[0],endCutXY[1],materialThickness]
                    for i in range(cutPasses):
                        iterationVect = [0,0,-cutPassDZ]
                        startXYZ_cut = motion.translatePointOrVect(startXYZ_cut,iterationVect)
                        endXYZ_cut = motion.translatePointOrVect(endXYZ_cut,iterationVect)
                        if firstCutPass:
                            gcode += motion.addFeedandSpeed(feedrate = cutPassFeedRate, speed = cutPassSpindleSpeed)
                            gcode += motion.turnSpindleOn()
                            firstCutPass = False
                            spindleOn = True
                        gcode += motion.rapid(startXYZ_cut,safeZ = safeZHeight)
                        gcode += motion.lineFeed(endXYZ_cut)
            gcode += motion.addFeedandSpeed(feedrate = finalPassFeedRate, speed = finalPassSpindleSpeed)
            
            if spindleOn == False:
                gcode += motion.turnSpindleOn()
                spindleOn = True
            
            startFinalXY = startPoint + hrizOffsetUnitVect * finalOffset
            endFinalXY = endPoint + hrizOffsetUnitVect * finalOffset
            
            startXYZ_final = [startFinalXY[0],startFinalXY[1],zAxisOffset]
            endXYZ_final = [endFinalXY[0],endFinalXY[1],zAxisOffset]
            
            
            for i in range(int(finalPasses)):
                gcode += motion.rapid(startXYZ_final,safeZ = safeZHeight)
                gcode += motion.lineFeed(endXYZ_final)
            
            gcode += motion.turnSpindleOff()
            spindleOn = False
            print homePosition
            gcode += motion.rapid(homePosition,safeZ = safeZHeight)
            gcode += motion.addPostamble()
            
            setupGCode = motion.addPreamble()
            setupGCode += motion.rapid(startXYZ_final,safeZ = safeZHeight)
            setupGCode += motion.addPostamble()
            print gcode
            
            return (gcode,setupGCode)
        else:
            return None
            
            