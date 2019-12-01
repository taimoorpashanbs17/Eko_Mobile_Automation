import unittest
from appium import webdriver

class device_Setup(unittest.TestCase):
    def setUp(self):
        self.dc = {}
        self.dc['udid'] = 'BBPBB19307204039'
        self.dc['appPackage'] = 'com.ekoapp.ekos'
        self.dc['appActivity'] = 'com.ekoapp.eko.EkoHome'
        self.dc['platformName'] = 'android'
        self.dc['autoGrantPermissions'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)
        # return self.driver

    def tearDown(self):
        self.driver.quit()


