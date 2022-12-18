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
        password_element.send_keys("admin123")
        time.sleep(2)

        xpath_to_login = '//button[@type="submit"]'
        login_button = driver.find_element(By.XPATH, xpath_to_login)
        login_button.click()
        time.sleep(2)






        xpath_to_pim = '//a[@href="/web/index.php/pim/viewPimModule"]'
        pim_element = driver.find_element(By.XPATH, xpath_to_pim)
        pim_element.click()
        time.sleep(5)








        driver.close()

ss = Project1()
ss.test()

