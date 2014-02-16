# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 20:11:14 2014

@author: Dirk Van Essendelft

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
import json
import os

class utilities():
    def __init__(self,parent=None):
        self.parent = parent

    def getQObjectNames(self,QObject, CutUnwanted = True, returnQObject = False):
        listQQObject = self.parent.findChildren(QObject)
        listQObject =  [str(t.objectName()) for t in listQQObject]
        if CutUnwanted:
            listQObjectFinal = []
            listQQObjectFinal = []
            for i,item in enumerate(listQObject):
                if item.rfind('spinbox_lineedit') == -1:
                    listQObjectFinal.append(item)
                    listQQObjectFinal.append(listQQObject[i])
            if returnQObject:
                return listQObjectFinal, listQQObjectFinal
            else:
                return listQObjectFinal
        else:
            if returnQObject:
                return listQObject, listQQObject
            else:
                return listQObject
 
    def getSpinBoxNames(self):
        listSpinBoxQObject = self.parent.findChildren(QtGui.QSpinBox)
        return [str(t.objectName()) for t in listSpinBoxQObject]
        
    def getQObjectVals(self,QObject):
        QObjectChildren = self.parent.findChildren(QObject)
        if QObject == QtGui.QLineEdit or QObject == QtGui.QSpinBox:
            return [str(t.text()) for t in QObjectChildren]
        elif QObject == QtGui.QComboBox:
            return [t.currentIndex() for t in QObjectChildren]
        elif QObject == QtGui.QButtonGroup:
            return [str(t.checkedButton().text()) for t in QObjectChildren]
        elif QObject == QtGui.QRadioButton or QObject == QtGui.QCheckBox:
            return [t.isChecked() for t in QObjectChildren]
        else:
            return None
    
    def getQObjectDict(self,QObject):
        QObjectNames = self.getQObjectNames(QObject,CutUnwanted = False)
        QObjectVals = self.getQObjectVals(QObject)
        comboBoxDict = {}
        for i,item in enumerate(QObjectNames):
            if item.rfind('spinbox_lineedit') == -1:
                comboBoxDict[item] = QObjectVals[i]
        return comboBoxDict
        
    def populateInfo(self,fileName):
        settings = self.getSettings(fileName)
        if settings != None:
            for key,val in settings.items():
                fieldName = self.stripQObjectFromName([key])[0]
                try:
                    if key.upper().rfind('LINEEDIT') != -1:
                        self.parent._lineEdits[fieldName].setText(val)
                    elif key.upper().rfind('COMBOBOX') != -1:
                        self.parent._comboBoxes[fieldName].setCurrentIndex(int(val))
                    elif key.upper().rfind('SPINBOX') != -1:
                        self.parent._spinBoxes[fieldName].setValue(float(val))
                    elif key.upper().rfind('RADIOBUTTON') != -1:
                        self.parent._radioButtons[fieldName].setChecked(val == 'True')
                    elif key.upper().rfind('CHECKBOX') != -1:
                        self.parent._checkBoxes[fieldName].setChecked(val == 'True')
                except:
                    print 'problem setting ' + fieldName
                
    def dumpSettings(self,fileName,settingsDict = None):
        if settingsDict == None:
            settingsDict = self.getQObjectDict(QtGui.QLineEdit)
        with open(fileName,'w') as outfile:
            json.dump(settingsDict, outfile)
            
    def dumpTextEdit(self,fileName,QTextObject):
        text = QTextObject.toPlainText()
        self.saveTextFile(fileName,text)
            
    def loadTextEdit(self,fileName,QTextObject):
        text = self.readTextFile(fileName)
        QTextObject.setPlainText(text)
            
    def getSettings(self,fileName):
        try:
            jdict = self.readJSONFile(fileName)
            strDict = {}
            for k,v in jdict.items():
                strDict[str(k)] = str(v)
            return strDict
        except:
            return None
            
    def setAllLineEditValidator2Double(self, listLineEdit = None):
        if listLineEdit == None:
            listLineEdit = self.parent._lineEdits.keys()
        for item in listLineEdit:
            self.parent._lineEdits[item].setValidator(QtGui.QDoubleValidator())
#            cmd = 'self.parent.ui.'+item+'.setValidator(QtGui.QDoubleValidator())'
#            exec(cmd)
            
    def readTextFile(self,fileName):
        with open(fileName,'r') as txtFile:
            txt = txtFile.read()
        return txt
        
    def saveTextFile(self,fileName,txt):
        with open(fileName,'w') as txtFile:
            txtFile.write(txt)
            
    def readJSONFile(self,fileName):
        with open(fileName,'r') as settings:
            jsonDict = json.load(settings)
        return jsonDict
        
    def saveGCode(self,gcode, setupGCode, folderPath = None, ModuleName = 'Jointer',filter = 'Text (*.txt)'):
        if folderPath == None:
            folderPath = os.getcwd()
        
        caption = 'Save gCode from the ' + ModuleName + ' Module'
        
        include = not(QtGui.QMessageBox.question(self.parent,'Include Setup','Do you want to include the setup gcode?','Yes',button1Text = 'No'))
        filePath = str(QtGui.QFileDialog.getSaveFileName(self.parent,directory = folderPath,caption = caption, filter = filter))
        path, fileName = os.path.split(filePath)
        fileNameGCode = ModuleName + '_' + fileName
        filePath = os.path.join(path,fileNameGCode)
        self.saveTextFile(filePath,gcode)
        if include:
            fileNameSetup = ModuleName + '_Setup_' + fileName
            filePath = os.path.join(path,fileNameSetup)
            self.saveTextFile(filePath,setupGCode)
        
    def readDefaultGCodeDirectory(self):
        try:
            with open('defaultGCodeDirectory.txt','r') as dgd:
                txt = dgd.read()
                return txt
        except:
            return os.getcwd()

    def setToFalseIfTrue(self,QButton):
        if QButton.isChecked():
            QButton.setCheckState(False)
            
    def returnChildrenDictionary(self,QObject, searchString = None):
        Names, QObjects = self.getQObjectNames(QObject,returnQObject = True)
        Names = self.stripQObjectFromName(Names)
        childDict = dict(zip(Names,QObjects))
        if searchString == None:
            return childDict
        else:
            searchDict = {}
            for k,v in childDict.items():
                if k.rfind(searchString) != -1:
                    searchDict[k] = v
            return searchDict
            
    def getCurrentModuleName(self):
        '''
        this module is only used if the parent is the main class
        '''
        currentModuleIndex = self.parent.ui.moduleTabWidget.currentIndex()
        currentModule = str(self.parent.ui.moduleTabWidget.tabText(currentModuleIndex)).replace(' ','')
        return currentModule
        
    def stripQObjectFromName(self,Names):
        Names = [t.split('LineEdit')[0] for t in Names]
        Names = [t.split('SpinBox')[0] for t in Names]
        Names = [t.split('CheckBox')[0] for t in Names]
        Names = [t.split('ComboBox')[0] for t in Names]
        Names = [t.split('TextBrowser')[0] for t in Names]
        Names = [t.split('RadioButton')[0] for t in Names]
        return Names
            