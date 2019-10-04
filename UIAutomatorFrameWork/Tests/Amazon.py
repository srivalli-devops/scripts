import sys
sys.path.append("../UIAutomatorFrameWork/")
from Lib.uiAutomator import uiAutomator
from time import sleep

class Amazon(uiAutomator):
    def __init__(self):
        super().__init__()

    def addItemToCart(self):
        self.openAppMenu()
        self.clickUsingText("Amazon Shopping")
        self.clickUsingText("Search")
        self.clearText("Search")
        self.setText("Search", "one plus 7 mobile")
        self.pressDown()
        self.pressEnter()
        self.clickUsingText("OnePlus 7 (Mirror Grey, 6GB RAM, Optic AMOLED Display, 128GB Storage, 3700mAH Battery)")
        self.scrollAndClickAnElement("Add to Cart")
        self.checkAndClickUsingText("DONE")

if __name__ == "__main__":
    testObj = Amazon()
    testObj.getDeviceInstance()
    if testObj.device is not None:
        testObj.addItemToCart()
        testObj.getDeviceBrand()
        testObj.getDeviceModel()
    else:
        print("unable to get the device instance. Check the device connection")
