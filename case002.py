import time

from appium import webdriver
from selenium.webdriver.common.by import By

from api import API
from Email import EMail
from util import Util

desired_caps1 = {
    "platformName": "android",
    "appPackage": "com.alibaba.android.rimet",
    "appActivity": ".biz.SplashActivity",
    "deviceName": "honor",
    "noReset": "true",
    "udid": "UEUNW17221002815"
}

util1 = Util()
email = EMail()
body = """
<h1>测试图片</h1>
<img src="cid:image1"/>    # 引用图片API
"""

util1.random_time(50)

try:
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps1)
    driver.implicitly_wait(10)
    api = API(driver)
    element = api.isElement(By.ID, 'et_pwd_login')
    if element:
        driver.find_element(by=By.ID, value='et_pwd_login').send_keys('lihang1988')
        driver.find_element(by=By.ID, value='btn_next').click()

    # driver.save_screenshot('UEUNW17221002815.png')
    # email.send_mail('打卡成功', content='打卡截图', image_body=body, image='UEUNW17221002815.png')

except:
    email.send_mail('打开失败了，赶紧找人吧！')

time.sleep(2)
driver.quit()