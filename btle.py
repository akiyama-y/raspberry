from bluepy.bluepy.btle import UUID, Peripheral




p = Peripheral("28:84:fa:97:0f:f8")
svc = p.getServiceByUUID(uuid="2B1DA6DE-9C29-4D6C-A930-B990EA2F12BB")

ch =svc.getCharacteristics(uuid="7F855F82-9378-4508-A3D2-CD989104AF22")[0]
ch.write()

while 1:
    if p.waitForNotifications(1.0):
        continue

    print "waiting"
