# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 20:07:19 2014

@author: Dirk Van Essendelft
"""

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
        
        
