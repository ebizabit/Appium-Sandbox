import unittest
import os
from random import randint
from appium import webdriver
from time import sleep

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        self.success = True
        self.desired_caps = {}
        self.desired_caps['appium-version'] = '1.0'
        self.desired_caps['platformName'] = 'iOS'
        self.desired_caps['platformVersion'] = '8.1'
        self.desired_caps['deviceName'] = 'iPhone 6'
        self.desired_caps['app'] = os.path.abspath('/Users/mikesan217/Library/Developer/Xcode/DerivedData/TestApp-dwcfgvjlcwaymugwkjpiovasnyil/Build/Products/Debug-iphonesimulator/TestApp.app')

        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(60)

    def acceptAlert(self):
        self.driver.switch_to_alert().accept()

    #def tearDown(self):
        #self.driver.quit()
       
    def testSum(self):
        #randint(0, 10)
        self.driver.find_element_by_name("IntegerA").click();
        self.driver.find_element_by_name("more, numbers").click();
        self.driver.find_element_by_name("3").click();
        self.driver.find_element_by_name("IntegerB").click();
        self.driver.find_element_by_name("more, numbers").click();
        self.driver.find_element_by_name("5").click();
        self.driver.find_element_by_name("Done").click();
        self.driver.find_element_by_name("ComputeSumButton").click();


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)