import unittest
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from appium.options.android import UiAutomator2Options


appium_server_url = 'http://localhost:4723'

class TestSettings(unittest.TestCase):
    def setUp(self) -> None:
        capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Pixel 5 API 31',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)
        self.driver = webdriver.Remote(appium_server_url, capabilities)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_battery(self) -> None:
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
        el.click()


    def test_find_sound(self) -> None:
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Sound"]')
        el.click()



class TestClock(unittest.TestCase):
    def setUp(self) -> None:
        capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Pixel 5 API 31',
    appPackage='com.android.deskclock',
    appActivity='com.android.deskclock.DeskClock',
    language='en',
    locale='US'
)
        self.driver = webdriver.Remote(appium_server_url, capabilities)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_desk_clock_all_nav (self) -> None:
        el = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='TIMER']")
        el.click()
        el = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='CLOCK']")
        el.click()
        el = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='ALARM']")
        el.click()
        el = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='STOPWATCH']")
        el.click()


    def test_desk_clock_timer (self) -> None:
        el = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='TIMER']")
        el.click()
        key = self.driver.find_element(by=AppiumBy.ID, value="com.android.deskclock:id/timer_setup_digit_1")
        key.click()
        key = self.driver.find_element(by=AppiumBy.ID, value="com.android.deskclock:id/timer_setup_digit_0")
        key.click()
        key.click()
        time.sleep(2)
        timer_loc = self.driver.find_element(by=AppiumBy.ID, value="com.android.deskclock:id/fab")
        timer_loc.click()
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()