import commands
import RPi.GPIO as GPIO
import time

commands.getoutput("sudo hciconfig hci0 up")
commands.getoutput("sudo hciconfig hci0 noscan")

rec = 0

print "ble ready!"

def callback_alert(pin):
    global rec
    commands.getoutput("sudo hciconfig hci0 leadv 3")
    commands.getoutput("sudo hcitool -i hci0 cmd 0x08 0x0008 1E 02 01 1A 1A FF 4C 00 02 15 0A CE 38 33 32 13 AA E2 98 F1 34 6D A3 F3 89 72 00 01 00 01 C8 00")
    rec = 1
    print "advertising"

def callback_off(pin):
    
    commands.getoutput("sudo hciconfig hci0 noleadv")
#    commands.getoutput("sudo hciconfig hci0 down")
    print "device down"

if __name__=="__main__":
    global rec
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP) # 4th pin used
    GPIO.add_event_detect(4, GPIO.RISING) # detect high->low
    GPIO.add_event_callback(4, callback_alert) #callback
    
    try:
        # onWait
        while True:

            if GPIO.input(4) == 0 and rec == 1:
                
                commands.getoutput("sudo hcitool -i hci0 cmd 0x08 0x0008 1E 02 01 1A 1A FF 4C 00 02 15 0A CE 38 33 32 13 AA E2 98 F1 34 6D A3 F3 89 72 00 01 00 02 C8 00")
                print "close"
                time.sleep(25)
                callback_off(4)
                rec = 0

            time.sleep(1)
            print rec

    except KeyboardInterrupt:
        print "\nBreak"
        callback_off(4)
        GPIO.cleanup()
