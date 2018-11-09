import time
import random


class API(object):

    def __init__(self, driver):
        self.driver = driver

    def isElement(self, fun, value):

        flag = None
        self.driver.implicitly_wait(60)

        try:
            self.driver.find_element(by=fun, value=value)
            flag = True
        except:
            flag = False
        finally:
            return flag
