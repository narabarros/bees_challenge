from selenium.webdriver.common.by import By
from time import sleep


class NewDepositPage:

    def __init__(self, driver):
        self.driver = driver
        self.name_input = self.driver.find_element(By.ID, 'deposit_name')
        self.address_input = self.driver.find_element(By.ID, 'deposit_address')
        self.city_input = self.driver.find_element(By.ID, 'deposit_city')
        self.state_input = self.driver.find_element(By.ID, 'deposit_state')
        self.zipcode_input = self.driver.find_element(By.ID, 'deposit_zipcode')
        self.click_create_deposit_button = self.driver.find_element(By.NAME, 'commit')

    def fill_form(self, name, address, city, state, zipcode):
        self.name_input.send_keys(name)
        self.address_input.send_keys(address)
        self.city_input.send_keys(city)
        self.state_input.send_keys(state)
        self.zipcode_input.send_keys(zipcode)

    def click_create_deposit(self):
        self.driver.find_element(By.NAME, 'commit').click()
        sleep(2)
