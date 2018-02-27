import serial
import serial.tools.list_ports
import time

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

song1 = ['1','1','5','5','6','6','5','5','4','4','3','3','2','2','1','1']
song2 = ['1','2','3','1','1','2','3','1','3','4','5','3','4','5']

#f = open('mysongs.csv', 'r')
#data = f.read()
#rows = data.split('\n')
#print(rows[0:5])
#row=rows[0]
#song1 = row.split(',')

for p in ports:
    print (p[1])
    if "Arduino" in p[1]:
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

#ser=serial.Serial(port='COM4')
#ser=serial.Serial(port='/dev/ttymodem542')

def run():
    action = "empty"
    while action != "q":
        print ('select which song do you want to play ? 1,2 q and others for quit')
        action = input("> ")
        if action == "1":
            for notes in song1:
                ser.write(notes.encode())
                print ("send:"+notes)
                time.sleep(1)
        elif action == "2":
            ser.write('2'.encode())

        else :
            return

run()
