
import serial
import serial.tools.list_ports
import time

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

song1 = ['1','1','1','5','5','6','6','5','5','4','4','3','3','2','2','1','1']
song2 = ['1','2','3','1','1','2','3','1','3','4','5','3','4','5']

for p in ports:
    print (p[1])
    if "Arduino" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

ser=serial.Serial(port='COM7')
def run():
    action = "empty"
    while action != "q":
        print ('select which song do you want to play ? 1,2 q and others for quit')
        action = input("> ")
        if action == "1":
            for notes in song1:
                ser.write(notes.encode())
                print ("send:"+notes)
                time.sleep(1.206)
        elif action == "2":
            for notes in song2:
                ser.write(notes.encode())
                print ("send:"+notes)
                time.sleep(1.206)

        else :
            return

run()
