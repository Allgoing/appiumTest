import time
import random


class Util(object):

    def random_time(self, number):
        random_number = random.randint(0, number)
        time.sleep(random_number)