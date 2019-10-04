import re,os
from Utilities import command
from uiautomator import Device
from time import sleep

class uiAutomator:
    def __init__(self):
        self.device = None

    def getDeviceInstance(self):
        deviceId = self.getDeviceID()
        if deviceId is not None:
            self.device = Device(deviceId)

    def getDeviceID(self):
        deviceId = None
        cmd = "devices"
        output = command.executeCommandOnDevice(cmd)
        if output is not None:
            for line in output.splitlines():
                reObj = re.search(r'(\w+).*device\b', line)
                if reObj:
                    deviceId = reObj.group(1).strip()
        return deviceId

    def rootAndRemount(self):
        self.root()
        sleep(2)
        self.remount()

    def root(self):
        cmd = "root"
        command.executeCommandOnDevice(cmd)

    def remount(self):
        cmd = "remount"
        command.executeCommandOnDevice(cmd)

    def writeToFile(self,filePath, fileContent, mode='w'):
        try:
            with open(filePath,mode) as f:
                f.write(fileContent)

        except Exception as e:
            print("Error: unable to write content to a file")
            print(e.__str__())

    def collectLogcat(self,filePath):
        cmd = "logcat"
        logcatContent = command.executeCommandOnDevice(cmd)
        if logcatContent is not None:
            self.writeToFile(filePath,logcatContent,'w')
        else:
            print("logcat is not collected properly")

    def collectDmesgLogs(self,filePath):
        cmd = "shell dmesg"
        fileContent = command.executeCommandOnDevice(cmd)
        if fileContent is not None:
            self.writeToFile(filePath,fileContent)
        else:
            print("dmesg log is not collected properly")

    def pushFiles(self,source,destination):
        cmd = "push {} {}".format(source,destination)
        command.executeCommandOnDevice(cmd)

    def pullFiles(self,source,destination):
        if self.doesResourceExists(source):
            cmd = "pull {} {}".format(source,destination)
            command.executeCommandOnDevice(cmd)
        else:
            print("Resource doesn't exists on the device, Hence pulling failed")

    def reboot(self):
        cmd = "reboot"
        command.executeCommandOnDevice(cmd)

    def installApp(self,apkPath):
        cmd = "install -r -g {}".format(apkPath)
        command.executeCommandOnDevice(cmd)

    def unInstallApp(self, packageName):
        cmd = "uninstall {}".format(packageName)
        command.executeCommandOnDevice(cmd)

    def installAPKs(self,apksPath):
        for apkFile in os.listdir(apksPath):
            if apkFile.endswith('.apk'):
                apkFilePath = os.path.join(apksPath,apkFile)
                self.installApp(apkFilePath)

    def doesResourceExists(self, filePath):
        cmd = "ls {}".format(filePath)
        output = command.executeCommandOnDevice(cmd)
        if 'No such file or directory' in output:
            return False
        return True

    def deleteResourceFromDevice(self,resourcePath):
        cmd = "shell rm -rf {}".format(resourcePath)
        command.executeCommandOnDevice(cmd)

    def captureScreenshot(self,imageFileName):
        imageFilePath = "/scard/{}".format(imageFileName)
        cmd = "shell screencap -p {}".format(imageFilePath)
        command.executeCommandOnDevice(cmd)

    def openAppMenu(self):
        self.device.press.home()
        self.swipeUp()

    def getCoOrdinates(self, xPercentage, yPercentage):
        x = (self.device.info['displayWidth']*xPercentage)/100
        y = (self.device.info['displayHeight']*yPercentage)/100
        return x,y

    def swipeUp(self):
        x1, y1 = self.getCoOrdinates(50, 75)
        x2, y2 = self.getCoOrdinates(50, 25)
        self.device.swipe(x1, y1, x2, y2)

    def swipeDown(self):
        x1, y1 = self.getCoOrdinates(50, 25)
        x2, y2 = self.getCoOrdinates(50, 75)
        self.device.swipe(x1, y1, x2, y2)

    def scrollUp(self, speed=60):
        x1, y1 = self.getCoOrdinates(50, 75)
        x2, y2 = self.getCoOrdinates(50, 25)
        cmd = "shell input touchscreen swipe {} {} {} {} {}".format(x1,y1,x2,y2,speed)
        command.executeCommandOnDevice(cmd)

    def scrollDown(self,speed=60):
        x1, y1 = self.getCoOrdinates(50, 25)
        x2, y2 = self.getCoOrdinates(50, 75)
        cmd = "shell input touchscreen swipe {} {} {} {} {}".format(x1,y1,x2,y2,speed)
        command.executeCommandOnDevice(cmd)

    def dragUp(self):
        x1, y1 = self.getCoOrdinates(50, 75)
        x2, y2 = self.getCoOrdinates(50, 25)
        self.device.drag(x1, y1, x2, y2)

    def dragDown(self):
        x1, y1 = self.getCoOrdinates(50, 25)
        x2, y2 = self.getCoOrdinates(50, 75)
        self.device.drag(x1, y1, x2, y2)


    def clickUsingText(self, textObj, className=None, instance=0):
        if className is None:
            self.device(text=textObj,instance=instance).click.wait()
            sleep(1)
        else:
            self.device(text=textObj, className= className, instance=instance).click.wait()

    def clearText(self, textObj, instance=0):
        self.device(text=textObj, instance=instance).clear_text()

    def setText(self, textObj, text, instance=0):
        self.device(text=textObj, instance=instance).set_text(text)
        sleep(1)

    def pressDown(self):
        self.device.press.down()
        sleep(1)

    def pressEnter(self):
        self.device.press.enter()
        sleep(1)

    def scrollAndClickAnElement(self, textObj, className=None, instance=0):
        count = 0
        while count <=20:
            if self.isElementwithTextExists(textObj):
                self.clickUsingText(textObj, className, instance)
                break
            else:
                self.scrollUp(500)


    def isElementwithTextExists(self,textObj):
        if self.device(text=textObj).exists:
            return True
        return False

    def checkAndClickUsingText(self, textObj, instance=0):
        counter = 0
        while counter <= 5:
            if self.isElementwithTextExists(textObj):
                self.clickUsingText(textObj,instance)
                sleep(2)
                break
            else:
                sleep(1)
                counter += 1
        return False

    def isElementExistsWithDescription(self,descriptionObj):
        if self.device(description=descriptionObj).exists:
            return True
        return False

    def clickUsingDescription(self, descriptionObj, className=None, instance=0):
        if className is None:
            self.device(text=descriptionObj,instance=instance).click.wait()
            sleep(1)
        else:
            self.device(text=descriptionObj, className= className, instance=instance).click.wait()

    def checkAndClickUsingDescription(self, descriptionObj, instance=0):
        counter = 0
        while counter <= 5:
            if self.isElementExistsWithDescription(descriptionObj):
                self.clickUsingDescription(descriptionObj, instance)
                sleep(2)
                break
            else:
                sleep(1)
                counter += 1
        return False

    def isElementExistsWithResourceId(self, resourceIdObj):
        if self.device(resourceId=resourceIdObj).exists:
            return True
        return False

    def clickUsingResourceId(self, resourceIdObj, className=None, instance=0):
        if className is None:
            self.device(resourceId=resourceIdObj, instance=instance).click.wait()
            sleep(1)
        else:
            self.device(resourceId=resourceIdObj, className=className, instance=instance).click.wait()

    def checkAndClickUsingResourceId(self, resourceIdObj, instance=0):
        counter = 0
        while counter <= 5:
            if self.isElementExistsWithResourceId(resourceIdObj):
                self.clickUsingResourceId(resourceIdObj, instance)
                sleep(2)
                break
            else:
                sleep(1)
                counter += 1
        return False

    def getDeviceProperty(self,property):
        cmd = "shell getprop"
        output = command.executeCommandOnDevice(cmd)
        if output is not None:
            lines = output.splitlines()
            for line in lines:
                if property in line:
                    (key,value) = line.split(':')
                    patternObj = re.search(r'\[(.*)\]',value)
                    if patternObj:
                        return patternObj.group(1)
        else:
            print("property is not found in getprop list")
            return None

    def getDeviceBrand(self):
        brand = self.getDeviceProperty('ro.product.brand')
        print(brand)

    def getDeviceModel(self):
        model = self.getDeviceProperty('ro.product.model')
        print(model)

    def getInstalledApps(self):
        cmd = "shell pm list packages"
        packageList = command.executeCommandOnDevice(cmd)
        if packageList is not None:
            return packageList


    def isApplicationInstalled(self, packageName):
        packageList = self.getInstalledApps()
        if packageList is not None:
            packageLines = packageList.splitlines()
            for line in packageLines:
                if packageName in line:
                    patternObj = re.search(r'package:(.*)',line)
                    if patternObj:
                        pkgName = patternObj.group(1)
                        if pkgName == packageName:
                            return True

        return False

