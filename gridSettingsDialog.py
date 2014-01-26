# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gridSettingsDialog.ui'
#
# Created: Tue Jan 21 11:39:24 2014
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

class Ui_gridSettings(object):
    def setupUi(self, gridSettings):
        gridSettings.setObjectName(_fromUtf8("gridSettings"))
        gridSettings.setWindowModality(QtCore.Qt.ApplicationModal)
        gridSettings.resize(424, 208)
        self.verticalLayout = QtGui.QVBoxLayout(gridSettings)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(gridSettings)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.gridXSpacingLabel = QtGui.QLabel(self.groupBox)
        self.gridXSpacingLabel.setObjectName(_fromUtf8("gridXSpacingLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.gridXSpacingLabel)
        self.gridXSpacingLineEdit = QtGui.QLineEdit(self.groupBox)
        self.gridXSpacingLineEdit.setObjectName(_fromUtf8("gridXSpacingLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.gridXSpacingLineEdit)
        self.gridXOffsetLabel = QtGui.QLabel(self.groupBox)
        self.gridXOffsetLabel.setObjectName(_fromUtf8("gridXOffsetLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.gridXOffsetLabel)
        self.gridXOffsetLineEdit = QtGui.QLineEdit(self.groupBox)
        self.gridXOffsetLineEdit.setObjectName(_fromUtf8("gridXOffsetLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.gridXOffsetLineEdit)
        self.gridYSpacingLabel = QtGui.QLabel(self.groupBox)
        self.gridYSpacingLabel.setObjectName(_fromUtf8("gridYSpacingLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.gridYSpacingLabel)
        self.gridYSpacingLineEdit = QtGui.QLineEdit(self.groupBox)
        self.gridYSpacingLineEdit.setObjectName(_fromUtf8("gridYSpacingLineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.gridYSpacingLineEdit)
        self.gridYSpacingLabel_2 = QtGui.QLabel(self.groupBox)
        self.gridYSpacingLabel_2.setObjectName(_fromUtf8("gridYSpacingLabel_2"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.gridYSpacingLabel_2)
        self.gridYSpacingLineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.gridYSpacingLineEdit_2.setObjectName(_fromUtf8("gridYSpacingLineEdit_2"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.gridYSpacingLineEdit_2)
        self.pinDiameterLabel = QtGui.QLabel(self.groupBox)
        self.pinDiameterLabel.setObjectName(_fromUtf8("pinDiameterLabel"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.pinDiameterLabel)
        self.pinDiameterLineEdit = QtGui.QLineEdit(self.groupBox)
        self.pinDiameterLineEdit.setObjectName(_fromUtf8("pinDiameterLineEdit"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.pinDiameterLineEdit)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(gridSettings)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.maxXRowsLabel = QtGui.QLabel(self.groupBox_2)
        self.maxXRowsLabel.setObjectName(_fromUtf8("maxXRowsLabel"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.maxXRowsLabel)
        self.maxXRowsLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.maxXRowsLineEdit.setObjectName(_fromUtf8("maxXRowsLineEdit"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.maxXRowsLineEdit)
        self.maxYRowsLabel = QtGui.QLabel(self.groupBox_2)
        self.maxYRowsLabel.setObjectName(_fromUtf8("maxYRowsLabel"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.maxYRowsLabel)
        self.maxYRowsLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.maxYRowsLineEdit.setObjectName(_fromUtf8("maxYRowsLineEdit"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.maxYRowsLineEdit)
        self.gridLayout_3.addLayout(self.formLayout_3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(gridSettings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(gridSettings)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), gridSettings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), gridSettings.reject)
        QtCore.QMetaObject.connectSlotsByName(gridSettings)

    def retranslateUi(self, gridSettings):
        gridSettings.setWindowTitle(_translate("gridSettings", "Grid Settings", None))
        self.groupBox.setTitle(_translate("gridSettings", "Dimensions", None))
        self.gridXSpacingLabel.setText(_translate("gridSettings", "Grid X Spacing", None))
        self.gridXOffsetLabel.setText(_translate("gridSettings", "Grid X Offset", None))
        self.gridYSpacingLabel.setText(_translate("gridSettings", "Grid Y Spacing", None))
        self.gridYSpacingLabel_2.setText(_translate("gridSettings", "Grid Y Spacing", None))
        self.pinDiameterLabel.setText(_translate("gridSettings", "Pin Diameter", None))
        self.groupBox_2.setTitle(_translate("gridSettings", "Limits", None))
        self.maxXRowsLabel.setText(_translate("gridSettings", "Max X Rows", None))
        self.maxYRowsLabel.setText(_translate("gridSettings", "Max Y Rows", None))

