from pcf8574_io import PCF85


class PCF:

    def __init__(self, address):
        self.address = address
        self.status = True
        self.pinModeFlag = 0x00
        self.smBusNum = 1
        PCF85.setup(address, self.smBusNum, self.status)

    def pin_mode(self, PinName, Mode):
        self.pinModeFlag = PCF85.pin_mode(PinName, Mode, self.pinModeFlag)

    def read(self, PinName):
        return PCF85.digitalRead(PinName, self.smBusNum, self.address)

    def write(self, PinName, Val):
        PCF85.digitalWrite(PinName, Val, self.address, self.pinModeFlag, self.smBusNum)

    def set_i2cBus(self, port):
        self.smBusNum = port
    
    def get_i2cBus(self):
        return self.smBusNum
    
    def get_pin_mode(self, PinName):
        return PCF85.get_pin_mode(PinName,self.pinModeFlag)
        
    def is_pin_output(self, PinName):
        return PCF85.is_pin_output(PinName,self.pinModeFlag)
    
    def get_all_mode(self):
        return PCF85.get_all_mode(self.pinModeFlag)