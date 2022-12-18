from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



class project1_step4():
    def test(self):
        driver=webdriver.Chrome()
        url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(url)
        driver.maximize_window()
        time.sleep(2)

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
        time.sleep(2)

        #edting the employee
        edit_element=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[5]/div')
        edit_element.click()
        time.sleep(5)

        # xpath for Nickname
        xpath_to_nickname = '//label[text()="Nickname"]/following::div[1]/input'
        nickname_element1 = driver.find_element(By.XPATH, xpath_to_nickname)
        nickname_element1.send_keys(Keys.CONTROl, 'b')

        nickname_element2 = driver.find_element(By.XPATH, xpath_to_nickname)
        nickname_element2.send_keys(Keys.BACKSPACE)

        nickname_element3 = driver.find_element(By.XPATH, xpath_to_nickname)
        nickname_element3.send_keys("basuu")
        time.sleep(4)

        # xpath for other id
        xpath_to_id = '//label[text()="Other Id"]/following::div[1]/input'
        id_element1 = driver.find_element(By.XPATH, xpath_to_id)
        id_element1.send_keys(Keys.CONTROL, 'b')
        id_element2 = driver.find_element(By.XPATH, xpath_to_id)
        id_element2.send_keys(Keys.BACKSPACE)
        id_element3 = driver.find_element(By.XPATH, xpath_to_id)
        id_element3.send_keys("1432")
        time.sleep(4)

        # xpath for DL
        xpath_to_dl = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
        dl_element1 = driver.find_element(By.XPATH, xpath_to_dl)
        dl_element1.send_keys(Keys.CONTROL, 'b')
        dl_element2 = driver.find_element(By.XPATH, xpath_to_dl)
        dl_element2.send_keys(Keys.BACKSPACE)
        dl_element3 = driver.find_element(By.XPATH, xpath_to_dl)
        dl_element3.send_keys("143256")
        time.sleep(4)

        # xpath for DL date
        xpath_to_dldate = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
        dldate_element1 = driver.find_element(By.XPATH, xpath_to_dldate)
        dldate_element1.send_keys(Keys.CONTROL, 'b')
        dldate_element2 = driver.find_element(By.XPATH, xpath_to_dldate)
        dldate_element2.send_keys(Keys.BACKSPACE)
        dldate_element3 = driver.find_element(By.XPATH, xpath_to_dldate)
        dldate_element3.send_keys("2022-12-17")
        time.sleep(5)

        # xpath for Militaryservice
        xpath_to_military = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input'
        military_element1 = driver.find_element(By.XPATH, xpath_to_military)
        military_element1.send_keys(Keys.CONTROL, 'b')
        military_element2 = driver.find_element(By.XPATH, xpath_to_military)
        military_element2.send_keys(Keys.BACKSPACE)
        military_element3 = driver.find_element(By.XPATH, xpath_to_military)
        military_element3.send_keys("yes")
        time.sleep(5)

        # xpath for Smoker
        xpath_to_smoker = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[2]/div/div[2]/div/label'
        smoker_element = driver.find_element(By.XPATH, xpath_to_smoker)
        smoker_element.click()
        time.sleep(5)

        # xpath to save
        xpath_to_save = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
        save_element = driver.find_element(By.XPATH, xpath_to_save)
        save_element.click()
        time.sleep(5)

        driver.close()

ss=project1_step4()
ss.test()