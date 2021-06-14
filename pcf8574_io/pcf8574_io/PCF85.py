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
    return set_mode(pinNameToNum(pinName), mode, flg, int(math.pow(2, pinNameToNum(pinName))))


def set_mode(pnNum, mode, rValue, flg):
    if "INPUT" in mode.strip() and isKthBitSet(flg, pnNum + 1):
        flg = flg - rValue
        return flg
    elif "OUTPUT" in mode.strip() and not isKthBitSet(flg, pnNum + 1):
        flg = flg + rValue
        return flg
    else:
        return flg


def digitalRead(pinName, smbs, addr):
    with SMBus(smbs) as bus:
        b = bus.read_byte(addr)
    # if isKthBitSet(b, pinNameToNum(pinName) + 1):
        return b
    # else:
        # return False


def pinNameToNum(pinName):
    pn = int(pinName.strip().replace("p", "").strip())
    if pn in range(8):
        return pn
    else:
        print("pin name error!")


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
        print("You can not Write Input Pin")


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
