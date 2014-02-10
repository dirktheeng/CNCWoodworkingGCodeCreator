# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 20:27:46 2014

@author: Dirk
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