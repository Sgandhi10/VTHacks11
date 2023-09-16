import socket
import fcntl
import struct

import pyupm_i2clcd as lcd

def get_ip_address(ifname):

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(), 
        0x8915, # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
        

myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

myLcd.clear()

myLcd.setColor(255, 255 ,0)

myLcd.setCursor(0, 0)

ip_address = get_ip_address('wlan0')
myLcd.write(ip_address)

