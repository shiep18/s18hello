import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
x1=41
z1=42
x2=48
z2=48
rent = 0
while True:
    time.sleep(1)
    pos=mc.player.getTilePos()
    if pos.x>x1 and pos.x<x2 and pos.z>z1 and pos.z<z2:
        rent = rent +1
        mc.postToChat("YOU owe rent:"+str(rent))
        
        
        
        
        
