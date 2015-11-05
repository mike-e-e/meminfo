import subprocess
import os
import time
from random import randint
import com.android.monkeyrunner
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
device=MonkeyRunner.waitForConnection()

device.shell('monkey -p com.miui.home --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.miui.home" 
fd=open("d:/memory/homesystemui.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
b=1
while(b<6):
    device.shell('monkey -p com.miui.home --throttle 200 -v 1000')
    MonkeyRunner.sleep(3)
    cmd="adb shell dumpsys meminfo com.miui.home" 
    fd=open("d:/memory/homesystemui.txt","a")
    data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
    fd.write(data.stdout.read())
    fd.close()
    b+=1

device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(720,2287,"DOWN_AND_UP")
MonkeyRunner.sleep(3)    
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(1)



a=1
while(a<7):
    i=1
    while(i<10):
        for i in range(1, 10):
            device.drag((100,10),(100,1400),0.5,1)
            MonkeyRunner.sleep(2)
            device.drag((600,1500),(300,1500),0.1,10)
            MonkeyRunner.sleep(2)
            device.touch(randint(0,1000),randint(0,1600),'DOWN_AND_UP')
            device.drag((100,10),(100,1400),0.5,1)
            MonkeyRunner.sleep(1)
        for i in range(1, 10):
            device.drag((100,10),(100,1400),0.5,1)
            MonkeyRunner.sleep(2)
            device.drag((300,1500),(600,1500),0.1,10)
            MonkeyRunner.sleep(2)
            device.touch(randint(0,1000),randint(0,1600),'DOWN_AND_UP')
            device.drag((100,10),(100,1400),0.5,1)
            MonkeyRunner.sleep(1)
        for i in range(1, 10):
            device.drag((100,10),(100,1400),0.5,1)
            MonkeyRunner.sleep(2)
            device.drag((600,1500),(300,1500),0.1,10)
            MonkeyRunner.sleep(2)
            longx = randint(0,1000)
            longy = randint(0,1600)
            device.drag((longx,longy),(longx,longy),1,10)
            device.drag((100,10),(100,1400),0.5,1)
            MonkeyRunner.sleep(1)
        i+=1
    cmd="adb shell dumpsys meminfo com.android.systemui" 
    fd1=open("d:/memory/homesystemui.txt","a")
    data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
    fd1.write(data.stdout.read())
    fd1.close()
    a+=1

device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(2)

