from selenium.webdriver.common.by import By
from time import sleep


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.open_page()
        self.email_field = self.driver.find_element(By.ID, 'user_email')
        self.password_field = self.driver.find_element(By.ID, 'user_password')
        self.submit_button = self.driver.find_element(By.XPATH, '//*[@id="new_user"]/div[2]/input')

    def open_page(self):
        self.driver.get("https://test-bees.herokuapp.com/")

    def sign_in(self, email, password):
        self.email_field.send_keys(email)
        self.password_field.send_keys(password)
        sleep(2)

    def click_submit(self):
        self.submit_button.click()
        sleep(2)