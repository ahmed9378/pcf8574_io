from smbus2 import SMBus

pinModeFlag = 0x00
PCFAddress = 0x20
smBusNum = 1
writeData = 0x00


def setup(PCFAdd, smBus):
    global pinModeFlag, writeData, PCFAddress, smBusNum
    pinModeFlag = 0x00
    PCFAddress = PCFAdd
    smBusNum = smBus
    writeData = 0x00
    with SMBus(smBusNum) as bus:
        b = bus.write_byte(PCFAddress, 0x00)


# mode INPUT 0,OUTPUT 1
def pin_mode(pinName, mode):
    global pinModeFlag
    if "p0" in pinName.strip():
        set_mode(pinName, mode, 0, 0x01)
    elif "p1" in pinName.strip():
        set_mode(pinName, mode, 1, 0x02)
    elif "p2" in pinName.strip():
        set_mode(pinName, mode, 2, 0x04)
    elif "p3" in pinName.strip():
        set_mode(pinName, mode, 3, 0x08)
    elif "p4" in pinName.strip():
        set_mode(pinName, mode, 4, 0x10)
    elif "p5" in pinName.strip():
        set_mode(pinName, mode, 5, 0x20)
    elif "p6" in pinName.strip():
        set_mode(pinName, mode, 6, 0x40)
    elif "p7" in pinName.strip():
        set_mode(pinName, mode, 7, 0x80)
    else:
        print("Wrong Pin Name!")


def isKthBitSet(n, k):
    if n & (1 << (k - 1)):
        return True
    else:
        return False


def read_data(pinNum):
    with SMBus(smBusNum) as bus:
        b = bus.read_byte(PCFAddress)
    if isKthBitSet(b, pinNum):
        return True
    else:
        return False


def write_data(pinName, val):
    if "p0" in pinName.strip():
        set_write(pinName, 0, 0x01, val)
    if "p1" in pinName.strip():
        set_write(pinName, 1, 0x02, val)
    if "p2" in pinName.strip():
        set_write(pinName, 2, 0x04, val)
    if "p3" in pinName.strip():
        set_write(pinName, 3, 0x08, val)
    if "p4" in pinName.strip():
        set_write(pinName, 4, 0x10, val)
    if "p5" in pinName.strip():
        set_write(pinName, 5, 0x20, val)
    if "p6" in pinName.strip():
        set_write(pinName, 6, 0x40, val)
    if "p7" in pinName.strip():
        set_write(pinName, 7, 0x80, val)


def set_mode(pinName, mode, pValue, rValue):
    global pinModeFlag
    cValue = pValue + 1
    if "p" + str(pValue) in pinName.strip():
        if "INPUT" in mode.strip() and isKthBitSet(pinModeFlag, cValue):
            pinModeFlag = pinModeFlag - rValue
        elif "OUTPUT" in mode.strip() and not isKthBitSet(pinModeFlag, cValue):
            pinModeFlag = pinModeFlag + rValue
        else:
            print("Wrong IO Mode")


def set_write(pinName, pValue, rValue, val):
    global writeData
    with SMBus(smBusNum) as bus:
        b = bus.read_byte(PCFAddress)
    writeData = b
    cValue = pValue + 1
    if "p" + str(pValue) in pinName.strip():
        if val == 0 and isKthBitSet(writeData, cValue):
            writeData = writeData - rValue
            with SMBus(smBusNum) as bus:
                bus.write_byte(PCFAddress, writeData)

        elif val == 1 and not isKthBitSet(writeData, cValue):
            writeData = writeData + rValue
            with SMBus(smBusNum) as bus:
                bus.write_byte(PCFAddress, writeData)


def checkPinNum(pinName):
    if 0 < int(pinName.strip().replace("p")) < 8:
        return True
    else:
        return False


def digitalRead(pinName):
    global pinModeFlag
    cValue = int(pinName.strip().replace("p", "")) + 1
    return read_data(cValue)


def digitalWrite(pinName, val):
    global pinModeFlag
    cValue = int(pinName.strip().replace("p", "")) + 1
    if isKthBitSet(pinModeFlag, cValue):
        if "HIGH" in val.strip():
            write_data(pinName, 1)
        elif "LOW" in val.strip():
            write_data(pinName, 0)
    else:
        print("You can not Write Input Pin")

# pin_mode("p0", "INPUT")
# digitalRead("p0")
# digitalWrite("p0", "HIGH")

# print("{0:b}".format(pinModeFlag))
