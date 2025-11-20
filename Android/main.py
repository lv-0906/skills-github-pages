from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
desired_caps = {
    "platformName": "Android",
    "platformVersion": "9",
    "udid": "MUA5DMOTERNIRON22101751",
    "appPackage": "com.motern.cherry.monitor",
    "appActivity": "com.motern.cherry.monitor.MainActivity",
    "automationName": "UiAutomator2"
}
def test_basic_operations():
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    try:
        Deposit = driver.find_element(AppiumBy.ID,'com.motern.cherry.monitor:id/button_deposit_bags')
        Deposit.click()
        print("已点击存包按钮")
    finally:
        print("测试完成，关闭驱动")
        driver.quit()
