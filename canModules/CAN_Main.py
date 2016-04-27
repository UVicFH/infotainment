import can
from canModules import CAN_Opener
import serial
import struct

"""
Combines both CAN_MAIN and CAN_HANDLER

"""

"""
For message filtering
Filtering has been removed temporarily

ID we care about
0x100
0x200
0x300

Mask
0x700
"""

CAN_MASK = 0xFFF

CAN_MESSAGE_1 = 0x100
CAN_MESSAGE_2 = 0x200
CAN_MESSAGE_3 = 0x300
CAN_MESSAGE_4 = 0x400

ENTRY_1 = {'can_id':CAN_MESSAGE_1, 'can_mask':CAN_MASK}
ENTRY_2 = {'can_id':CAN_MESSAGE_2, 'can_mask':CAN_MASK}
ENTRY_3 = {'can_id':CAN_MESSAGE_3, 'can_mask':CAN_MASK}
ENTRY_4 = {'can_id':CAN_MESSAGE_4, 'can_mask':CAN_MASK}

FILTER_DICTIONARY_LIST = [ENTRY_1,ENTRY_2,ENTRY_3,ENTRY_4]


can.rc['interface'] = 'socketcan_native'
from can.interfaces.interface import Bus
can_interface = "can0"

ONE_BIT_MASK        = 0x1
TWO_BIT_MASK        = 0X3
THREE_BIT_MASK      = 0x7
FOUR_BIT_MASK       = 0xF

FIVE_BIT_MASK       = 0x1F
SIX_BIT_MASK        = 0x3F
SEVEN_BIT_MASK      = 0x7F
EIGHT_BIT_MASK      = 0xFF

NINE_BIT_MASK       = 0x1FF
TEN_BIT_MASK        = 0x3FF
ELEVEN_BIT_MASK     = 0x7FF
TWELVE_BIT_MASK     = 0xFFF

THRIRTEEN_BIT_MASK  = 0x1FFF
FOURTEEN_BIT_MASK   = 0x3FFF
FIFTEEN_BIT_MASK    = 0x7FFF
SIXTEEN_BIT_MASK    = 0xFFFF

class CAN_Main(object):
	"""	
	There should be:
	Signals | Messages
	--------+---------
	?       | ?

	Each has a Previous & Current
	Each has a update boolean
	Each has a set_value Function
	All are init to 0/False unless otherwise specified

	PROTOTYPE:
		def __init__
			self.current_PARAM = 0 
			self.previous_PARAM = 0
			self.update_PARAM = False

		def set_PARAM(pValue):
			self.previous_PARAM = self.current_PARAM
			self.current_PARAM = pValue
			if(self.previous_PARAM != self.current_PARAM):
			self.update_PARAM = True

	ADD READ FROM CAN STUFF
		pollBus() in FHguiTest
		can message read
	"""
	#current_vehicle_speed = -1
	#previous_vehicle_speed = -2
	#update_vehicle_speed = False
	
	try:
		serialport = serial.Serial("/dev/ttyUSB0", 115200, timeout=0.5)
	except:
		print("No Serial Port detected")
		
	def __init__(self):
		
	
		#super(CAN_Main, self).__init__()
		#self.can_handler = CAN_Handler.CAN_Handler()
		#self.bus = Bus(can_interface,(FILTER_DICTIONARY_LIST))

		#Engine Signals
		self.current_engine_coolant_temp = 0 
		self.previous_engine_coolant_temp = 0
		self.update_engine_coolant_temp = False

		self.current_engine_RPM = 0
		self.previous_engine_RPM = 0
		self.update_engine_RPM = False

		self.current_shift = 0
		self.previous_shift = 0
		self.update_shift = False

		#Warnings
		self.current_warning_ess_overtemp = 0
		self.previous_warning_ess_overtemp = 0
		self.update_warning_ess_overtemp = False

		self.current_warning_glv_soc_low = 0
		self.previous_warning_glv_soc_low = 0
		self.update_warning_glv_soc_low = False

		self.current_warning_motor_over_temp = 0
		self.previous_warning_motor_over_temp = 0
		self.update_warning_motor_over_temp = False

		self.current_warning_charging = 0
		self.previous_warning_charging = 0
		self.update_warning_charging = False

		self.current_warning_fuel_low = 0
		self.previous_warning_fuel_low = 0
		self.update_warning_fuel_low = False

		self.current_warning_CAN_down = 0
		self.previous_warning_CAN_down = 0
		self.update_warning_CAN_down = False

		self.current_warning_motor_on = 0
		self.previous_warning_motor_on = 0
		self.update_warning_motor_on = False
	
		#Electrical Systems
		self.current_ess_soc = 0
		self.previous_ess_soc = 0
		self.update_ess_soc = False

		self.current_fuel = 0
		self.previous_fuel = 0
		self.update_fuel = False

		self.current_target_fuel = 0
		self.previous_target_fuel = 0
		self.update_target_fuel = False

		self.current_current_gear = 0
		self.previous_current_gear = 0
		self.update_current_gear = False
				
		self.current_vehicle_speed = 0
		self.previous_vehicle_speed = 0
		self.update_vehicle_speed = False

	def telemetry(self, pFrame):
			dataString=""
			for i in range(len(pFrame.data)):
				dataString+=","+str(pFrame.data[i])
			canString=(str(pFrame.arbitration_id)+":"+dataString.strip(","))
			try:	
		        	self.serialport.write(canString.encode())
		        	self.serialport.write('\n'.encode()) 	
			except:
				pass

	def pollBus(self):
		try:	
			msg = self.bus.recv(timeout=10)
			self.telemetry(msg)
			self.process_CAN_message(msg)
		except :
			print("TODO m: We need to catch this, yo")
			raise

	def process_CAN_message(self, pCan_frame):
		self.message_select(pCan_frame)

	#engine coolant temp
	def set_engine_coolant_temp(self, pValue): #TODO MAKE THIS CONTROL WARNING LIGHT
		self.previous_engine_coolant_temp = self.current_engine_coolant_temp
		self.current_engine_coolant_temp = pValue
		if(self.previous_engine_coolant_temp != self.current_engine_coolant_temp):
			self.update_engine_coolant_temp = True
	#engine RPM
	def set_engine_RPM(self, pValue):
		self.previous_engine_RPM = self.current_engine_RPM
		self.current_engine_RPM = pValue
		if(self.previous_engine_RPM != self.current_engine_RPM):
			self.update_engine_RPM = True
	#Shift
	def set_shift(self, pValue):
		self.previous_shift = self.current_shift
		self.current_shift = pValue
		if(self.previous_shift != self.current_shift):
			self.update_shift = True
	
	#Warning Charing
	def set_warning_charging(self, pValue):
		self.previous_warning_charging = self.current_warning_charging
		self.current_warning_charging = pValue
		if(self.previous_warning_charging != self.current_warning_charging):
			self.update_warning_charging = True
	#Warning Fuel Low
	def set_warning_fuel_low(self, pValue):
		self.previous_warning_fuel_low = self.current_warning_fuel_low
		self.current_warning_fuel_low = pValue
		if(self.previous_warning_fuel_low != self.current_warning_fuel_low):
			self.update_warning_fuel_low = True
	#Warning CAN down
	def set_warning_CAN_down(self, pValue):
		self.previous_warning_CAN_down = self.current_warning_CAN_down
		self.current_warning_CAN_down = pValue
		if(self.previous_warning_CAN_down != self.current_warning_CAN_down):
			self.update_warning_CAN_down = True
	#Warning Motor On
	def set_warning_motor_on(self, pValue):
		self.previous_warning_motor_on = self.current_warning_motor_on
		self.current_warning_motor_on = pValue
		if(self.previous_warning_motor_on != self.current_warning_motor_on):
			self.update_warning_motor_on = True
	#warning ess over temp
	def set_warning_ess_overtemp(self, pValue):
		self.previous_warning_ess_overtemp = self.current_warning_ess_overtemp
		self.current_warning_ess_overtemp = pValue
		if(self.previous_warning_ess_overtemp != self.current_warning_ess_overtemp):
			self.update_warning_ess_overtemp = True
	#warning glv soc low
	def set_warning_glv_soc(self, pValue):
		self.previous_warning_glv_soc_low = self.current_warning_glv_soc_low
		self.current_warning_glv_soc_low = pValue
		if(self.previous_warning_glv_soc_low != self.current_warning_glv_soc_low):
			self.update_warning_glv_soc_low = True
	#warning motor over temp
	def set_warning_motor_over_temp(self, pValue):
		self.previous_warning_motor_over_temp = self.current_warning_motor_over_temp
		self.current_warning_motor_over_temp = pValue
		if(self.previous_warning_motor_over_temp != self.current_warning_motor_over_temp):
			self.update_warning_motor_over_temp = True

	#current ess soc
	def set_ess_soc(self, pValue):
		self.previous_ess_soc = self.current_ess_soc
		self.current_ess_soc = pValue
		if(self.previous_ess_soc != self.current_ess_soc):
			self.update_ess_soc = True
	#current fuel level
	def set_fuel(self, pValue):
		self.previous_fuel = self.current_fuel
		self.current_fuel = pValue
		if(self.previous_fuel != self.current_fuel):
			self.update_fuel = True
	#current target fuel
	def set_target_fuel(self, pValue):
		self.previous_target_fuel = self.current_target_fuel
		self.current_target_fuel = pValue
		if(self.previous_target_fuel != self.current_target_fuel):
			self.update_target_fuel = True
	
	#current gear  set_target_fuel
	def set_current_gear(self, pValue):
		self.previous_current_gear = self.current_current_gear
		self.current_current_gear = pValue
		if(self.previous_current_gear != self.current_current_gear):
			self.update_current_gear = True
	#vehicle speed
	def set_vehicle_speed(self, pValue):
		self.previous_vehicle_speed = self.current_vehicle_speed
		self.current_vehicle_speed = pValue
		if(self.previous_vehicle_speed != self.current_vehicle_speed):
			self.update_vehicle_speed = True


	def initializeInstances(self):
		#FILTER REMOVED TEMPORARILY FOR TELEMETRY TESTING
		#self.bus = Bus(can_interface,can_filters=FILTER_DICTIONARY_LIST)
		self.bus = Bus(can_interface)
		self.can_tools = CAN_Opener.Can_Opener()

	def message_select(self, pCAN_frame):
		if(pCAN_frame.arbitration_id == 0x101): #Fast
			self.message_vechicle_fast(pCAN_frame.data)
		if(pCAN_frame.arbitration_id == 0x102): #Slow
			self.message_vechicle_slow(pCAN_frame.data)			
		if(pCAN_frame.arbitration_id == 0x200): #Warnings
			self.message_vechicle_warnings(pCAN_frame.data)
		else:
			pass

	def shiftData(self, pValue, pShiftPlaces): #simple divide
		return pValue>>pShiftPlaces

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
	def message_vechicle_fast(self, data):
		self.set_engine_RPM(data[3]*256 + data[2]) #2 bytes
		self.set_vehicle_speed(self.shiftData(data[4], 1)) #div by 2
		self.set_ess_soc(self.shiftData(data[5], 1)) #div by 2
		self.set_current_gear(data[6] & FOUR_BIT_MASK) #Lowest 4 bits
		self.set_shift(self.shiftData(data[6],4) & ONE_BIT_MASK)

	def message_vechicle_slow(self, data):
		self.set_target_fuel(self.shiftData(data[0], 1)) #div by 2
		self.set_fuel(self.shiftData(data[4], 1)) #div by 2
		self.set_engine_coolant_temp(data[6]) #no div by 2?

	def message_vechicle_warnings(self, data):
		self.set_warning_motor_over_temp(data[0] & ONE_BIT_MASK)
		self.set_warning_fuel_low(self.shiftData(data[0], 1) & ONE_BIT_MASK)
		self.set_warning_ess_overtemp(self.shiftData(data[0], 2) & ONE_BIT_MASK)
		self.set_warning_CAN_down(self.shiftData(data[0], 4) & ONE_BIT_MASK)
		self.set_warning_charging(self.shiftData(data[0], 5) & ONE_BIT_MASK)
		self.set_warning_motor_on(self.shiftData(data[0], 6) & ONE_BIT_MASK)
		self.set_warning_glv_soc(self.shiftData(data[0], 7) & ONE_BIT_MASK)










