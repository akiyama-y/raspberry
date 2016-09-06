import RPi.GPIO as GPIO
import time

def callback(pin):
    time.sleep(0.5) #preactive for chattering
    print("recieved")

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM) # GPIO mode
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 17th pi is used
    GPIO.add_event_detect(17, GPIO.RISING) # detect low->high
    GPIO.add_event_callback(17, callback) # callback
    try:
        # onWait
        while True:
            time.sleep(1) 
    except KeyboardInterrupt:
        print "\nBreak"
        GPIO.cleanup()
