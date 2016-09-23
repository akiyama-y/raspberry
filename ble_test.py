import commands
import RPi.GPIO as GPIO
import time

commands.getoutput("sudo hciconfig hci0 up")
commands.getoutput("sudo hciconfig hci0 noscan")
commands.getoutput("sudo hciconfig hci0 leadv 3")

rec = "inactive"

print "ble ready!"

commands.getoutput("sudo hcitool -i hci0 cmd 0x08 0x0008 1E 02 01 1A 1A FF 4C 00 02 15 0A CE 38 33 32 13 AA E2 98 F1 34 6D A3 F3 89 72 00 00 00 00 C8 00")
rec = "active"
print "advertising"
