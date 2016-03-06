from tkinter import *
from tkinter import ttk
from subprocess import call

#CAN imports
import can
can.rc['interface'] = 'socketcan_native'
from can.interfaces.interface import Bus
can_interface = "can0"

import struct
#All the mask we will need most likely, easy to add more, should be globals
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


class DistanceGui(object):
	root = Tk()
	bus = Bus(can_interface) #Not stoked on this area.. want it to work
	
	def __init__(self):
		self.currentDistance = StringVar()
		self.currentDistance.set(0)

		self.currentDistancemm = StringVar()
		self.currentDistancemm.set(0)

		self.frame_rate = 100
		self.initializeMainWindow()
		self.makeMainFrame()
		self.makeCanvas()
	
	def pack_data(can_byte_array):
        	buf=bytes()
        	buf=buf.join((struct.pack('B', val) for val in can_byte_array))
        	packed_can_data = int.from_bytes(buf, byteorder='big')
        	return packed_can_data
    
    	def shift_mask(start_loc, length, lumped_data, filter):
        	shift = 64 - start_loc - length
        	lumped_data = lumped_data>>shift
        	lumped_data = lumped_data & filter
        	return lumped_data

	def initializeMainWindow(self):
		self.root.title("FH CAN TEST")
		self.root.attributes("-fullscreen", True)
		self.root.bind()
		self.state = False
	
	def makeMainFrame(self):
		self.mainframe = ttk.Frame(self.root, padding="0 0 0 0")
		self.mainframe.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=(N, E, W, S))
		self.mainframe.columnconfigure(0, weight=1)
		self.mainframe.rowconfigure(0, weight=1) 

	def makeCanvas(self):
		self.distanceLabel = ttk.Label(self.mainframe, textvariable=self.currentDistance, width=3, font="Helvetica 36 bold")
		self.distanceLabel.grid(column=0, row=1, sticky=(E))
		
		self.distanceTextLabel = ttk.Label(self.mainframe, text="DISTANCE (cm)", font="Helvetica 10 bold")
		self.distanceTextLabel.grid(column=1, row=1, sticky=(W))

		self.distanceLabelmm = ttk.Label(self.mainframe, textvariable=self.currentDistancemm, width=3, font="Helvetica 36 bold")
		self.distanceLabelmm.grid(column=0, row=2, sticky=(E))
		
		self.distanceTextLabelmm = ttk.Label(self.mainframe, text="DISTANCE (mm)", font="Helvetica 10 bold")
		self.distanceTextLabelmm.grid(column=1, row=2 , sticky=(W))

	def increaseNum(self):
		try:
			msg = self.bus.recv()
			bits = pack_data(msg.data)
			if(msg.id==0x00):
				#Distance is cm
				cm = shift_mask(8,8,bits,EIGHT_BIT_FILTER)
				self.currentDistance.set(cm)
			if(msg.id==0x01):
				#Distance is mm
				mm = shift_mask(0,8,bits,EIGHT_BIT_FILTER)
				self.currentDistancemm.set(mm)
			else:
				pass

			#self.currentDistance.set(msg.data[1])

		except ValueError:
			pass
		self.root.after(self.frame_rate, self.increaseNum)

	def run(self):
		#this is where the magic is going to happen
		self.increaseNum()	
		self.root.mainloop()

if __name__ == "__main__":
	distGui = DistanceGui()
	distGui.run()	
