from PyQt5.QtCore import QThread, pyqtSignal
from random import randint
# TODO uncomment import once on pi
from canModules import CAN_Main, CAN_Opener

#inherit from Qthread and setup our own thread class  
class UpdateThread(QThread):
    #WARNINGS - Feed INT: 0=BAD 1=GOOD 2=WARN
    glv_soc = pyqtSignal(int)
    motor_temp = pyqtSignal(int)
    ess_temp = pyqtSignal(int)
    charging = pyqtSignal(int)
    fuel_low = pyqtSignal(int)
    CAN_down = pyqtSignal(int)
    motor_on = pyqtSignal(int)

    #TEXT - Feed String
    gear = pyqtSignal(str)
    speed = pyqtSignal(str)
    temp_text = pyqtSignal(int)

    #DIAL - Feed INT RPM
    tachNeedle = pyqtSignal(int)

    #BAR GRAPHS - Feed INT: 0-100 percent
    ess_soc = pyqtSignal(int)
    fuel = pyqtSignal(int)

    shift = pyqtSignal(int)

    def __init__(self,parent=None):  
        super(UpdateThread,self).__init__(parent)  
        self.exiting = False  
        
        self.canMain = CAN_Main.CAN_Main()
        self.canMain.initializeInstances()
    
    def __del__(self):
        self.wait()

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
            #self.demo2()
        return 

    def pollBus(self):
        self.canMain.pollBus()

    def f_to_c(self, pTemperature_F):
        return ((1.8*pTemperature_F)+32)

    def checkForUpdates(self):
        #TEXT
        if self.canMain.update_current_gear:
            self.gear.emit(str(self.canMain.current_current_gear))
            self.canMain.update_current_gear = False

        if self.canMain.update_vehicle_speed:
            self.speed.emit(str(self.canMain.current_vehicle_speed))
            self.canMain.update_vehicle_speed = False

        if self.canMain.update_engine_coolant_temp:
            tmp_engine_temp = self.canMain.current_engine_coolant_temp
            #Find out what units temp is in...
            self.UpdateThread.updateMOTOR_TEMP_HACK(tmp_engine_temp)
            if((158<=tmp_engine_temp<176) or (203<tmp_engine_temp<=221)):
                self.temp_text.emit(2)
            elif (176 <= tmp_engine_temp <= 203):
                self.temp_text.emit(0)
            elif(tmp_engine_temp<158 or tmp_engine_temp>221):
                self.temp_text.emit(1)

        #Shift
        if self.canMain.update_shift:
            self.shift.emit(self.canMain.current_shift)
            self.canMain.update_shift = False

        #DIAL
        if self.canMain.update_engine_RPM:
            self.tachNeedle.emit(int(self.canMain.current_engine_RPM))
            self.canMain.update_engine_RPM = False

        #WARNINGS       
        if self.canMain.update_warning_ess_overtemp:
            self.ess_temp.emit(self.canMain.current_warning_ess_overtemp)
            self.canMain.update_warning_ess_overtemp = False

        if self.canMain.update_warning_motor_over_temp:
            self.motor_temp.emit(self.canMain.current_warning_motor_over_temp)
            self.canMain.update_warning_motor_over_temp = False

        if self.canMain.update_warning_glv_soc_low:
            self.glv_soc.emit(self.canMain.current_warning_glv_soc_low)
            self.canMain.update_warning_glv_soc_low = False

        if self.canMain.update_warning_charging:
            self.charging.emit(self.canMain.current_warning_charging)
            self.canMain.update_warning_charging = False

        if self.canMain.update_warning_fuel_low:
            self.fuel_low.emit(self.canMain.current_warning_fuel_low)
            self.canMain.update_warning_fuel_low = False

        if self.canMain.update_warning_CAN_down:
            self.CAN_down.emit(self.canMain.current_warning_CAN_down)
            self.canMain.update_warning_CAN_down = False

        if self.canMain.update_warning_motor_on:
            self.motor_on.emit(self.canMain.current_warning_motor_on)
            self.canMain.update_warning_motor_on = False

        #BARS
        if self.canMain.update_ess_soc:
            self.ess_soc.emit(self.canMain.current_ess_soc)
            self.canMain.update_ess_soc = False

        if self.canMain.update_fuel or self.canMain.update_target_fuel:
            self.fuel.emit(self.canMain.current_fuel)
            self.canMain.update_fuel = False

