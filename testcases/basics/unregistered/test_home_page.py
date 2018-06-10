from pageobject.home_page import HomePage
from pageobject.stores_page import StoresPage
from parameterized import parameterized


class TestHomePage(HomePage, StoresPage):
    @parameterized.expand([('Cairo', 'Pizza Milano', True),
                           ('Cairo', "RANDAM", False)])
    def test002_discover_near_rest(self, location, restaurant, assertion):
        """ UEA-002
        *Test case to make sure that user can search for a specific restaurant*

            **Test Scenario:**

            - Get the ‘stores’ page
            - Search for the restaurant name according to data driven input.
            - Assert the restaurant is existing or not according to data driven input.
        """
        self.find_food(location=location)
        restauarent_details = self.get_restaurant_details(restaurant=restaurant)
        for restaurant_data in restauarent_details:
            if restaurant in restaurant_data['title']:
                self.assertEqual(assertion, True)
                break
        else:
            self.assertEqual(assertion, False)
