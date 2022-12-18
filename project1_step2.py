from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

class Project1():
    def test(self):

        driver = webdriver.Chrome()
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)

        xpath_to_username = '//input[@name="username"]'
        username_element = driver.find_element(By.XPATH, xpath_to_username)
        username_element.send_keys("Admin")
        time.sleep(2)


        xpath_to_password = '//input[@name="password"]'
        password_element = driver.find_element(By.XPATH, xpath_to_password)
        password_element.send_keys("invalid password")
        time.sleep(2)

        xpath_to_login = '//button[@type="submit"]'
        login_button = driver.find_element(By.XPATH, xpath_to_login)
        login_button.click()
        time.sleep(2)

        invalid_xpath = '//div[@class="oxd-alert-content oxd-alert-content--error"]'
        invalid_element = driver.find_element(By.XPATH, invalid_xpath)
        print(invalid_element.text)
        time.sleep(2)

        driver.close()

ss = Project1()
ss.test()
