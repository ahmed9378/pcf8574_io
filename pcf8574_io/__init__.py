from pcf8574_io import PCF85


class PCF:

    def __init__(self, address, status):
        self.address = address
        self.status = status
        PCF85.setup(address, 1, status)

    def pin_mode(self, PinName, Mode):
        return PCF85.pin_mode(PinName, Mode)

    def digital_read(self, PinName):
        return PCF85.digitalRead(PinName)

    def digital_write(self, PinName, Val):
        return PCF85.digitalWrite(PinName, Val)

