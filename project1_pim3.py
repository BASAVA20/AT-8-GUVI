from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

class project1_step4():
    def test(self):
        driver = webdriver.Chrome()  # intializes the driver object
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        driver.maximize_window()
        time.sleep(3)

        xpath_to_username = '//input[@name="username"]'
        username_element = driver.find_element(By.XPATH, xpath_to_username)
        username_element.send_keys("Admin")
        time.sleep(2)

        xpath_to_password = '//input[@name="password"]'
        password_element = driver.find_element(By.XPATH, xpath_to_password)
        password_element.send_keys("admin123")
        password_element.send_keys(Keys.ENTER)
        time.sleep(2)

        #clicking on PIM
        pim_element = driver.find_element(By.XPATH,'//a[@href="/web/index.php/pim/viewPimModule"]')
        pim_element.click()
        time.sleep(5)
        #deleting a employee details
        delete_element = driver.find_element(By.XPATH,'//button[@class="oxd-icon-button oxd-table-cell-action-space"]')
        delete_element.click()
        print(delete_element.text)
        time.sleep(5)
        button_element = driver.find_element(By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]')
        button_element.click()
        print(button_element.text)
        time.sleep(5)

        driver.close()



ss= project1_step4()
ss.test()