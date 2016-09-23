import RPi.GPIO as GPIO
import time
from bluetooth import *
import commands
import sys

#BT
uuid= "2f09892e-b8e7-4acf-a323-1ad687d48c52" 

server_socket = BluetoothSocket( RFCOMM )
server_socket.bind(("", PORT_ANY))
server_socket.listen(1)

print "listening"

advertise_service( server_socket, "Window sensor",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS],
                   profiles = [ SERIAL_PORT_PROFILE ],
                   )
while True:
    print "waiting for connection"
    
    client_socket, client_info = server_socket.accept()
    
    print "accepted"

    try:

        data = client_socket.recv(1024)
        print "[%s]" % data

        time.sleep(1)
        server_socket.send("alert")
    
    except IOError:
        pass
    except KeyboardInterrupt:

        print "disconnected"

        server_socket.close()
        client_socket.close()
        
        print "done"

        break

