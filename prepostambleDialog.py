# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prepostamble.ui'
#
# Created: Sun Jan 26 19:57:05 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_prePostDialog(object):
    def setupUi(self, prePostDialog):
        prePostDialog.setObjectName(_fromUtf8("prePostDialog"))
        prePostDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        prePostDialog.resize(558, 427)
        self.verticalLayout_2 = QtGui.QVBoxLayout(prePostDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.prePostTextEdit = QtGui.QTextEdit(prePostDialog)
        self.prePostTextEdit.setObjectName(_fromUtf8("prePostTextEdit"))
        self.verticalLayout.addWidget(self.prePostTextEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(prePostDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(prePostDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), prePostDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), prePostDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(prePostDialog)

    def retranslateUi(self, prePostDialog):
        prePostDialog.setWindowTitle(_translate("prePostDialog", "Dialog", None))

