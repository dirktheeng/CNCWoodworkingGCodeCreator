# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 20:07:19 2014

@author: Dirk Van Essendelft
"""

import datetime
from utilities import utilities

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
    def __init__(self,Table_Offset = (0,0,0), Table_Datum = (0,0,0),parent = None):
        self.parent = parent
        self.util = utilities()
        self._Table_Offset = Table_Offset
        self._Table_Datum = Table_Datum
        self._g_rapid = 'G0'
        self._g_feed = 'G1'
        self._new_line = '\n'
        self._x = 'X'
        self._y = 'Y'
        self._z = 'Z'
        self._feed = 'F'
        self._speed = 'S'
        self._preamble = self.util.readTextFile('Preamble.txt')
        self._postamble = self.util.readTextFile('Postamble.txt')
        self._pause = 'G04P'
        self._spindleOnCW = 'M03'
        self._spindleOnCCW = 'M04'
        self._spindleOff = 'M05'
    
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
            return self._g_rapid + self.__codeXYZ(XYZ) + self._new_line
        safeZ = str(safeZ)
        XY = (XYZ[0],XYZ[1])
        Z = XYZ[2]
        gcode = self._g_rapid + self.__codeZ(safeZ) + self._new_line
        gcode += self._g_rapid + self.__codeXY(XY) + self._new_line
        gcode += self._g_rapid + self.__codeZ(Z) + self._new_line
        return gcode
        
        
    def addPreamble(self):
        gcode = '(Begin Preamble)' + self._new_line
        gcode += '(Created by CNC Woodworker g-Code Creator)' + self._new_line
        gcode += '(CNC Woodworker written by Dirk Van Essendelft)' + self._new_line
        gcode += '(g-code created at ' + datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y") + ')' + self._new_line
        gcode += self._preamble + self._new_line
        gcode += '(End Preamble)' + self._new_line
        return gcode
        
    def addPostamble(self):
        gcode = '(Begin Postamble)' + self._new_line
        gcode += self._postamble + self._new_line
        gcode += '(End Postamble)' + self._new_line
        return gcode
        
    def lineFeed(self,XYZ,feedrate = None,speed = None):
        XYZ = self.__translateXYZ(XYZ)
        gcode = self._g_feed + self.__codeXYZ(XYZ)
        if feedrate != None:
            gcode += self._feed + str(feedrate)
            
        if speed != None:
            gcode += self._speed + str(speed)
            
        gcode += self._new_line
        return gcode
        
    def addFeedandSpeed(self,feedrate = None, speed = None):
        gcode = ''
        if feedrate != None:
            gcode += self._feed + str(feedrate)
        if speed != None:
            gcode += self._speed + str(speed)
        return gcode
        
    def turnSpindleOn(self, direction = 'CW', pause = 5):
        gcode = ''
        if direction == 'CW':
            gcode += self._spindleOnCW + self._new_line
        else:
            gcode += self._spindleOnCCW + self._new_line
        if pause > 0:
            gcode += self._pause + str(pause) + self._new_line
        return gcode
        
    def turnSpindleOff(self):
        return self._spindleOff + self._new_line
        
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
        
        
