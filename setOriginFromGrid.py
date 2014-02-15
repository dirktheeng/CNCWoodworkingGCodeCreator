# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 20:27:46 2014

@author: Dirk

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
from setOriginFromGridDialog import Ui_setOriginFromGrid
from utilities import utilities

class setOriginFromGridDialog(QtGui.QDialog):
    def __init__(self,parent=None, currentModule = None):
        self.currentModule = currentModule
        self.parent = parent
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_setOriginFromGrid()
        self.ui.setupUi(self)
        self.util = utilities(parent = self)
        if self.currentModule != None:
            self.moduleUtil = utilities(parent = self.parent._moduleDict[currentModule])
        self._lineEdits = self.util.returnChildrenDictionary(QtGui.QLineEdit)
        self._spinBoxes = self.util.returnChildrenDictionary(QtGui.QSpinBox)
        self._checkBoxes = self.util.returnChildrenDictionary(QtGui.QCheckBox)
        self._comboBoxes = self.util.returnChildrenDictionary(QtGui.QComboBox)
        self._radioButtons = self.util.returnChildrenDictionary(QtGui.QRadioButton)
        self.util.populateInfo('originFromGridSettings.txt')
        self.connectActions()

    def connectActions(self):
        """
        Connect the user interface controls to the logic
        """
        self.ui.buttonBox.accepted.connect(self.onOKButton)
        
    def onOKButton(self):
        spinBoxDict = self.util.getQObjectDict(QtGui.QSpinBox)
        radioButtonDict = self.util.getQObjectDict(QtGui.QRadioButton)
        settingsDict = dict(spinBoxDict.items() + radioButtonDict.items())
        self.util.dumpSettings('originFromGridSettings.txt',settingsDict = settingsDict)
        
        gridXOffset = float(self.parent._gridSettings['gridXOffsetLineEdit'])
        gridYOffset = float(self.parent._gridSettings['gridYOffsetLineEdit'])
        gridXSpacing = float(self.parent._gridSettings['gridYSpacingLineEdit'])
        gridYSpacing = float(self.parent._gridSettings['gridYSpacingLineEdit'])
        bedXOffset = float(self.parent._machineSettings['bedXOffsetLineEdit'])
        bedYOffset = float(self.parent._machineSettings['bedYOffsetLineEdit'])
        gridXPosition = float(settingsDict['xGridPositionSpinBox'])
        gridYPosition = float(settingsDict['yGridPositionSpinBox'])
        pinXPositive = settingsDict['xPositiveRadioButton']
        pinYPositive = settingsDict['yPositiveRadioButton']
        if pinXPositive:
            pinXOffset = float(self.parent._gridSettings['pinDiameterLineEdit'])/2
        else:
            pinXOffset = -float(self.parent._gridSettings['pinDiameterLineEdit'])/2
        if pinYPositive:
            pinYOffset = float(self.parent._gridSettings['pinDiameterLineEdit'])/2
        else:
            pinYOffset = -float(self.parent._gridSettings['pinDiameterLineEdit'])/2
            
        xOrigin = bedXOffset + gridXOffset + gridXSpacing * gridXPosition + pinXOffset
        yOrigin = bedYOffset + gridYOffset + gridYSpacing * gridYPosition + pinYOffset
        
        self.parent._origin = [xOrigin,yOrigin]
        
        if self.currentModule != None:
            self.parent._moduleDict[self.currentModule]._lineEdits['xOrigin'].setText(str(xOrigin))
            self.parent._moduleDict[self.currentModule]._lineEdits['yOrigin'].setText(str(yOrigin))