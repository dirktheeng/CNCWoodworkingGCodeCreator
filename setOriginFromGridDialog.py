# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setOriginFromGridDialog.ui'
#
# Created: Mon Feb 10 15:33:12 2014
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

class Ui_setOriginFromGrid(object):
    def setupUi(self, setOriginFromGrid):
        setOriginFromGrid.setObjectName(_fromUtf8("setOriginFromGrid"))
        setOriginFromGrid.resize(326, 154)
        self.gridLayout = QtGui.QGridLayout(setOriginFromGrid)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(setOriginFromGrid)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.xGridPositionLabel = QtGui.QLabel(setOriginFromGrid)
        self.xGridPositionLabel.setObjectName(_fromUtf8("xGridPositionLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.xGridPositionLabel)
        self.xGridPositionSpinBox = QtGui.QSpinBox(setOriginFromGrid)
        self.xGridPositionSpinBox.setObjectName(_fromUtf8("xGridPositionSpinBox"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.xGridPositionSpinBox)
        self.yGridPositionLabel = QtGui.QLabel(setOriginFromGrid)
        self.yGridPositionLabel.setObjectName(_fromUtf8("yGridPositionLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.yGridPositionLabel)
        self.yGridPositionSpinBox = QtGui.QSpinBox(setOriginFromGrid)
        self.yGridPositionSpinBox.setObjectName(_fromUtf8("yGridPositionSpinBox"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.yGridPositionSpinBox)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.yNegativeRadioButton = QtGui.QRadioButton(setOriginFromGrid)
        self.yNegativeRadioButton.setObjectName(_fromUtf8("yNegativeRadioButton"))
        self.yPosNeg_buttonGroup = QtGui.QButtonGroup(setOriginFromGrid)
        self.yPosNeg_buttonGroup.setObjectName(_fromUtf8("yPosNeg_buttonGroup"))
        self.yPosNeg_buttonGroup.addButton(self.yNegativeRadioButton)
        self.gridLayout_3.addWidget(self.yNegativeRadioButton, 1, 2, 1, 1)
        self.xNegativeRadioButton = QtGui.QRadioButton(setOriginFromGrid)
        self.xNegativeRadioButton.setObjectName(_fromUtf8("xNegativeRadioButton"))
        self.xPosNeg_buttonGroup = QtGui.QButtonGroup(setOriginFromGrid)
        self.xPosNeg_buttonGroup.setObjectName(_fromUtf8("xPosNeg_buttonGroup"))
        self.xPosNeg_buttonGroup.addButton(self.xNegativeRadioButton)
        self.gridLayout_3.addWidget(self.xNegativeRadioButton, 0, 2, 1, 1)
        self.xPositiveRadioButton = QtGui.QRadioButton(setOriginFromGrid)
        self.xPositiveRadioButton.setChecked(True)
        self.xPositiveRadioButton.setObjectName(_fromUtf8("xPositiveRadioButton"))
        self.xPosNeg_buttonGroup.addButton(self.xPositiveRadioButton)
        self.gridLayout_3.addWidget(self.xPositiveRadioButton, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(setOriginFromGrid)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(setOriginFromGrid)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.yPositiveRadioButton = QtGui.QRadioButton(setOriginFromGrid)
        self.yPositiveRadioButton.setChecked(True)
        self.yPositiveRadioButton.setObjectName(_fromUtf8("yPositiveRadioButton"))
        self.yPosNeg_buttonGroup.addButton(self.yPositiveRadioButton)
        self.gridLayout_3.addWidget(self.yPositiveRadioButton, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)

        self.retranslateUi(setOriginFromGrid)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), setOriginFromGrid.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), setOriginFromGrid.reject)
        QtCore.QMetaObject.connectSlotsByName(setOriginFromGrid)

    def retranslateUi(self, setOriginFromGrid):
        setOriginFromGrid.setWindowTitle(_translate("setOriginFromGrid", "Dialog", None))
        self.xGridPositionLabel.setText(_translate("setOriginFromGrid", "X Grid Position", None))
        self.yGridPositionLabel.setText(_translate("setOriginFromGrid", "Y Grid Position", None))
        self.yNegativeRadioButton.setText(_translate("setOriginFromGrid", "Negative", None))
        self.xNegativeRadioButton.setText(_translate("setOriginFromGrid", "Negative", None))
        self.xPositiveRadioButton.setText(_translate("setOriginFromGrid", "Positive", None))
        self.label_3.setText(_translate("setOriginFromGrid", "Side of Pin: X Axis", None))
        self.label_5.setText(_translate("setOriginFromGrid", "Side of Pin: Y Axis", None))
        self.yPositiveRadioButton.setText(_translate("setOriginFromGrid", "Positive", None))

