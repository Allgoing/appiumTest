import time

from appium import webdriver
from selenium.webdriver.common.by import By

from api import API
from Email import EMail

desired_caps = {
    "platformName": "android",
    "appPackage": "com.alibaba.android.rimet",
    "appActivity": ".biz.SplashActivity",
    "deviceName": "UEUNW17221002815",
    "noReset": "true"
}

# email = EMail()
try:
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(60)
    api = API(driver)
    element = api.isElement(By.ID, 'et_pwd_login')
    if element:
        driver.find_element(by=By.ID, value='et_pwd_login').send_keys('lihang1988')
        driver.find_element(by=By.ID, value='btn_next').click()

except:
    pass

time.sleep(2)
driver.quit()