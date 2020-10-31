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

    def digital_read(self, PinName):
        return PCF85.digitalRead(PinName, self.smBusNum, self.address)

    def digital_write(self, PinName, Val):
        PCF85.digitalWrite(PinName, Val, self.address, self.pinModeFlag, self.smBusNum)
