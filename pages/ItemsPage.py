from selenium.webdriver.common.by import By
from time import sleep


class ItemsPage:

    def __init__(self, driver):
        self.driver = driver
        self.open_page()
        self.new_item_button = self.driver.find_element(By.XPATH, '/html/body/div/a')

    def open_page(self):
        self.driver.get("https://test-bees.herokuapp.com/items")
        sleep(1)

    def click_new_item(self):
        self.new_item_button.click()
        sleep(2)