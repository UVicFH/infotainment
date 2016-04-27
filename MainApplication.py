from PyQt5.QtCore import QUrl, QObject, QVariant, QRunnable, QCoreApplication, QThreadPool
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtGui import QColor
from PyQt5.QtQuick import QQuickView
import os
import sys
import signal
import time
import threading
from UpdateThread import UpdateThread

def handler(signum, frame):
    print("ayyyy")
    sys.exit()

signal.signal(signal.SIGINT, handler)

class MainApplication(QQuickView):  
    GOOD = 0
    BAD = 1
    WARN = 2

    fuelRed = ["fuel_r1","fuel_r2"]
    fuelYellow = ["fuel_y1","fuel_y2","fuel_y3","fuel_y4","fuel_y5","fuel_y6","fuel_y7","fuel_y8"]
    fuelGreen = ["fuel_g1","fuel_g2","fuel_g3","fuel_g4","fuel_g5","fuel_g6","fuel_g7","fuel_g8","fuel_g9","fuel_g10","fuel_g11","fuel_g12","fuel_g13","fuel_g14","fuel_g15","fuel_g16","fuel_g17","fuel_g18","fuel_g19","fuel_g20"]

    socRed = ["soc_r1","soc_r2"]
    socYellow = ["soc_y1","soc_y2","soc_y3","soc_y4","soc_y5","soc_y6","soc_y7","soc_y8"]
    socGreen = ["soc_g1","soc_g2","soc_g3","soc_g4","soc_g5","soc_g6","soc_g7","soc_g8","soc_g9","soc_g10","soc_g11","soc_g12","soc_g13","soc_g14","soc_g15","soc_g16","soc_g17","soc_g18","soc_g19","soc_g20"]

    def __init__(self,parent=None):
        super(MainApplication, self).__init__(parent)
        #self.resize(1200, 900) # TODO update to get screen size for full
        
        self.setSource(QUrl.fromLocalFile(os.path.join(os.path.dirname(__file__),'qml/Display_rev_1.qml')))
        self.setupUpdateThread()  
        self.qml = self.rootObject()
       


    def updateTachNeedle(self, tachRPM):
        #Major ticks are spaced by 20 degrees
        goToAngle = (tachRPM*-0.02)
        self.qml.setProperty("tachNeedleAngle", QVariant(int(goToAngle)))

    def updateSpeed(self, pSPEED):  
        self.qml.setProperty("speed", QVariant(str(pSPEED)))


    def updateESS_SOC(self, pESS_SOC):
        #Pass in the soc percent, this will do the rest for soc 
        #and target soc soc_y1
        def turn_off(pBar_array):
            for bar in pBar_array:
                self.qml.setProperty(bar, QVariant(0))

        pESS_SOC = int(pESS_SOC)
        
        if(pESS_SOC<=10):
            turn_off(self.socGreen)
            turn_off(self.socYellow)
            
            if(pESS_SOC==0):
                self.qml.setProperty("soc_r1", QVariant(0))
            else:
                self.qml.setProperty("soc_r1", QVariant(1))


            if(pESS_SOC>5):
                self.qml.setProperty("soc_r2", QVariant(1))
            else:
                self.qml.setProperty("soc_r2", QVariant(0))

        if(pESS_SOC>10 and pESS_SOC<=40):
            turn_off(self.socGreen)
            turn_off(self.socRed)

            self.qml.setProperty("soc_y1", QVariant(1))
            self.qml.setProperty("soc_y2", QVariant(1))
            self.qml.setProperty("soc_y3", QVariant(1))

            if(pESS_SOC>15):
                self.qml.setProperty("soc_y4", QVariant(1))
            else:
                self.qml.setProperty("soc_y4", QVariant(0))

            if(pESS_SOC>20):
                self.qml.setProperty("soc_y5", QVariant(1))
            else:
                self.qml.setProperty("soc_y5", QVariant(0))

            if(pESS_SOC>25):
                self.qml.setProperty("soc_y6", QVariant(1))
            else:
                self.qml.setProperty("soc_y6", QVariant(0))

            if(pESS_SOC>30):
                self.qml.setProperty("soc_y7", QVariant(1))
            else:
                self.qml.setProperty("soc_y7", QVariant(0))

            if(pESS_SOC>35):
                self.qml.setProperty("soc_y8", QVariant(1))
            else:
                self.qml.setProperty("soc_y8", QVariant(0))

        if(pESS_SOC>40):
            turn_off(self.socRed)
            turn_off(self.socYellow)
            
            self.qml.setProperty("soc_g1", QVariant(1))
            self.qml.setProperty("soc_g2", QVariant(1))
            self.qml.setProperty("soc_g3", QVariant(1))
            self.qml.setProperty("soc_g4", QVariant(1))
            self.qml.setProperty("soc_g5", QVariant(1))
            self.qml.setProperty("soc_g6", QVariant(1))
            self.qml.setProperty("soc_g7", QVariant(1))
            self.qml.setProperty("soc_g8", QVariant(1))
            self.qml.setProperty("soc_g9", QVariant(1))

            if(pESS_SOC>45):
                self.qml.setProperty("soc_g10", QVariant(1))
            else:
                self.qml.setProperty("soc_g10", QVariant(0))
            
            if(pESS_SOC>50):
                self.qml.setProperty("soc_g11", QVariant(1))
            else:
                self.qml.setProperty("soc_g11", QVariant(0))
            
            if(pESS_SOC>55):
                self.qml.setProperty("soc_g12", QVariant(1))
            else:
                self.qml.setProperty("soc_g12", QVariant(0))
            
            if(pESS_SOC>60):
                self.qml.setProperty("soc_g13", QVariant(1))
            else:
                self.qml.setProperty("soc_g13", QVariant(0))
            
            if(pESS_SOC>65):
                self.qml.setProperty("soc_g14", QVariant(1))
            else:
                self.qml.setProperty("soc_g14", QVariant(0))
            
            if(pESS_SOC>70):
                self.qml.setProperty("soc_g15", QVariant(1))
            else:
                self.qml.setProperty("soc_g15", QVariant(0))
            
            if(pESS_SOC>75):
                self.qml.setProperty("soc_g16", QVariant(1))
            else:
                self.qml.setProperty("soc_g16", QVariant(0))
            
            if(pESS_SOC>80):
                self.qml.setProperty("soc_g17", QVariant(1))
            else:
                self.qml.setProperty("soc_g17", QVariant(0))
            
            if(pESS_SOC>85):
                self.qml.setProperty("soc_g18", QVariant(1))
            else:
                self.qml.setProperty("soc_g18", QVariant(0))
            
            if(pESS_SOC>90):
                self.qml.setProperty("soc_g19", QVariant(1))
            else:
                self.qml.setProperty("soc_g19", QVariant(0))
            
            if(pESS_SOC>95):
                self.qml.setProperty("soc_g20", QVariant(1))
            else:
                self.qml.setProperty("soc_g20", QVariant(0))

        # if(pESS_SOC<=10):
        #     turn_off(self.socGreen)
        #     turn_off(self.socYellow)
        #     counter = 0
        #     for bar in self.socRed:
        #         if(pESS_SOC>counter):
        #             self.qml.setProperty(self.bar, QVariant(1))
        #         else:
        #             self.qml.setProperty(self.bar, QVariant(0))
        #         counter+=5

        # if(pESS_SOC>10 and pESS_SOC<=40):
        #     turn_off(self.socGreen)
        #     turn_off(self.socRed)
        #     counter = 0
        #     for bar in self.socYellow:
        #         if(pESS_SOC>counter):
        #             self.qml.setProperty(bar, QVariant(1))
        #         else:
        #             self.qml.setProperty(bar, QVariant(0))
        #         counter+=5

        # if(pESS_SOC>40):
        #     turn_off(self.socRed)
        #     turn_off(self.socYellow)
        #     counter = 0
        #     for bar in self.socGreen:
        #         if(pESS_SOC>counter):
        #             self.qml.setProperty(bar, QVariant(1))
        #         else:
        #             self.qml.setProperty(bar, QVariant(0))
        #         counter+=5

    def updateGear(self, pGEAR):  
        self.qml.setProperty("gear", QVariant(str(pGEAR)))

    def updateSHIFT(self, pShift):
        if(pShift==1):
            self.qml.setProperty("tach_shift", QVariant(1))
            self.qml.setProperty("tach", QVariant(0))
        if(pShift==0):
            self.qml.setProperty("tach_shift", QVariant(0))
            self.qml.setProperty("tach", QVariant(1))

    def updateFUEL(self, pFUEL):
        #Pass in the fuel percent, this will do the rest for fuel 
        #and target fuel
        def turn_off(pBar_array):
            for bar in pBar_array:
                self.qml.setProperty(bar, QVariant(0))

        pFUEL = int(pFUEL)
        if(pFUEL<=10):
            turn_off(self.fuelGreen)
            turn_off(self.fuelYellow)
            
            if(pFUEL==0):
                self.qml.setProperty("fuel_r1", QVariant(0))
            else:
                self.qml.setProperty("fuel_r1", QVariant(1))


            if(pFUEL>5):
                self.qml.setProperty("fuel_r2", QVariant(1))
            else:
                self.qml.setProperty("fuel_r2", QVariant(0))

            # counter = 0
            # for bar in self.fuelRed:
            #     if(pFUEL>=counter):
            #         self.qml.setProperty(bar, QVariant(1))
            #     else:
            #         self.qml.setProperty(bar, QVariant(0))
            #     counter+=5

        if(pFUEL>10 and pFUEL<=40):
            turn_off(self.fuelGreen)
            turn_off(self.fuelRed)

            self.qml.setProperty("fuel_y1", QVariant(1))
            self.qml.setProperty("fuel_y2", QVariant(1))
            self.qml.setProperty("fuel_y3", QVariant(1))

            if(pFUEL>15):
                self.qml.setProperty("fuel_y4", QVariant(1))
            else:
                self.qml.setProperty("fuel_y4", QVariant(0))

            if(pFUEL>20):
                self.qml.setProperty("fuel_y5", QVariant(1))
            else:
                self.qml.setProperty("fuel_y5", QVariant(0))

            if(pFUEL>25):
                self.qml.setProperty("fuel_y6", QVariant(1))
            else:
                self.qml.setProperty("fuel_y6", QVariant(0))

            if(pFUEL>30):
                self.qml.setProperty("fuel_y7", QVariant(1))
            else:
                self.qml.setProperty("fuel_y7", QVariant(0))

            if(pFUEL>35):
                self.qml.setProperty("fuel_y8", QVariant(1))
            else:
                self.qml.setProperty("fuel_y8", QVariant(0))

            # counter = 0
            # for bar in self.fuelYellow:
            #     if(pFUEL>=counter):
            #         self.qml.setProperty(bar, QVariant(1))
            #     else:
            #         self.qml.setProperty(bar, QVariant(0))
            #     counter+=5

        if(pFUEL>40):
            turn_off(self.fuelRed)
            turn_off(self.fuelYellow)
            
            self.qml.setProperty("fuel_g1", QVariant(1))
            self.qml.setProperty("fuel_g2", QVariant(1))
            self.qml.setProperty("fuel_g3", QVariant(1))
            self.qml.setProperty("fuel_g4", QVariant(1))
            self.qml.setProperty("fuel_g5", QVariant(1))
            self.qml.setProperty("fuel_g6", QVariant(1))
            self.qml.setProperty("fuel_g7", QVariant(1))
            self.qml.setProperty("fuel_g8", QVariant(1))
            self.qml.setProperty("fuel_g9", QVariant(1))

            if(pFUEL>45):
                self.qml.setProperty("fuel_g10", QVariant(1))
            else:
                self.qml.setProperty("fuel_g10", QVariant(0))
            
            if(pFUEL>50):
                self.qml.setProperty("fuel_g11", QVariant(1))
            else:
                self.qml.setProperty("fuel_g11", QVariant(0))
            
            if(pFUEL>55):
                self.qml.setProperty("fuel_g12", QVariant(1))
            else:
                self.qml.setProperty("fuel_g12", QVariant(0))
            
            if(pFUEL>60):
                self.qml.setProperty("fuel_g13", QVariant(1))
            else:
                self.qml.setProperty("fuel_g13", QVariant(0))
            
            if(pFUEL>65):
                self.qml.setProperty("fuel_g14", QVariant(1))
            else:
                self.qml.setProperty("fuel_g14", QVariant(0))
            
            if(pFUEL>70):
                self.qml.setProperty("fuel_g15", QVariant(1))
            else:
                self.qml.setProperty("fuel_g15", QVariant(0))
            
            if(pFUEL>75):
                self.qml.setProperty("fuel_g16", QVariant(1))
            else:
                self.qml.setProperty("fuel_g16", QVariant(0))
            
            if(pFUEL>80):
                self.qml.setProperty("fuel_g17", QVariant(1))
            else:
                self.qml.setProperty("fuel_g17", QVariant(0))
            
            if(pFUEL>85):
                self.qml.setProperty("fuel_g18", QVariant(1))
            else:
                self.qml.setProperty("fuel_g18", QVariant(0))
            
            if(pFUEL>90):
                self.qml.setProperty("fuel_g19", QVariant(1))
            else:
                self.qml.setProperty("fuel_g19", QVariant(0))
            
            if(pFUEL>95):
                self.qml.setProperty("fuel_g20", QVariant(1))
            else:
                self.qml.setProperty("fuel_g20", QVariant(0))

            # counter = 0
            # for bar in self.fuelGreen:
            #     if(pFUEL>counter):
            #         self.qml.setProperty(bar, QVariant(1))
            #     else:
            #         self.qml.setProperty(bar, QVariant(0))
            #     counter+=5

        #if(pFUEL<self.updateThread.canMain.current_target_fuel):
        roundedFUEL = pFUEL - (pFUEL % 5)
        roundedTARGET = self.updateThread.canMain.current_target_fuel - (self.updateThread.canMain.current_target_fuel % 5)
        for num in range(1,21):
            if(num>=roundedFUEL/5 and num<=roundedTARGET/5):
                self.qml.setProperty("fuel_b"+str(num), QVariant(1))
            else:
                self.qml.setProperty("fuel_b"+str(num), QVariant(0))



    def updateMOTOR_TEMP_HACK(self, pDEGREES): 
        self.qml.setProperty("temp_text_text", QVariant(str(pDEGREES)))

    def updateMOTOR_TEMP(self, pMOTOR_TEMP): 
        if(pMOTOR_TEMP==self.GOOD): #GOOD
            self.qml.setProperty("temp_text_color", QVariant("#00FF00"))
        #    self.qml.setProperty("tempC", QVariant("#00FF00"))
        if(pMOTOR_TEMP==self.BAD): #BAD
            self.qml.setProperty("temp_text_color", QVariant("#FF0000"))
        #    self.qml.setProperty("tempC", QVariant("#FF0000"))     
        if(pMOTOR_TEMP==self.WARN): #WARN
            self.qml.setProperty("temp_text_color", QVariant("#FFFF00"))
        #    self.qml.setProperty("tempC", QVariant("#FFFF00"))
    '''
    Need:
    RPM
    speed
    ess soc
    gear
    shift

    target fuel
    fuel
    engine temp

    warn motor temp
    warn fuel low
    war ess over temp
    warn CAN down
    warn charging
    warn power on

    '''
    def updateMOTOR_OVER_TEMP(self, pSTATUS):
        if(pMOTOR_TEMP==self.GOOD): #GOOD
            self.qml.setProperty("motor_temp_red", QVariant(0)) 
            self.qml.setProperty("motor_temp_yellow", QVariant(0))
        if(pSTATUS==self.BAD): #BAD
            self.qml.setProperty("motor_temp_red", QVariant(1)) 
            self.qml.setProperty("motor_temp_yellow", QVariant(0))  
        if(pSTATUS==self.WARN): #WARN
            self.qml.setProperty("motor_temp_red", QVariant(0)) 
            self.qml.setProperty("motor_temp_yellow", QVariant(1))

    def updateFUEL_LOW(self, pSTATUS):
        if(pSTATUS==self.GOOD): #GOOD
            self.qml.setProperty("fuel_red", QVariant(0))
        if(pSTATUS==self.BAD): #BAD
            self.qml.setProperty("fuel_red", QVariant(1))

    def updateESS_TEMP(self, pESS_TEMP): 
        if(pESS_TEMP==self.GOOD): #GOOD
            self.qml.setProperty("ess_temp_red", QVariant(0))
        if(pESS_TEMP==self.BAD): #BAD
            self.qml.setProperty("ess_temp_red", QVariant(1))
 
    def updateCAN_DOWN(self, pCAN_Status):
        if(pCAN_Status==self.GOOD): #GOOD
            self.qml.setProperty("can_red", QVariant(0))
        if(pCAN_Status==self.BAD): #BAD
            self.qml.setProperty("can_red", QVariant(1))

    def updateCHARGING(self, pCHARGE_STATUS):
        if(pCHARGE_STATUS==self.GOOD): #GOOD
            self.qml.setProperty("power_on", QVariant(0))
        if(pCHARGE_STATUS==self.BAD): #BAD
            self.qml.setProperty("power_on", QVariant(1))
    
    def updateMOTOR_ON(self, pMOTOR_STATUS):
        if(pMOTOR_STATUS==self.GOOD): #GOOD
            self.qml.setProperty("can_red", QVariant(0))
        if(pMOTOR_STATUS==self.BAD): #BAD
            self.qml.setProperty("can_red", QVariant(1))

    def updateGLV_SOC(self, pGLV_SOC): 
        if(pGLV_SOC==self.GOOD): #GOOD
            self.qml.setProperty("glv_soc_red", QVariant(0))
        if(pGLV_SOC==self.BAD): #BAD
            self.qml.setProperty("glv_soc_red", QVariant(1))

    def mousePressEvent(self, QMouseEvent):
        # Used for finding mouse postions, strictly testing
        print(QMouseEvent.pos()) 
   
    def setupUpdateThread(self):  
        self.updateThread = UpdateThread()  
        
        # Connect our update function to the progress signal of the update thread  
        self.updateThread.speed.connect(self.updateSpeed)
        self.updateThread.gear.connect(self.updateGear)
        self.updateThread.temp_text.connect(self.updateMOTOR_TEMP_HACK)

        self.updateThread.shift.connect(self.updateSHIFT)
        
        self.updateThread.glv_soc.connect(self.updateGLV_SOC)
        self.updateThread.motor_temp.connect(self.updateMOTOR_OVER_TEMP)
        self.updateThread.ess_temp.connect(self.updateESS_TEMP)
        self.updateThread.charging.connect(self.updateCHARGING)
        self.updateThread.fuel_low.connect(self.updateFUEL_LOW)
        self.updateThread.CAN_down.connect(self.updateCAN_DOWN)
        self.updateThread.motor_on.connect(self.updateMOTOR_ON)
        
        self.updateThread.tachNeedle.connect(self.updateTachNeedle)
        
        self.updateThread.ess_soc.connect(self.updateESS_SOC)
        self.updateThread.fuel.connect(self.updateFUEL)
  
        if not self.updateThread.isRunning():
            # If the thread has not been started let's kick it off  
            self.updateThread.start()  
  
if __name__ == '__main__':  
    print("YOU HAVE 1 SECOND!") 
    time.sleep(1) 
    app = QGuiApplication(sys.argv)  
    win = MainApplication()  
    win.show()  
    app.processEvents()
    sys.exit(app.exec_())
