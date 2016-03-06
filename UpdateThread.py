from PyQt5.QtCore import QThread, pyqtSignal
from random import randint
# TODO uncomment import once on pi
from canModules import CAN_Main, CAN_Opener

#inherit from Qthread and setup our own thread class  
class UpdateThread(QThread):
    #WARNINGS - Feed INT: 0=BAD 1=GOOD 2=WARN
    brb = pyqtSignal(int)
    glv_soc = pyqtSignal(int)
    motor_temp = pyqtSignal(int)
    ess_temp = pyqtSignal(int)
    tran = pyqtSignal(int)
    
    #TEXT - Feed String
    gear = pyqtSignal(str)
    throttlePercent = pyqtSignal(str)
    engineTorque = pyqtSignal(str)
    speed = pyqtSignal(str)
    
    #DIAL - Feed INT RPM
    tachNeedle = pyqtSignal(int)

    #BAR GRAPHS - Feed INT: 0-100 percent
    ess_soc = pyqtSignal(int)
    fuel = pyqtSignal(int)

    def __init__(self,parent=None):  
        super(UpdateThread,self).__init__(parent)  
        self.exiting = False  
        
        self.canMain = CAN_Main.CAN_Main()
        self.canMain.initializeInstances()
    
    def __del__(self):
        self.wait()

    def demo(self):
        #Demos all features
        self.msleep(2000)
            
        self.glv_soc.emit(0)
        self.motor_temp.emit(0)
        self.brb.emit(0)
        self.ess_temp.emit(0)
        self.tran.emit(0)

        self.engineTorque.emit(str(0))
        self.throttlePercent.emit(str(0))
        self.fuel.emit(0)
        self.ess_soc.emit(0)
        
        self.msleep(1000)
        
        self.glv_soc.emit(1)
        self.motor_temp.emit(1)
        self.brb.emit(1)
        self.ess_temp.emit(1)
        self.tran.emit(1)
        
        for x in range(0,101):
            self.fuel.emit(x)
            self.ess_soc.emit(x)
            
            self.speed.emit(str(x))
            self.tachNeedle.emit(x*120)
            self.engineTorque.emit(str(x))
            self.throttlePercent.emit(str(x))
            self.gear.emit((x-(x%20))/20)
            self.msleep(30)

        self.motor_temp.emit(2)

    def stop(self):
        print("threadClass Stop")
        self.exiting = True
        self.terminate()

    def run(self):
        temp = 0
        #self.displayStartup()
        while not self.exiting:
            # Code below is CAN code to be integrated after testing
            self.pollBus()
            self.checkForUpdates()

            # All code below is testing/demo code  
            #self.demo()
        return 

    def pollBus(self):
        self.canMain.pollBus()

    def checkForUpdates(self):
        #TEXT
        if self.canMain.update_current_gear:
            self.gear.emit(str(self.canMain.current_current_gear))
            self.canMain.update_current_gear = False

        if self.canMain.update_vehicle_speed:
            self.speed.emit(str(self.canMain.current_vehicle_speed))
            self.canMain.update_vehicle_speed = False

        if self.canMain.update_throttle_percent:
            self.throttlePercent.emit(str(self.canMain.current_throttle_percent))
            self.canMain.update_throttle_percent = False

        if self.canMain.update_engine_torque:
            tmp_engine_torque = self.canMain.current_engine_torque/10
            self.engineTorque.emit(str(int(tmp_engine_torque)))
            self.canMain.update_engine_torque = False

        #DIAL
        if self.canMain.update_engine_RPM:
            self.tachNeedle.emit(int(self.canMain.current_engine_RPM))
            self.canMain.update_engine_RPM = False

        #WARNINGS
        if self.canMain.update_warning_glv_cockpit_brb:
            self.glv_soc.emit(int(self.canMain.current_warning_glv_soc_low))

        if self.canMain.update_engine_coolant_temp:
            tmp_engine_temp = self.canMain.current_engine_coolant_temp
            #Find out what units temp is in...
            if tmp_engine_temp<180:
                self.motor_temp.emit(2)
            elif ((tmp_engine_temp>=180) and (tmp_engine_temp<210)):
                self.motor_temp.emit(0)
            elif tmp_engine_temp>210:
                self.motor_temp.emit(1)

        if self.canMain.update_warning_glv_cockpit_brb:
            self.brb.emit(self.canMain.current_warning_glv_cockpit_brb)
            self.canMain.update_engine_coolant_temp = False

        if self.canMain.update_warning_ess_overtemp:
            self.ess_temp.emit(self.canMain.current_warning_ess_overtemp)
            self.canMain.update_warning_ess_overtemp = False

        if self.canMain.update_warning_transmission_failure:
            self.tran.emit(self.canMain.current_warning_transmission_failure)
            self.canMain.update_warning_transmission_failure = False

        #BARS
        if self.canMain.update_ess_soc:
            self.ess_soc.emit(self.canMain.current_ess_soc)
            self.canMain.update_ess_soc = False

        if self.canMain.update_fuel:
            self.fuel.emit(self.canMain.current_fuel)
            self.canMain.update_fuel = False

