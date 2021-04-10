#
#
# Ce module contient une fonction global SensorRed()

class Sensors:

    def __init__(self, func_count):
    	self.func_count = func_count 
    	self.FUNC_ID 	= 0
    	self.rsp		= "Null"

    def ReadSensor_1(self):
    	self.rsp = "Sensor 1"

    def ReadSensor_2(self):
    	self.rsp = "Sensor 2"

    def ReadSensor_3(self):
    	self.rsp = "Sensor 3"

    def ReadSensor_4(self):
    	self.rsp = "Sensor 4"

    def ReadSensor_5(self):
    	self.rsp = "Sensor 5"

    def Read(self):
    	if (self.FUNC_ID == 0):
    		self.ReadSensor_1()
    	else:
    		if (self.FUNC_ID == 1):
    			self.ReadSensor_2()
    		else:
    			if (self.FUNC_ID == 2):
    				self.ReadSensor_3()
    			else:
    				self.rsp = "Null"

    	self.FUNC_ID += 1
    	if (self.FUNC_ID >= self.func_count):
    		self.FUNC_ID = 0

    	return self.rsp