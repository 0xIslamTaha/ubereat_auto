from pageobject.objects import objects
from pageobject.basic_class import BaseTest
import time


class StoresPage(BaseTest):
    def get_restaurant_details(self, restaurant):
        restuarants_details = []
        search_element = self.driver.find_element_by_xpath(objects['search_key'])
        search_element.send_keys(restaurant)
        search_element.submit()

        time.sleep(5)
        all_data_items = self.driver.find_elements_by_tag_name('a')
        for item in all_data_items:
            restaurant = {'title': '',
                          'status': '',
                          'details': ''}
            data = item.text.split('\n')
            if data:
                if "Closed" == data[0]:
                    restaurant['status'] = 'Closed'
                    restaurant['title'] = data[1]
                    restaurant['details'] = data[2:]
                elif "Currently unavailable" == data[0]:
                    restaurant['status'] = 'Currently unavailable'
                    restaurant['title'] = data[1]
                    restaurant['details'] = data[2:]
                else:
                    restaurant['status'] = 'Open'
                    restaurant['title'] = data[0]
                    restaurant['details'] = data[1:]
                restuarants_details.append(restaurant)

        return restuarants_details
