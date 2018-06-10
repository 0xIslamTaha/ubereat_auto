from pageobject.objects import objects
from pageobject.basic_class import BaseTest
import time


class HomePage(BaseTest):
    def find_food(self, location):
        self.driver.find_element_by_id(objects['add_sec']).send_keys(location)
        self.driver.find_element_by_xpath(objects['add_item_1']).click()
        time.sleep(5)

