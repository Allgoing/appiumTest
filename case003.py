import time
import threading

from appium import webdriver
from selenium.webdriver.common.by import By

from api import API
from Email import EMail

desired_caps1 = {
    "platformName": "android",
    "appPackage": "com.alibaba.android.rimet",
    "appActivity": ".biz.SplashActivity",
    "deviceName": "honor",
    "noReset": "true",
    "udid": "UEUNW17221002815"
}

desired_caps2 = {
    "platformName": "android",
    "appPackage": "com.alibaba.android.rimet",
    "appActivity": ".biz.SplashActivity",
    "deviceName": "sumsung",
    "noReset": "true",
    "udid": "64de8478"
}


# email = EMail()
# body = """
# <h1>测试图片</h1>
# <img src="cid:image1"/>    # 引用图片
# """


def task1():
    email = EMail()
    body = """
    <h1>测试图片</h1>
    <img src="cid:image1"/>    # 引用图片
    """

    try:
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps1)
        driver.implicitly_wait(10)
        api = API(driver)
        element = api.isElement(By.ID, 'et_pwd_login')
        if element:
            driver.find_element(by=By.ID, value='et_pwd_login').send_keys('lihang1988')
            driver.find_element(by=By.ID, value='btn_next').click()

        time.sleep(3)
        driver.save_screenshot('UEUNW17221002815.png')
        email.send_mail('打卡成功', content='打卡截图', image_body=body, image='UEUNW17221002815.png')

    except:
        email.send_mail('打开失败了，赶紧找人吧！')

    time.sleep(2)
    driver.quit()


def task2():
    email = EMail()
    body = """
    <h1>测试图片</h1>
    <img src="cid:image1"/>    # 引用图片
    """

    try:
        driver = webdriver.Remote('http://localhost:4725/wd/hub', desired_caps2)
        driver.implicitly_wait(10)
        api = API(driver)
        element = api.isElement(By.ID, 'et_pwd_login')
        if element:
            driver.find_element(by=By.ID, value='et_pwd_login').send_keys('qetuo13579')
            driver.find_element(by=By.ID, value='btn_next').click()

        time.sleep(3)
        driver.save_screenshot('64de8478.png')
        email.send_mail('打卡成功', content='打卡截图', to_addrs_in='409803186@qq.com', image_body=body, image='64de8478.png')

    except:
        email.send_mail('打开失败了，赶紧找人吧！')

    time.sleep(2)
    driver.quit()


threads = []
t1 = threading.Thread(target=task1)
threads.append(t1)

t2 = threading.Thread(target=task2)
threads.append(t2)

if __name__ == '__main__':
    for i in threads:
        i.start()
