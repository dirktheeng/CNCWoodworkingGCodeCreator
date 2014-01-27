# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 20:11:14 2014

@author: Dirk Van Essendelft
"""

from PyQt4 import QtGui, QtCore
import json

class utilities():
    def __init__(self,parent=None):
        self.parent = parent

    def getQObjectNames(self,QObject, CutUnwanted = True):
        listQQObject = self.parent.findChildren(QObject)
        listQObject =  [str(t.objectName()) for t in listQQObject]
        if CutUnwanted:
            listQObjectFinal = []
            for item in listQObject:
                if item.rfind('spinbox_lineedit') == -1:
                    listQObjectFinal.append(item)
            return listQObjectFinal
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
                if key.upper().rfind('LINEEDIT') != -1:
                    try:
                        cmd = 'self.parent.ui.'+key+'.setText("'+val+'")'
                        exec(cmd)
                    except:
                        print 'problem loading line edit'
                        print cmd
                elif key.upper().rfind('COMBOBOX') != -1:
                    try:
                        cmd = 'self.parent.ui.'+key+'.setCurrentIndex('+val+')'
                        exec(cmd)
                    except:
                        print 'problem loading combo box'
                        print cmd
                elif key.upper().rfind('SPINBOX') != -1:
                    try:
                        cmd = 'self.parent.ui.'+key+'.setValue('+val+')'
                        exec(cmd)
                    except:
                        print 'problem loading spin box'
                        print cmd
                
    def dumpSettings(self,fileName,settingsDict = None):
        if settingsDict == None:
            settingsDict = self.getQObjectDict(QtGui.QLineEdit)
        with open(fileName,'w') as outfile:
            json.dump(settingsDict, outfile)
            
    def dumpTextEdit(self,filename,QTextObject):
        text = QTextObject.toPlainText()
        with open(filename,'w') as txtFile:
            txtFile.write(text)
            
    def loadTextEdit(self,filename,QTextObject):
        with open(filename,'r') as txtFile:
            text = txtFile.read()
        QTextObject.setPlainText(text)
            
    def getSettings(self,fileName):
        try:
            with open(fileName,'r') as settings:
                jdict = json.load(settings)
                strDict = {}
                for k,v in jdict.items():
                    strDict[str(k)] = str(v)
                return strDict
        except:
            return None
            
    def setAllLineEditValidator2Double(self, listLineEdit = None):
        if listLineEdit == None:
            listLineEdit = self.getQObjectNames(QtGui.QLineEdit)
        for item in listLineEdit:
            cmd = 'self.parent.ui.'+item+'.setValidator(QtGui.QDoubleValidator())'
            exec(cmd)