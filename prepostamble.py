# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 20:27:46 2014

@author: Dirk
"""
from PyQt4 import QtGui, QtCore
from prepostambleDialog import Ui_prePostDialog
from utilities import utilities

class prePostAmbleDialog(QtGui.QDialog):
    def __init__(self, prepostName, parent = None):
        self.parent = parent
        self.prepostName = prepostName
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_prePostDialog()
        self.ui.setupUi(self)
        self.setWindowTitle(prepostName)
        self.util = utilities()
        self.connectActions()
        self.util.loadTextEdit(self.prepostName+'.txt',self.ui.prePostTextEdit)
        
    def connectActions(self):
        """
        Connect the user interface controls to the logic
        """
        self.ui.buttonBox.accepted.connect(self.onOKButton)
        
    def onOKButton(self):
        self.util.dumpTextEdit(self.prepostName+'.txt',self.ui.prePostTextEdit)