import PCF85


class PCF:

    def __init__(self, address):
        self.address = address
        PCF85.setup(address, 1)

    def pin_mode(self, PinName, Mode):
        return PCF85.pin_mode(PinName, Mode)

    def digital_read(self, PinName):
        return PCF85.digitalRead(PinName)

    def digital_write(self, PinName, Val):
        return PCF85.digitalWrite(PinName, Val)

