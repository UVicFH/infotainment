from PyQt5.QtCore import QUrl, QObject, QVariant, QRunnable, QCoreApplication, QThreadPool
from PyQt5.QtGui import QGuiApplication 
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

    def __init__(self,parent=None):
        super(MainApplication, self).__init__(parent)
        #self.resize(1200, 900) # TODO update to get screen size for full
        
        self.setSource(QUrl.fromLocalFile(os.path.join(os.path.dirname(__file__),'qml/Display_rev_1.qml')))
        self.setupUpdateThread()  
        self.qml = self.rootObject()
        

    def updateESS_SOC(self, pESS_SOC):
        #Pass in the SOC percent, this will do the rest
        for i in range(0,20):
            if(pESS_SOC>(i*5)):
                self.qml.setProperty("soc_"+str((i+1)*5), QVariant(1))
            else:
                self.qml.setProperty("soc_"+str((i+1)*5), QVariant(0))

    def updateFUEL(self, pFUEL):
        #Pass in the fuel percent, this will do the rest
        for i in range(0,20):
            if(pFUEL>(i*5)):
                self.qml.setProperty("fuel_"+str((i+1)*5), QVariant(1))
            else:
                self.qml.setProperty("fuel_"+str((i+1)*5), QVariant(0))

    def updateGLV_SOC(self, pGLV_SOC): 
        if(pGLV_SOC==self.GOOD): #GOOD
            self.qml.setProperty("glv_soc_green", QVariant(1))
            self.qml.setProperty("glv_soc_red", QVariant(0))
        if(pGLV_SOC==self.BAD): #BAD
            self.qml.setProperty("glv_soc_green", QVariant(0))
            self.qml.setProperty("glv_soc_red", QVariant(1)) 

    def updateMOTOR_TEMP(self, pMOTOR_TEMP): 
        if(pMOTOR_TEMP==self.GOOD): #GOOD
            self.qml.setProperty("motor_temp_green", QVariant(1))
            self.qml.setProperty("motor_temp_red", QVariant(0))
            self.qml.setProperty("motor_temp_yellow", QVariant(0))
        if(pMOTOR_TEMP==self.BAD): #BAD
            self.qml.setProperty("motor_temp_green", QVariant(0))
            self.qml.setProperty("motor_temp_red", QVariant(1)) 
            self.qml.setProperty("motor_temp_yellow", QVariant(0))        
        if(pMOTOR_TEMP==self.WARN): #WARN
            self.qml.setProperty("motor_temp_green", QVariant(0))
            self.qml.setProperty("motor_temp_red", QVariant(0)) 
            self.qml.setProperty("motor_temp_yellow", QVariant(1)) 

    def updateBRB(self, pBRB): 
        if(pBRB==self.GOOD): #GOOD
            self.qml.setProperty("brb_green", QVariant(1))
            self.qml.setProperty("brb_red", QVariant(0))
        if(pBRB==self.BAD): #BAD
            self.qml.setProperty("brb_green", QVariant(0))
            self.qml.setProperty("brb_red", QVariant(1)) 

    def updateESS_TEMP(self, pESS_TEMP): 
        if(pESS_TEMP==self.GOOD): #GOOD
            self.qml.setProperty("ess_temp_green", QVariant(1))
            self.qml.setProperty("ess_temp_red", QVariant(0))
        if(pESS_TEMP==self.BAD): #BAD
            self.qml.setProperty("ess_temp_green", QVariant(0))
            self.qml.setProperty("ess_temp_red", QVariant(1))

    def updateTRAN(self, pTRAN):
        if(pTRAN==self.GOOD): #GOOD
            self.qml.setProperty("tran_green", QVariant(1))
            self.qml.setProperty("tran_red", QVariant(0))
        if(pTRAN==self.BAD): #BAD
            self.qml.setProperty("tran_green", QVariant(0))
            self.qml.setProperty("tran_red", QVariant(1)) 

    def updateEngineTorque(self, engineTorque):  
        self.qml.setProperty("engineTorque", QVariant(str(engineTorque)))

    def updateSpeed(self, pSPEED):  
        self.qml.setProperty("speed", QVariant(str(pSPEED)))

    def updateGear(self, pGEAR):  
        self.qml.setProperty("gear", QVariant(str(pGEAR)))

    def updateThrottle(self, pTHROTTLE):  
        self.qml.setProperty("throttle", QVariant(str(pTHROTTLE)))

    def mousePressEvent(self, QMouseEvent):
        # Used for finding mouse postions, strictly testing
        print(QMouseEvent.pos()) 

    def updateTachNeedle(self, tachRPM):
        # TODO angle is 270 degrees around tach, use mousePressEvent to get position then work around, i know its dusty but its ok
        # TODO update to allow input to be RPM vs Degrees
        goToAngle = (tachRPM*0.0226)+1.3077
        self.qml.setProperty("tachNeedleAngle", QVariant(int(goToAngle)))
   
    def setupUpdateThread(self):  
        self.updateThread = UpdateThread()  
        # Connect our update function to the progress signal of the update thread  
        self.updateThread.engineTorque.connect(self.updateEngineTorque)
        self.updateThread.throttlePercent.connect(self.updateThrottle)
        self.updateThread.speed.connect(self.updateSpeed)
        self.updateThread.gear.connect(self.updateGear)

        self.updateThread.brb.connect(self.updateBRB)
        self.updateThread.glv_soc.connect(self.updateGLV_SOC)
        self.updateThread.motor_temp.connect(self.updateMOTOR_TEMP)
        self.updateThread.ess_temp.connect(self.updateESS_TEMP)
        self.updateThread.tran.connect(self.updateTRAN)
        
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
