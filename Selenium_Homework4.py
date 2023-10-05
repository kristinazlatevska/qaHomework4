import random
import unittest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class ShopTests(unittest.TestCase):

    def login(self, driver, username, password):
        username_input = driver.find_element(By.CSS_SELECTOR, "[data-testid=store-name-input]")
        password_input = driver.find_element(By.CSS_SELECTOR, "[data-testid=password-input]")
        login_button = driver.find_element(By.CSS_SELECTOR, "[data-testid=login-button]")

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

    def register(self, driver, username, password):
        username_input = driver.find_element(By.CSS_SELECTOR, "[data-testid=store-name-input]")
        username_input.send_keys(username)

        password_input = driver.find_element(By.CSS_SELECTOR, "[data-testid=password-input]")
        password_input.send_keys(password)

        register_button = driver.find_element(By.CSS_SELECTOR, "[data-testid=register-button]")
        register_button.click()

    def test_register(self):
        driver = webdriver.Chrome()
        driver.get("https://qaworkshop.netlify.app/")
        self.register(driver, "User1234567", "pass123")

        message = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "[data-testid=message]")))
        self.assertTrue(message.text == "User registered")
        driver.quit()

    def test_login(self):
        driver = webdriver.Chrome()
        driver.get("https://qaworkshop.netlify.app/")
        self.login(driver, "Kristina", "academy12345")

        empty_order = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "[data-testid=empty-order-button]")))
        self.assertTrue(empty_order.text == "EMPTY ORDER!")
        driver.quit()

    def test_delete(self):
        driver = webdriver.Chrome()
        driver.get("https://qaworkshop.netlify.app/")
        self.register(driver, "User555", "pass123")

        delete_button = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "[data-testid=delete-button]")))
        delete_button.click()

        message = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "[data-testid=message]")))
        self.assertTrue(message.text == "User deleted!")

        driver.quit()

    def test_addBug(self):
        driver = webdriver.Chrome()
        driver.get("https://qaworkshop.netlify.app/")
        self.login(driver, "Kristina", "academy12345")

        ladybug_button = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, '/html/body/div/div/div[1]/ul/li[7]/button')))
        ladybug_button.click()

        order_item = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "[data-testid=order-item]")))
        self.assertTrue(order_item)
        sleep(10)
        driver.quit()

    def test_createNewBug(self):
        driver = webdriver.Chrome()
        driver.get("https://qaworkshop.netlify.app/")
        self.login(driver, "Kristina", "academy12345")

        clear_inventory_button = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "[data-testid=clear-inventory-button]")))
        clear_inventory_button.click()

        bug_name_input = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "[data-testid=bug-name-input]")))
        bug_price_input = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "[data-testid=bug-price-input]")))
        bug_description_input = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "[data-testid=bug-description-input]")))

        bug_name_input.send_keys("Dragonfly")
        bug_price_input.send_keys("2599")
        bug_description_input.send_keys("Dragonfly species are characterized by long bodies with two narrow pairs of wings")

        add_bug_button = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "[data-testid=bug-submit-button]")))
        add_bug_button.click()

        new_bug_element = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "/html/body/div/div/div[1]/ul/li[1]/button")))
        new_bug_element.click()

        sleep(5)

        order_item = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "[data-testid=order-item]")))
        self.assertTrue(order_item)
        driver.quit()

    def test_emptyOrder(self):   # additional test 1
        driver = webdriver.Chrome()
        driver.get("https://qaworkshop.netlify.app/")
        self.login(driver, "Kristina", "academy12345")
        empty_order_button = WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid=empty-order-button]")))
        empty_order_button.click()
        driver.save_screenshot("test_empty_order.png")

        total_price = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "[data-testid=total-price]")))
        self.assertTrue(total_price.text == "$0.00")
        sleep(3)
        driver.quit()

    def test_loadSampleBugs(self):  # additional test 2
        driver = webdriver.Chrome()
        driver.get("https://qaworkshop.netlify.app/")
        self.login(driver, "Kristina", "academy12345")

        clear_inventory_button = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "[data-testid=clear-inventory-button]")))
        clear_inventory_button.click()

        sleep(3)

        load_sample_button = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "[data-testid=load-sample-bugs-button]")))
        load_sample_button.click()

        driver.save_screenshot("test_loadSampleBugs.png")
        order_button = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "[data-testid=add-to-order-button")))
        self.assertTrue(order_button)
        sleep(3)
        driver.quit()

    def test_addMoreQuantity(self):  # additional test 3
        driver = webdriver.Chrome()
        driver.get("https://qaworkshop.netlify.app/")
        self.login(driver, "Kristina", "academy12345")

        add_to_order_button = WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "[data-testid=add-to-order-button]")))

        quantity = random.randint(2, 10)

        for _ in range(quantity):
            add_to_order_button.click()

        driver.save_screenshot("test_AddMoreQuantity.png")

        count_element = WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "[data-testid=bug-count-bug21]")))
        count_text = count_element.get_property('textContent')
        order_quantity = int(count_text)

        sleep(5)
        self.assertTrue(quantity == order_quantity)
        driver.quit()


if __name__ == '__main__':
    unittest.main()
