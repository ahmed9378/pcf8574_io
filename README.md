### **Python driver for PCF8574 8bit IO Expander board**
Developed for the Raspberry Pi, requires the python-smbus2 package to access the I2C bus.

tested on raspberry pi 3b plus with two PCF8574 boards.


First install smbus2 using:
`pip3 install smbus2` 

then install the actual package using:
`pip3 install pcf8574-io`


Usage Example:
```python
import pcf8574_io

# you can use up to 8 PCF8574 boards 0x20 and 0x21 are the I2C addresses
# true will set all the pins HIGH +5v false will set them to LOW 0v 
p1 = pcf8574_io
p2 = pcf8574_io

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
```

Note: the board has only 25mA output current so if you want to control some relay modules,
that need more than 25mA use more than one pin to control each relay.

The board been used:
![alt text](https://image.made-in-china.com/2f0j00CbvRKwBGGecA/Pcf8574-Io-Expansion-Board-I-O-Expander-I2c-Bus-Evaluation-Development-Module.jpg)

#**Link**
https://pypi.org/project/pcf8574-io/



