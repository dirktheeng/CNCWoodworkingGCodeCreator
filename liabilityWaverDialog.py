# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'liabilityWaverDialog.ui'
#
# Created: Fri Feb 14 23:36:21 2014
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

class Ui_liabilityWaver(object):
    def setupUi(self, liabilityWaver):
        liabilityWaver.setObjectName(_fromUtf8("liabilityWaver"))
        liabilityWaver.resize(710, 458)
        liabilityWaver.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(liabilityWaver)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textBrowser = QtGui.QTextBrowser(liabilityWaver)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.buttonBox = QtGui.QDialogButtonBox(liabilityWaver)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(liabilityWaver)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), liabilityWaver.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), liabilityWaver.reject)
        QtCore.QMetaObject.connectSlotsByName(liabilityWaver)

    def retranslateUi(self, liabilityWaver):
        liabilityWaver.setWindowTitle(_translate("liabilityWaver", "Liability Waver", None))
        self.textBrowser.setHtml(_translate("liabilityWaver", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Liability Waver</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2,sans-serif\'; font-size:10pt;\">The product of this software is text files which contain gcode that may or may not be suitable to use with CNC machines and equipment. If gcode is not suitable for a CNC machine or equipment, it can cause damage to equipment and parts as well as personnel injuries which can vary in severity and could include death. Determination of the suitability for use on any CNC machines or equipment is solely the responsibility of the users of this software (you).  This means that the users of this software (you) should carefully inspect the gcode produced from this sofware and know every aspect of the gcode BEFORE you use it on any CNC equipment.  Because there are aspects of gcode which are specific to each cnc machine or equipment, gcode should never be directly transferred from one machine to another.  Users of this software should only use gcode from this software on the same machine for which the software is setup.  The authors of this software offer no warranty and no guarantee for any of the gcode produced from this software.  </span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2,sans-serif\'; font-size:10pt;\">By activating the &quot;OK&quot; button in this dialog, you are agreeing that the authors of this software are to be held free from any and all liability related to the use of the gcode produced from this software on any CNC machine or equipment. In Addition should you activate the &quot;OK&quot; button in this dialog, you agree to take complete liability for the use of the gcode you produce from this software which includes any and all equipment and/or part damage and/or injury and/or death to yourself and/or others due to improper gcode statements which make the gcode unsuitable for use with CNC equipment or machines.  Further, by activating the &quot;OK&quot; button in this dialog, you agree not to transfer and product gcode to any other equipment but that which has been properly setup in the software.  Finally, by activating the &quot;OK&quot; button in this dialog, you are agreeing not to remove this liability statement from the software.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2,sans-serif\'; font-size:10pt;\">If you cannot agree to these liability terms, you must activate the &quot;I Disagree&quot; button in this dialog and never use this program or any part of it in any way, shape, or form.</span><span style=\" font-size:8pt;\"> </span></p></body></html>", None))

