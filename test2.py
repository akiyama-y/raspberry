import RPi.GPIO as GPIO
import time
from bluetooth import *
import commands
import sys

#BT
uuid= "2f09892e-b8e7-4acf-a323-1ad687d48c52" 

server_socket = BluetoothSocket( RFCOMM )
server_socket.bind(("", 0))
server_socket.listen(1)

print "listening"

advertise_service( server_socket, "Window sensor",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS],
                   profiles = [ SERIAL_PORT_PROFILE ],
                   )

print "waiting for connection"

client_socket, client_info = server_socket.accept()

print "accepted"

data = client_socket.recv(1024)
print "[%s]" % data

while True:
    time.sleep(1)
    server_socket.send("alert")
    server_socket.close()
    client_socket.close()

def callback(pin):
    client_socket, client_info = server_socket.accept()

    print "Accepted"

    time.sleep(0.5) #preactive for chattering
    print("recieved")
    server_socket.send("ALERT!window1") # todo
    server_socket.close()
    client_socket.close()

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
