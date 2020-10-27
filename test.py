import pcf8574_io

# you can use up to 8 PCF8574 boards
p1 = pcf8574_io.PCF(0x20)
p2 = pcf8574_io.PCF(0x21)

# p0 to p7 are the pins name
# INPUT or OUTPUT is the mode
p1.pin_mode("p0", "INPUT")
print(p1.digital_read("p0"))

# you can write and read the output pins
# use HIGH or LOW to set the pin HIGH is +5v LOW is 0v
p1.pin_mode("p4", "OUTPUT")
p1.digital_write("p4", "HIGH")
print(p1.digital_read("p4"))

# you can read and write up to 8 boards at the same time just make sure you ech board has a different address
p2.pin_mode("p7", "OUTPUT")
p2.digital_write("p7", "LOW")
print(p2.digital_read("p7"))


