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

CAN_LAYOUT = 0 #get rid of this when CAN migration is finalized

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
		
		self.current_engine_torque = 0
		self.previous_engine_torque = 0
		self.update_engine_torque = False
		
		self.current_engine_RPM = 0
		self.previous_engine_RPM = 0
		self.update_engine_RPM = False
		
		self.current_throttle_percent = 0
		self.previous_throttle_percent = 0
		self.update_throttle_percent = False

		#Warnings
		self.current_warning_ess_overtemp = 0
		self.previous_warning_ess_overtemp = 0
		self.update_warning_ess_overtemp = False

		#self.current_warning_fuel_level_low = 0
		#self.previous_warning_fuel_level_low = 0
		#self.update_warning_fuel_level_low = False

		self.current_warning_glv_cockpit_brb = 0
		self.previous_warning_glv_cockpit_brb = 0
		self.update_warning_glv_cockpit_brb = False

		self.current_warning_glv_soc_low = 0
		self.previous_warning_glv_soc_low = 0
		self.update_warning_glv_soc_low = False

		self.current_warning_motor_over_temp = 0
		self.previous_warning_motor_over_temp = 0
		self.update_warning_motor_over_temp = False

		self.current_warning_transmission_failure = 0 
		self.previous_warning_transmission_failure = 0
		self.update_warning_transmission_failure = False
	
		#Electrical Systems
		self.current_ess_soc = 0
		self.previous_ess_soc = 0
		self.update_ess_soc = False

		self.current_fuel = 0
		self.previous_fuel = 0
		self.update_fuel = False

		#self.current_ess_voltage = 0
		#self.previous_ess_voltage = 0
		#self.update_ess_voltage = False

		#Control 
		#self.current_odometer = 0
		#self.previous_odometer= 0
		#self.update_odometer = False

		#self.current_current_control_mode = 0 #not confusing at all
		#self.previous_current_control_mode = 0
		#self.update_current_control_mode = False

		self.current_current_gear = 0
		self.previous_current_gear = 0
		self.update_current_gear = False
		
		
		self.current_vehicle_speed = 0
		self.previous_vehicle_speed = 0
		self.update_vehicle_speed = False

		#self.current_engery_budget_status = 0
		#self.previous_engery_budget_status = 0
		#self.update_engery_budget_status = False
	
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

	#engine torque
	def set_engine_torque(self, pValue):
		self.previous_engine_torque = self.current_engine_torque
		self.current_engine_torque = pValue
		if(self.previous_engine_torque != self.current_engine_torque):
			self.update_engine_torque = True

	#engine RPM
	def set_engine_RPM(self, pValue):
		self.previous_engine_RPM = self.current_engine_RPM
		self.current_engine_RPM = pValue
		if(self.previous_engine_RPM != self.current_engine_RPM):
			self.update_engine_RPM = True

	#throttle percent
	def set_throttle_percent(self, pValue):
		self.previous_throttle_percent = self.current_throttle_percent
		self.current_throttle_percent = pValue
		if(self.previous_throttle_percent != self.current_throttle_percent):
			self.update_throttle_percent = True
	
	#warning ess over temp
	def set_warning_ess_overtemp(self, pValue):
		self.previous_warning_ess_overtemp = self.current_warning_ess_overtemp
		self.current_warning_ess_overtemp = pValue
		if(self.previous_warning_ess_overtemp != self.current_warning_ess_overtemp):
			self.update_warning_ess_overtemp = True

	#warning fuel level low - Replaced with bar graph
	#def set_warning_fuel_level_low(self, pValue):
	#	self.previous_warning_fuel_level_low = self.current_warning_fuel_level_low
	#	self.current_warning_fuel_level_low = pValue
	#	if(self.previous_warning_fuel_level_low != self.current_warning_fuel_level_low):
	#		self.update_warning_fuel_level_low = True

	#warning glv cockpit brb
	def set_warning_glv_cockpit_brb(self, pValue):
		self.previous_warning_glv_cockpit_brb = self.current_warning_glv_cockpit_brb
		self.current_warning_glv_cockpit_brb = pValue
		if(self.previous_warning_glv_cockpit_brb != self.current_warning_glv_cockpit_brb):
			self.update_warning_glv_cockpit_brb = True

	#warning glv soc low
	def set_warning_glv_soc_low(self, pValue):
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

	#warning transmission failure
	def set_warning_transmission_failure(self, pValue):
		self.previous_warning_transmission_failure = self.current_warning_transmission_failure
		self.current_warning_transmission_failure = pValue
		if(self.previous_warning_transmission_failure != self.current_warning_transmission_failure):
			self.update_warning_transmission_failure = True

	#current ess soc
	def set_ess_soc(self, pValue):
		self.previous_ess_soc = self.current_ess_soc
		self.current_ess_soc = pValue
		if(self.previous_ess_soc != self.current_ess_soc):
			self.update_ess_soc = True

	#current ess voltage - Not used anymore
	#def set_ess_voltage(self, pValue):
	#	self.previous_ess_voltage = self.current_ess_voltage
	#	self.current_ess_voltage = pValue
	#	if(self.previous_ess_voltage != self.current_ess_voltage):
	#		self.update_ess_voltage = True

	#current odometer
	#def set_odometer(self, pValue):
	#	self.previous_odometer = self.current_odometer
	#	self.current_odometer = pValue
	#	if(self.previous_odometer != self.current_odometer):
	#		self.update_odometer = True

	#current fuel level
	def set_fuel(self, pValue):
		self.previous_fuel = self.current_fuel
		self.current_fuel = pValue
		if(self.previous_fuel != self.current_fuel):
			self.update_fuel = True

	#current control mode - Not used anymore
	#def set_current_control_mode(self, pValue):
	#	self.previous_current_control_mode = self.current_current_control_mode
	#	self.current_current_control_mode = pValue
	#	if(self.previous_current_control_mode != self.current_current_control_mode):
	#		self.update_current_control_mode = True

	#current gear
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

	#energy budget status - Not used
	#def set_engery_budget_status(self, pValue):
	#	self.previous_engery_budget_status = self.current_engery_budget_status
	#	self.current_engery_budget_status = pValue
	#	if(self.previous_engery_budget_status != self.current_engery_budget_status):
	#		self.update_engery_budget_status = True

	def initializeInstances(self):
		#FILTER REMOVED TEMPORARILY FOR TELEMETRY TESTING
		#self.bus = Bus(can_interface,can_filters=FILTER_DICTIONARY_LIST)
		self.bus = Bus(can_interface)
		self.can_tools = CAN_Opener.Can_Opener()

	def message_select(self, pCAN_frame):
		if(CAN_LAYOUT==0):
			if(pCAN_frame.arbitration_id == 0x100):
				self.message_one(pCAN_frame.data)
			elif(pCAN_frame.arbitration_id == 0x200):
				self.message_two(pCAN_frame.data)
			elif(pCAN_frame.arbitration_id == 0x300):
				self.message_three(pCAN_frame.data)
			elif(pCAN_frame.arbitration_id == 0x400):
				self.message_four(pCAN_frame.data)
			else:
				pass
		elif(CAN_LAYOUT==1):
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

	def message_one(self, data): #Engine Signals
		self.set_engine_coolant_temp(data[0])
		self.set_engine_torque(data[1])
		self.set_engine_RPM(data[3]*256 + data[2])
		self.set_throttle_percent(self.shiftData(data[4], 1))
		self.set_fuel(data[5]) #May have to update later

	def message_two(self, data): #Warnings
		self.set_warning_glv_soc_low(self.shiftData(data[0], 3) & ONE_BIT_MASK)
		self.set_warning_glv_cockpit_brb(self.shiftData(data[0], 2) & ONE_BIT_MASK)
		self.set_warning_ess_overtemp(data[0] & ONE_BIT_MASK)
		self.set_warning_transmission_failure(self.shiftData(data[0], 5) & ONE_BIT_MASK)

	def message_three(self, data): #Electrical Systems
		self.set_ess_soc(self.shiftData(data[5], 1))
	
	def message_four(self, data): #Control
		self.set_current_gear(self.shiftData(data[0], 2) & FOUR_BIT_MASK)
		self.set_vehicle_speed(self.shiftData(data[1], 1))


	'''
	Need:

	ess soc (ESS_Voltage?)
	engine torque
	'''
	def message_vechicle_fast(self, data):
		#Engine_Throttle_Percent
		#Motor_Throttle_Percent
		self.set_engine_RPM(data[3]*256 + data[2]) #2 bytes
		self.set_vehicle_speed(self.shiftData(data[4], 1)) #div by 2
		#ESS_Voltage SOC?
		self.set_current_gear(data[6] & FOUR_BIT_MASK) #Lowest 4 bits

	def message_vechicle_slow(self, data):
		#Vehicle dist
		self.set_throttle_percent(self.shiftData(data[2], 1)) #div by 2
		#Driver_Brake_Percent
		self.set_fuel(self.shiftData(data[4], 1)) #div by 2
		self.set_warning_glv_cockpit_brb(data[5] & ONE_BIT_MASK)
		#GLV TSMS
		#Current_Control_Mode
		self.set_engine_coolant_temp(data[6]) #no div by 2?

	def message_vechicle_warnings(self, data):
		#Fuel_Low
		self.set_warning_ess_overtemp(self.shiftData(data[0], 4) & ONE_BIT_MASK)
		self.set_warning_transmission_failure(self.shiftData(data[0], 5) & ONE_BIT_MASK)

