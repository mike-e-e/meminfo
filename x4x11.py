
import subprocess
import os
import com.android.monkeyrunner
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
device=MonkeyRunner.waitForConnection()


#034browser
device.startActivity("com.android.browser/com.android.browser.BrowserActivity")
MonkeyRunner.sleep(3)
device.touch(530,134,"DOWN_AND_UP")
MonkeyRunner.sleep(4)
device.type("http://10.237.2.150/memtest/sina.htm")
MonkeyRunner.sleep(2)
device.touch(1000,134,"DOWN_AND_UP")
MonkeyRunner.sleep(5)
device.touch(690,1836,"DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1836,"DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(530,134,"DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.type("http://10.237.2.150/memtest/wangyi.htm")
MonkeyRunner.sleep(2)
device.touch(1000,134,"DOWN_AND_UP")
MonkeyRunner.sleep(5)
device.touch(690,1836,"DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1836,"DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(530,134,"DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.type("http://10.237.2.150/memtest/sohu.htm")
MonkeyRunner.sleep(2)
device.touch(1000,134,"DOWN_AND_UP")
MonkeyRunner.sleep(5)
device.touch(690,1836,"DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1836,"DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(530,134,"DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.type("http://10.237.2.150/memtest/fenghuang.htm")
MonkeyRunner.sleep(2)
device.touch(1000,134,"DOWN_AND_UP")
MonkeyRunner.sleep(5)
device.touch(690,1836,"DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1836,"DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(530,134,"DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.type("http://10.237.2.150/memtest/aitaobao.htm")
MonkeyRunner.sleep(2)
device.touch(1000,134,"DOWN_AND_UP")
MonkeyRunner.sleep(10)
cmd="adb shell dumpsys meminfo com.android.browser" 
fd=open("d:/memory/34browser.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(100)
cmd="adb shell dumpsys meminfo com.android.browser" 
fd1=open("d:/memory/34browser.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
MonkeyRunner.sleep(2)
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)



#02contacts
device.touch(413,1750,"DOWN_AND_UP")
MonkeyRunner.sleep(2)
device.drag((540,1500),(540,600),0.5,10)
MonkeyRunner.sleep(1)
device.drag((540,1500),(540,600),0.5,10)
MonkeyRunner.sleep(1)
device.touch(540,960,"DOWN_AND_UP")
MonkeyRunner.sleep(1)
device.touch(540,960,"DOWN_AND_UP")
MonkeyRunner.sleep(1)
device.touch(623,1821,"DOWN_AND_UP")
MonkeyRunner.sleep(2)
cmd="adb shell dumpsys meminfo android.process.acore" 
fd=open("d:/memory/02contacts.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo android.process.acore" 
fd1=open("d:/memory/02contacts.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
MonkeyRunner.sleep(2)
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#03incallui
device.touch(159,1750,"DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(180,1126,"DOWN_AND_UP")
MonkeyRunner.sleep(1)
device.touch(540,1636,"DOWN_AND_UP")
MonkeyRunner.sleep(1)
device.touch(540,1636,"DOWN_AND_UP")
MonkeyRunner.sleep(1)
device.touch(180,1126,"DOWN_AND_UP")
MonkeyRunner.sleep(1)
device.touch(540,1636,"DOWN_AND_UP")
MonkeyRunner.sleep(1)
device.touch(540,1820,"DOWN_AND_UP")
MonkeyRunner.sleep(10)
cmd="adb shell dumpsys meminfo com.android.incallui" 
fd=open("d:/memory/03incallui.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(10)
cmd="adb shell dumpsys meminfo com.android.incallui" 
fd1=open("d:/memory/03incallui.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.touch(540,30,"DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1755,"DOWN_AND_UP")
MonkeyRunner.sleep(2)
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#04yellowpage
device.shell('monkey -p com.miui.yellowpage --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.miui.yellowpage" 
fd=open("d:/memory/04yellowpage.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.miui.yellowpage" 
fd1=open("d:/memory/04yellowpage.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#05mms
device.shell('monkey -p com.android.mms --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.android.mms" 
fd=open("d:/memory/05mms.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.android.mms" 
fd1=open("d:/memory/05mms.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#06gallery
device.shell('monkey -p com.miui.gallery --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.miui.gallery" 
fd=open("d:/memory/06gallery.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.miui.gallery" 
fd1=open("d:/memory/06gallery.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)



#09camera
device.shell('monkey -p com.android.camera --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.android.camera" 
fd=open("d:/memory/09camera.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.android.camera" 
fd1=open("d:/memory/09camera.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#10weather2
device.shell('monkey -p com.miui.weather2 --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.miui.weather2" 
fd=open("d:/memory/10weather.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.miui.weather2" 
fd1=open("d:/memory/10weather.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#11thememanager
device.shell('monkey -p com.android.thememanager --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.android.thememanager" 
fd=open("d:/memory/11thememanager.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.android.thememanager" 
fd1=open("d:/memory/11thememanager.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#12securitycenter
device.startActivity(component="com.miui.securitycenter/com.miui.securitycenter.MainActivity")
MonkeyRunner.sleep(2)
device.touch(180,1370,"DOWN_AND_UP")
MonkeyRunner.sleep(2)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(2)
device.touch(540,1370,"DOWN_AND_UP")
MonkeyRunner.sleep(2)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(2)
device.touch(900,1370,"DOWN_AND_UP")
MonkeyRunner.sleep(2)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(2)
device.touch(180,1701,"DOWN_AND_UP")
MonkeyRunner.sleep(2)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(2)
device.touch(540,1701,"DOWN_AND_UP")
MonkeyRunner.sleep(2)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(2)
device.touch(900,1701,"DOWN_AND_UP")
MonkeyRunner.sleep(2)
device.press('KEYCODE_BACK','DOWN_AND_UP')
MonkeyRunner.sleep(2)
cmd="adb shell dumpsys meminfo com.miui.securitycenter" 
fd=open("d:/memory/12securitycenter.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
cmd="adb shell dumpsys meminfo com.miui.cleanmaster" 
fd=open("d:/memory/12cleanmaster.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
cmd="adb shell dumpsys meminfo com.miui.networkassistant" 
fd=open("d:/memory/12networkassistant.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
cmd="adb shell dumpsys meminfo com.miui.antispam" 
fd=open("d:/memory/12antispam.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(30)
cmd="adb shell dumpsys meminfo com.miui.securitycenter" 
fd1=open("d:/memory/12securitycenter.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
cmd="adb shell dumpsys meminfo com.miui.cleanmaster" 
fd1=open("d:/memory/12cleanmaster.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
cmd="adb shell dumpsys meminfo com.miui.networkassistant" 
fd1=open("d:/memory/12networkassistant.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
cmd="adb shell dumpsys meminfo com.miui.antispam" 
fd1=open("d:/memory/12antispam.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
MonkeyRunner.sleep(2)
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#13market
device.shell('monkey -p com.xiaomi.market --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.xiaomi.market" 
fd=open("d:/memory/13market.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.xiaomi.market" 
fd1=open("d:/memory/13market.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#14account
device.shell('monkey -p com.xiaomi.account --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.xiaomi.account" 
fd=open("d:/memory/14account.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.xiaomi.account" 
fd1=open("d:/memory/14account.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#15email
device.shell('monkey -p com.android.email --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.android.email" 
fd=open("d:/memory/15email.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.android.email" 
fd1=open("d:/memory/15email.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#16updater
device.startActivity(component="com.android.updater/com.android.updater.MainActivity")
MonkeyRunner.sleep(5)
cmd="adb shell dumpsys meminfo com.android.updater" 
fd=open("d:/memory/16updater.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(30)
cmd="adb shell dumpsys meminfo com.android.updater" 
fd1=open("d:/memory/16updater.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)



#18fmradio
device.shell('monkey -p com.miui.fmradio --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.miui.fmradio" 
fd=open("d:/memory/18fmradio.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.miui.fmradio" 
fd1=open("d:/memory/18fmradio.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#19calculator2
device.shell('monkey -p com.android.calculator2 --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.android.calculator2" 
fd=open("d:/memory/19calculator2.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.android.calculator2" 
fd1=open("d:/memory/19calculator2.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#20fileexplorer
device.shell('monkey -p com.android.fileexplorer --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.android.fileexplorer" 
fd=open("d:/memory/20fileexplorer.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.android.fileexplorer" 
fd1=open("d:/memory/20fileexplorer.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#21compass
device.shell('monkey -p com.miui.compass --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.miui.compass" 
fd=open("d:/memory/21compass.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.miui.compass" 
fd1=open("d:/memory/21compass.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#22barcodescanner
device.shell('monkey -p com.miui.barcodescanner --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.miui.barcodescanner" 
fd=open("d:/memory/22barcodescanner.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.miui.barcodescanner" 
fd1=open("d:/memory/22barcodescanner.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#23bugreport
device.shell('monkey -p com.miui.bugreport --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.miui.bugreport" 
fd=open("d:/memory/23bugreport.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.miui.bugreport" 
fd1=open("d:/memory/23bugreport.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#24voiceassist
device.shell('monkey -p com.miui.voiceassist --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.miui.voiceassist" 
fd=open("d:/memory/24voiceassist.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.miui.voiceassist" 
fd1=open("d:/memory/24voiceassist.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#25downloads
device.shell('monkey -p com.android.providers.downloads.ui --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo android.process.mediaUI" 
fd=open("d:/memory/25downloads.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo android.process.mediaUI" 
fd1=open("d:/memory/25downloads.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#26wallet
device.shell('monkey -p com.mipay.wallet --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.mipay.wallet" 
fd=open("d:/memory/26wallet.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.mipay.wallet" 
fd1=open("d:/memory/26wallet.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#27calendar
device.shell('monkey -p com.android.calendar --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.android.calendar" 
fd=open("d:/memory/27calendar.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.android.calendar" 
fd1=open("d:/memory/27calendar.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#28notes
device.shell('monkey -p com.miui.notes --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.miui.notes" 
fd=open("d:/memory/28notes.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.miui.notes" 
fd1=open("d:/memory/28notes.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#29smarthome
device.shell('monkey -p com.xiaomi.smarthome --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.xiaomi.smarthome" 
fd=open("d:/memory/29smarthome.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.xiaomi.smarthome" 
fd1=open("d:/memory/29smarthome.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#30gamecenter
device.shell('monkey -p com.xiaomi.gamecenter --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.xiaomi.gamecenter" 
fd=open("d:/memory/30gamecenter.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.xiaomi.gamecenter" 
fd1=open("d:/memory/30gamecenter.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#31video
device.shell('monkey -p com.miui.video --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.miui.video" 
fd=open("d:/memory/31video.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.miui.video" 
fd1=open("d:/memory/31video.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#32xiaomishenghuo
device.shell('monkey -p com.xiaomi.o2o --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.xiaomi.o2o" 
fd=open("d:/memory/32xiaomishenghuo.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.xiaomi.o2o" 
fd1=open("d:/memory/32xiaomishenghuo.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#33jinrong
device.shell('monkey -p com.xiaomi.jr --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.xiaomi.jr" 
fd=open("d:/memory/33jinrong.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.xiaomi.jr" 
fd1=open("d:/memory/33jinrong.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#35payment
device.shell('monkey -p com.xiaomi.payment --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.xiaomi.payment" 
fd=open("d:/memory/35payment.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.xiaomi.payment" 
fd1=open("d:/memory/35payment.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#36vip
device.shell('monkey -p com.xiaomi.vip --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.xiaomi.vip" 
fd=open("d:/memory/36vip.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.xiaomi.vip" 
fd1=open("d:/memory/36vip.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#04yellowpage
device.shell('monkey -p com.miui.yellowpage --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.miui.yellowpage" 
fd=open("d:/memory/04yellowpage.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.miui.yellowpage" 
fd1=open("d:/memory/04yellowpage.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#01settings
device.shell('monkey -p com.android.settings --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.android.settings" 
fd=open("d:/memory/01settings.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.android.settings" 
fd1=open("d:/memory/01settings.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#08player
device.shell('monkey -p com.miui.player --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.miui.player" 
fd=open("d:/memory/08player.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.miui.player" 
fd1=open("d:/memory/08player.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#17soundrecorder
device.shell('monkey -p com.android.soundrecorder --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.android.soundrecorder" 
fd=open("d:/memory/17soundrecorder.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.android.soundrecorder" 
fd1=open("d:/memory/17soundrecorder.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)


#07deskclock
device.shell('monkey -p com.android.deskclock --throttle 200 -v 1000')
MonkeyRunner.sleep(3)
cmd="adb shell dumpsys meminfo com.android.deskclock" 
fd=open("d:/memory/07deskclock.txt","w")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd.write(data.stdout.read())
fd.close()
device.press("KEYCODE_HOME","DOWN_AND_UP")
MonkeyRunner.sleep(60)
cmd="adb shell dumpsys meminfo com.android.deskclock" 
fd1=open("d:/memory/07deskclock.txt","a")
data=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
fd1.write(data.stdout.read())
fd1.close()
device.press("KEYCODE_MENU","DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(540,1707,"DOWN_AND_UP")
MonkeyRunner.sleep(3)

