from selenium.webdriver.common.by import By
from time import sleep


class DepositPage:
    def __init__(self, driver):
        self.driver = driver
        self.open_deposit_page()
        self.new_deposit_button = self.driver.find_element(By.XPATH, '/html/body/div/a')

    def open_deposit_page(self):
        self.driver.get("https://test-bees.herokuapp.com/deposits")
        sleep(1)

    def click_new_deposit(self):
        self.new_deposit_button.click()
        sleep(1)
