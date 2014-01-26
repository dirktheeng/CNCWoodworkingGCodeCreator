# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:02:18 2014

@author: Dirk Van Essendelft
"""

import sys, os, csv, json
from PyQt4 import QtGui, QtCore
from main import Ui_MainWindow
from machineSettingsDialog import Ui_machineSettings
from gridSettingsDialog import Ui_gridSettings


class CNCWWCreator(QtGui.QMainWindow):
    def __init__(self,parent=None):
        util = utilities(self)
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.vars = globalVars()
        self.connectActions()
        self.vars.machineSettings = util.getSettings('machineSettings.txt')
        self.vars.gridSettings = util.getSettings('gridSettings.txt')
        self.vars.moduleList = []
        for i in range(1000):
            mName = str(self.ui.moduleTabWidget.tabText(i))
            if mName == '':
                break
            else:
                self.vars.moduleList.append(mName.replace(' ',''))
        for mod in self.vars.moduleList:
            cmd = 'self.'+mod+' = moduleBase("'+mod+'",parent = self)'
            exec(cmd)
        
    def connectActions(self):
        """
        Connect the user interface controls to the logic
        """
        self.ui.actionMachine.triggered.connect(self.machineSettinsDialog)
        self.ui.actionGrid.triggered.connect(self.gridSettinsDialog)
        self.ui.actionExit.triggered.connect(self.mainQuit)
        self.ui.generateGCodePushButton.clicked.connect(self.onGenerateGCodePressed)
        
    def machineSettinsDialog(self):
        machineSettings = machineSettingsDialog(parent = self)
        machineSettings.exec_()
        
    def gridSettinsDialog(self):
        gridSettings = gridSettingsDialog(parent = self)
        gridSettings.exec_()
        
    def mainQuit(self):
        pass
    
    def onGenerateGCodePressed(self):
        currentModuleIndex = self.ui.moduleTabWidget.currentIndex()
        currentModule = str(self.ui.moduleTabWidget.tabText(currentModuleIndex)).replace(' ','')
        cmd = 'self.'+currentModule+'.saveModuleEntries()'
        exec(cmd)
        cmd = 'self.'+currentModule+'.produceGCode()'
        exec(cmd)
        
class machineSettingsDialog(QtGui.QDialog):
    def __init__(self,parent=None):
        self.parent = parent
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_machineSettings()
        self.ui.setupUi(self)
        self.util =utilities(parent = self)
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
        self.parent.vars.machineSettings = self.util.getQObjectDict(QtGui.QLineEdit)
        
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
            
            
class globalVars():
    def __init__(self,parent=None):
        self.parent = parent
        
class moduleBase():
    '''
    This class handles all functions related to the module and should only be
    enstantiated from the main program
    '''
    def __init__(self,name,parent=None):
        self.parent = parent
        self.name = name
        self.loadSetupHTML()
        self.setupXYComboBox()
        self.util = utilities() # this is here so the methods appear in text completion
        cmd = 'self.util = utilities(parent = self.parent.ui.tab_'+name+')'
        exec(cmd)
        self.parentUtil = utilities(parent=parent)
        self.parentUtil.setAllLineEditValidator2Double(listLineEdit = self.util.getQObjectNames(QtGui.QLineEdit))
        self.loadModuleEntries()
        
    def loadSetupHTML(self):
        try:
            with open(self.name+'_Setup.htm','r') as htmlFile:
                htmlText = htmlFile.read()
        except:
            QtGui.QMessageBox.information(self.parent,'File Error',self.name+'_Setup.htm was not found')
            htmlText = None
        if htmlText != None:
            cmd = 'self.parent.ui.textBrowser_'+self.name+'_Setup.setHtml(htmlText)'
            try:
                exec(cmd)
            except:
                pass
            
    def setupXYComboBox(self):
        try:
            cmd = 'self.parent.ui.comboBox_'+self.name+'_SelectXYAxis.addItems(["X Axis","Y Axis"])'
            exec(cmd)
        except:
            pass
                
    def saveModuleEntries(self):
        fileName = self.name+'_ModuleEntries.txt'
        self.buildModuleDict()
        self.util.dumpSettings(fileName,settingsDict = self.moduleDict)
        
    def buildModuleDict(self):
        moduleEntryDict = self.util.getQObjectDict(QtGui.QLineEdit)
        moduleComboDict = self.util.getQObjectDict(QtGui.QComboBox)
        moduleSpinBox = self.util.getQObjectDict(QtGui.QSpinBox)
        self.moduleDict = dict(moduleEntryDict.items() + moduleComboDict.items() + moduleSpinBox.items())
        
    def loadModuleEntries(self):
        fileName = self.name+'_ModuleEntries.txt'
        self.parentUtil.populateInfo(fileName)
        self.buildModuleDict()
        
    def produceGCode(self):
        '''
        This function handles producing the g-code for all modules
        '''
        self.buildModuleDict()
        machineSettings = self.parent.vars.machineSettings
        gridSettings = self.parent.vars.gridSettings
        Table_Offset = (float(machineSettings["bedXOffsetLineEdit"]),float(machineSettings["bedYOffsetLineEdit"]),0)
        motion = gMotion(Table_Offset=Table_Offset)
        gcode = ''
        for k,v in self.moduleDict.items():
            k = k.split('LineEdit')[0]
            k = k.split('SpinBox')[0]
            if k.rfind("_"+self.name+"_") != -1:
                k = k.split("_"+self.name+"_")[1]
            cmd = k + " = float(" + str(v) + ')'
            print k, v
            exec(cmd)  
        if self.name == 'Jointer':
            startAxiDist = distFromOrigin + materialLength + overTravel
            finishAxiDist = distFromOrigin - overTravel
            
            cutPasses = int(cutPasses)
            if cutPasses > 0:
                cutPassDZ = (materialThickness -  zAxisOffset)/ (cutPasses)
                if SelectXYAxis == 0:
                    startXYZ_cut = [startAxiDist,cutOffset - toolDiameter/2.0,zAxisOffset]
                    endXYZ_cut = [finishAxiDist,cutlOffset - toolDiameter/2.0,zAxisOffset]
                else:
                    startXYZ_cut = [cutOffset - toolDiameter/2.0,finishAxiDist,zAxisOffset]
                    endXYZ_cut = [cutOffset - toolDiameter/2.0,startAxiDist,zAxisOffset]
                    
                for i in range(cutPasses):
                    zCutHeight = materialThickness - cutPassDZ*(i+1)
                    startXYZ_cut[2] = zCutHeight
                    endXYZ_cut[2] = zCutHeight
                    gcode += motion.rapid(startXYZ_cut,safeZ = safeZHeight)
                    gcode += motion.lineFeed(endXYZ_cut)
                    
            
            if SelectXYAxis == 0:
                startXYZ_final = [startAxiDist,finalOffset - toolDiameter/2.0,zAxisOffset]
                endXYZ_final = [finishAxiDist,finalOffset - toolDiameter/2.0,zAxisOffset]
            else:
                startXYZ_final = [finalOffset - toolDiameter/2.0,finishAxiDist,zAxisOffset]
                endXYZ_final = [finalOffset - toolDiameter/2.0,startAxiDist,zAxisOffset]
            
            for i in range(int(finalPasses)):
                gcode += motion.rapid(startXYZ_final,safeZ = safeZHeight)
                gcode += motion.lineFeed(endXYZ_final)
            
            print gcode
            
            
        else:
            return None
        
class gMotion():
    '''
    This class contains the common g-code generation functions.
    
    If Table_Offset and Table_Datum are passed in, the class functions will
    account for that so those distances in the position calculations.
    
    The table offset are the x,y,z positions of the corner of the bed of the
    mill relative to the home limits
    
    The table datum is the position of the desired datum relative to the corner
    of the bed of the mill
    '''
    def __init__(self,Table_Offset = (0,0,0), Table_Datum = (0,0,0)):
        self._Table_Offset = Table_Offset
        self._Table_Datum = Table_Datum
        self._g_rapid = 'G0'
        self._g_feed = 'G1'
        self._new_line = '\n'
        self._x = 'X'
        self._y = 'Y'
        self._z = 'Z'
    
    def rapid(self,XYZ,safeZ = None):
        '''
        accepts a list or tuple (items can be int or double) of x, y, z
        coordinates (XYZ) and an optional safe Z height (safeZ, int double or str).  
        
        If safeZ is specifid the function will produce gcode that will raise 
        the tool to the specified height traverse in the XY plane and then lower
        to the specified Z in XYZ
        
        It is HIGHLY recommended that safeZ is specified
        '''
        XYZ = self.__translateXYZ(XYZ)

        if safeZ == None:
            return self._g_rapid + self.__code(XYZ) + self._new_line
        safeZ = str(safeZ)
        XY = (XYZ[0],XYZ[1])
        Z = XYZ[2]
        gcode = self._g_rapid + self.__codeZ(safeZ) + self._new_line
        gcode += self._g_rapid + self.__codeXY(XY) + self._new_line
        gcode += self._g_rapid + self.__codeZ(Z) + self._new_line
        return gcode
        
        
    def lineFeed(self,XYZ):
        XYZ = self.__translateXYZ(XYZ)
        return self._g_feed + self.__codeXYZ(XYZ) + self._new_line
        
    def __translateXYZ(self,XYZ):
        '''
        This function translates the xyz coordinates for all movement functions
        to the coordinate system relative to the home position
        
        XYZ should be a list or tuple of double or int where the order is x, y, z
        '''
        pos = [0,0,0]
#        print self._Table_Datum
#        print self._Table_Offset
        for i in range(3):
            pos[i] = self._Table_Datum[i] + self._Table_Offset[i]+XYZ[i]
            
        return pos
            
        
        
    def __codeXYZ(self,XYZ):
        '''
        codes a list or tuple of x, y, z cordinates (XYZ) into gcode format
        '''
        return self._x + str(XYZ[0]) + self._y + str(XYZ[1]) + self._z + str(XYZ[2])
        
    def __codeXY(self,XY):
        '''
        codes a list or tuple of x, y cordinates (XY) into gcode format
        '''
        return self._x + str(XY[0]) + self._y + str(XY[1])
        
    def __codeZ(self,Z):        
        '''
        codes an int or double z cordinate (Z) into gcode format
        '''
        return self._z + str(Z)
        
        

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    mainapp = CNCWWCreator()
    mainapp.show()
    sys.exit(app.exec_())
