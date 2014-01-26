# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'machineSettingsDialog.ui'
#
# Created: Tue Jan 21 11:38:50 2014
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

class Ui_machineSettings(object):
    def setupUi(self, machineSettings):
        machineSettings.setObjectName(_fromUtf8("machineSettings"))
        machineSettings.setWindowModality(QtCore.Qt.ApplicationModal)
        machineSettings.resize(426, 182)
        self.verticalLayout = QtGui.QVBoxLayout(machineSettings)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(machineSettings)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.bedXLengthLabel = QtGui.QLabel(self.groupBox)
        self.bedXLengthLabel.setObjectName(_fromUtf8("bedXLengthLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.bedXLengthLabel)
        self.bedXOffsetLineEdit = QtGui.QLineEdit(self.groupBox)
        self.bedXOffsetLineEdit.setInputMask(_fromUtf8(""))
        self.bedXOffsetLineEdit.setText(_fromUtf8(""))
        self.bedXOffsetLineEdit.setCursorPosition(0)
        self.bedXOffsetLineEdit.setObjectName(_fromUtf8("bedXOffsetLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.bedXOffsetLineEdit)
        self.bedYLengthLabel = QtGui.QLabel(self.groupBox)
        self.bedYLengthLabel.setObjectName(_fromUtf8("bedYLengthLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.bedYLengthLabel)
        self.bedYLengthLineEdit = QtGui.QLineEdit(self.groupBox)
        self.bedYLengthLineEdit.setInputMask(_fromUtf8(""))
        self.bedYLengthLineEdit.setText(_fromUtf8(""))
        self.bedYLengthLineEdit.setCursorPosition(0)
        self.bedYLengthLineEdit.setObjectName(_fromUtf8("bedYLengthLineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.bedYLengthLineEdit)
        self.bedYOffsetLineEdit = QtGui.QLineEdit(self.groupBox)
        self.bedYOffsetLineEdit.setInputMask(_fromUtf8(""))
        self.bedYOffsetLineEdit.setText(_fromUtf8(""))
        self.bedYOffsetLineEdit.setFrame(True)
        self.bedYOffsetLineEdit.setCursorPosition(0)
        self.bedYOffsetLineEdit.setObjectName(_fromUtf8("bedYOffsetLineEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.bedYOffsetLineEdit)
        self.bedXOffsetLabel = QtGui.QLabel(self.groupBox)
        self.bedXOffsetLabel.setObjectName(_fromUtf8("bedXOffsetLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.bedXOffsetLabel)
        self.bedYOffsetLabel = QtGui.QLabel(self.groupBox)
        self.bedYOffsetLabel.setObjectName(_fromUtf8("bedYOffsetLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.bedYOffsetLabel)
        self.bedXLengthLineEdit = QtGui.QLineEdit(self.groupBox)
        self.bedXLengthLineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.bedXLengthLineEdit.setInputMask(_fromUtf8(""))
        self.bedXLengthLineEdit.setText(_fromUtf8(""))
        self.bedXLengthLineEdit.setCursorPosition(0)
        self.bedXLengthLineEdit.setObjectName(_fromUtf8("bedXLengthLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.bedXLengthLineEdit)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(machineSettings)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.maxXTravelLabel = QtGui.QLabel(self.groupBox_2)
        self.maxXTravelLabel.setObjectName(_fromUtf8("maxXTravelLabel"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.maxXTravelLabel)
        self.maxXTravelLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.maxXTravelLineEdit.setObjectName(_fromUtf8("maxXTravelLineEdit"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.maxXTravelLineEdit)
        self.maxYTravelLabel = QtGui.QLabel(self.groupBox_2)
        self.maxYTravelLabel.setObjectName(_fromUtf8("maxYTravelLabel"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.maxYTravelLabel)
        self.maxYTravelLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.maxYTravelLineEdit.setObjectName(_fromUtf8("maxYTravelLineEdit"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.maxYTravelLineEdit)
        self.maxZTravelLabel = QtGui.QLabel(self.groupBox_2)
        self.maxZTravelLabel.setObjectName(_fromUtf8("maxZTravelLabel"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.maxZTravelLabel)
        self.maxZTravelLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.maxZTravelLineEdit.setObjectName(_fromUtf8("maxZTravelLineEdit"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.maxZTravelLineEdit)
        self.maxSpindleSpeedLabel = QtGui.QLabel(self.groupBox_2)
        self.maxSpindleSpeedLabel.setObjectName(_fromUtf8("maxSpindleSpeedLabel"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.maxSpindleSpeedLabel)
        self.maxSpindleSpeedLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.maxSpindleSpeedLineEdit.setObjectName(_fromUtf8("maxSpindleSpeedLineEdit"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.maxSpindleSpeedLineEdit)
        self.gridLayout_3.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(machineSettings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(machineSettings)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), machineSettings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), machineSettings.reject)
        QtCore.QMetaObject.connectSlotsByName(machineSettings)
        machineSettings.setTabOrder(self.buttonBox, self.bedXLengthLineEdit)
        machineSettings.setTabOrder(self.bedXLengthLineEdit, self.bedXOffsetLineEdit)
        machineSettings.setTabOrder(self.bedXOffsetLineEdit, self.bedYLengthLineEdit)
        machineSettings.setTabOrder(self.bedYLengthLineEdit, self.bedYOffsetLineEdit)
        machineSettings.setTabOrder(self.bedYOffsetLineEdit, self.maxXTravelLineEdit)
        machineSettings.setTabOrder(self.maxXTravelLineEdit, self.maxYTravelLineEdit)
        machineSettings.setTabOrder(self.maxYTravelLineEdit, self.maxZTravelLineEdit)
        machineSettings.setTabOrder(self.maxZTravelLineEdit, self.maxSpindleSpeedLineEdit)

    def retranslateUi(self, machineSettings):
        machineSettings.setWindowTitle(_translate("machineSettings", "Macnine Settings", None))
        self.groupBox.setTitle(_translate("machineSettings", "Bed Dimensions", None))
        self.bedXLengthLabel.setText(_translate("machineSettings", "Bed X Length", None))
        self.bedYLengthLabel.setText(_translate("machineSettings", "Bed Y Length", None))
        self.bedXOffsetLabel.setText(_translate("machineSettings", "Bed X Offset", None))
        self.bedYOffsetLabel.setText(_translate("machineSettings", "Bed Y Offset", None))
        self.groupBox_2.setTitle(_translate("machineSettings", "Limits", None))
        self.maxXTravelLabel.setText(_translate("machineSettings", "Max X Travel", None))
        self.maxYTravelLabel.setText(_translate("machineSettings", "Max Y Travel", None))
        self.maxZTravelLabel.setText(_translate("machineSettings", "Max Z Travel", None))
        self.maxSpindleSpeedLabel.setText(_translate("machineSettings", "Max Spindle Speed", None))

