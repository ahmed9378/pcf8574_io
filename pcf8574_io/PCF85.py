from smbus2 import SMBus
import math


def setup(PCFAdd, smBus, status):
    if status:
        with SMBus(smBus) as bus:
            bus.write_byte(PCFAdd, 0xFF)
    elif not status:
        with SMBus(smBus) as bus:
            bus.write_byte(PCFAdd, 0x00)


def pin_mode(pinName, mode, flg):
    pn = pinNameToNum(pinName)
    return set_mode(pinName, mode, int(math.pow(2, pn)), flg)
    


def set_mode(pinName, mode, rValue, flg):
    pn = pinNameToNum(pinName)
    if "INPUT" in mode.strip() and isKthBitSet(flg, pn + 1):
        flg = flg - rValue
        return flg
    elif "OUTPUT" in mode.strip() and not isKthBitSet(flg, pn + 1):
        flg = flg + rValue
        return flg
    else:
        return flg


def digitalRead(pinName, smbs, addr):
    with SMBus(smbs) as bus:
        b = bus.read_byte(addr)
    if isKthBitSet(b, pinNameToNum(pinName) + 1):
        return True
    else:
        return False


def pinNameToNum(pinName):
    try:
        pn = int(pinName.strip().replace("p", "").strip())
        if pn in range(8):
            return pn
        else:
            print("Wrone pin name!")
    except:
        raise Exception("Wrone pin name!")


def isKthBitSet(n, k):
    if n & (1 << (k - 1)):
        return True
    else:
        return False


def digitalWrite(pinName, val, addr, flg, smbs):
    if isKthBitSet(flg, pinNameToNum(pinName) + 1):
        if "HIGH" in val.strip():
            write_data(pinNameToNum(pinName), 1, smbs, flg, addr)
        elif "LOW" in val.strip():
            write_data(pinNameToNum(pinName), 0, smbs, flg, addr)
        else:
            print("Wrong pin mode for pin",pinName)
    else:
        print("You can't write input pin")


def write_data(pnNum, val, smbs, flg, addr):
    if isKthBitSet(flg, pnNum + 1):
        with SMBus(smbs) as bus:
            wr = bus.read_byte(addr)
        if val == 0 and isKthBitSet(wr, pnNum + 1):
            wr = wr - int(math.pow(2, pnNum))
            with SMBus(smbs) as bus:
                bus.write_byte(addr, wr)
        elif val == 1 and not isKthBitSet(wr, pnNum + 1):
            wr = wr + int(math.pow(2, pnNum))
            with SMBus(smbs) as bus:
                bus.write_byte(addr, wr)

def get_pin_mode(pinName,flg):
    pn = pinNameToNum(pinName)
    if isKthBitSet(flg,pn+1):
        return "OUTPUT"
    else:
        return "INPUT"

def is_pin_output(pinName,flg):
    pn = pinNameToNum(pinName)
    return isKthBitSet(flg,pn+1)

def get_all_mode(flg):
    mlist = []
    for i in range(0,8):
        if isKthBitSet(flg,i+1):
            mlist.append("OUTPUT")
        else:
            mlist.append("INPUT")
    return mlist