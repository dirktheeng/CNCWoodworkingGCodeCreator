# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 20:27:46 2014

@author: Dirk
"""
from PyQt4 import QtGui, QtCore
from gridSettingsDialog import Ui_gridSettings
from utilities import utilities

class gridSettingsDialog(QtGui.QDialog):
    def __init__(self,parent=None):
        self.parent = parent
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_gridSettings()
        self.ui.setupUi(self)
        self.util = utilities(parent = self)
        self.util.setAllLineEditValidator2Double()
        self.util.populateInfo('gridSettings.txt')
        self.connectActions()

    def connectActions(self):
        """
        Connect the user interface controls to the logic
        """
        self.ui.buttonBox.accepted.connect(self.onOKButton)
        
    def onOKButton(self):
        self.util.dumpSettings('gridSettings.txt')
        self.parent.vars.gridSettings = self.util.getQObjectDict(QtGui.QLineEdit)