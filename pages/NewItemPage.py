from selenium.webdriver.common.by import By
from time import sleep


class NewItemPage:

    def __init__(self, driver):
        self.driver = driver
        self.open_new_item_page()
        self.name_input = self.driver.find_element(By.ID, 'item_name')
        self.height_input = self.driver.find_element(By.ID, 'item_height')
        self.width_input = self.driver.find_element(By.ID, 'item_width')
        self.weight_input = self.driver.find_element(By.ID, 'item_weight')
        self.click_create_item_button = self.driver.find_element(By.NAME, 'commit')

    def open_new_item_page(self):
        self.driver.get("https://test-bees.herokuapp.com/items/new")
        sleep(1)

    def fill_form(self, name, height, width, weight):
        self.name_input.send_keys(name)
        self.height_input.send_keys(height)
        self.width_input.send_keys(width)
        self.weight_input.send_keys(weight)

    def click_create_item(self):
        self.click_create_item_button.click()
        sleep(2)
