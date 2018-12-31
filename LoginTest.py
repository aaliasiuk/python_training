# -*- coding: utf-8 -*-
from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
#from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import NoAlertPresentException
import unittest

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, username="aaliasiuk@gazelle.com", password="Sqa2018sqa")
        self.logout(driver)

    def test_invalid_login(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, username="aaliasiuk@gazelle.com", password="invalid")
        #self.logout(driver)

    def logout(self, driver):
        driver.find_element_by_id("customer_logout_link").click()

    def login(self, driver, username, password):
        driver.find_element_by_id("customer_login_link").click()
        driver.find_element_by_id("CustomerEmail").clear()
        driver.find_element_by_id("CustomerEmail").send_keys(username)
        driver.find_element_by_id("CustomerPassword").click()
        driver.find_element_by_id("CustomerPassword").clear()
        driver.find_element_by_id("CustomerPassword").send_keys(password)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/following::input[2]").click()

    def open_home_page(self, driver):
        driver.get("https://buy.gazellestaging.com/")

    # def is_element_present(self, how, what):
    #     try: self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException as e: return False
    #     return True
    #
    # def is_alert_present(self):
    #     try: self.driver.switch_to_alert()
    #     except NoAlertPresentException as e: return False
    #     return True
    #
    # def close_alert_and_get_its_text(self):
    #     try:
    #         alert = self.driver.switch_to_alert()
    #         alert_text = alert.text
    #         if self.accept_next_alert:
    #             alert.accept()
    #         else:
    #             alert.dismiss()
    #         return alert_text
    #     finally: self.accept_next_alert = True
    #
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
