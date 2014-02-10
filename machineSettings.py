# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 20:27:46 2014

@author: Dirk
"""
from PyQt4 import QtGui, QtCore
from machineSettingsDialog import Ui_machineSettings
from utilities import utilities

class machineSettingsDialog(QtGui.QDialog):
    def __init__(self,parent=None):
        self.parent = parent
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_machineSettings()
        self.ui.setupUi(self)
        self.util =utilities(parent = self)
        self._lineEdits = self.util.returnChildrenDictionary(QtGui.QLineEdit)
        self._spinBoxes = self.util.returnChildrenDictionary(QtGui.QSpinBox)
        self._checkBoxes = self.util.returnChildrenDictionary(QtGui.QCheckBox)
        self._comboBoxes = self.util.returnChildrenDictionary(QtGui.QComboBox)
        self.util.setAllLineEditValidator2Double()
        self.util.populateInfo('machineSettings.txt')
        self.connectActions()

    def connectActions(self):
        """
        Connect the user interface controls to the logic
        """
        self.ui.buttonBox.accepted.connect(self.onOKButton)
        
    def onOKButton(self):
        self.util.dumpSettings('machineSettings.txt')
        self.parent._machineSettings = self.util.getQObjectDict(QtGui.QLineEdit)