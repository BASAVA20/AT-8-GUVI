from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
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
        time.sleep(2)

        xpath_to_add = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'
        add_button = driver.find_element(By.XPATH, xpath_to_add)
        add_button.click()
        time.sleep(2)

        xpath_to_firstname = '//input[@name="firstName"]'
        firstname_box = driver.find_element(By.XPATH, xpath_to_firstname)
        firstname_box.send_keys("NM")
        time.sleep(2)

        xpath_to_middlename = '//input[@name="middleName"]'
        middlename_box = driver.find_element(By.XPATH, xpath_to_middlename)
        middlename_box.send_keys("BASAVARAJ")
        time.sleep(2)

        xpath_to_lastname = '//input[@name="lastName"]'
        lastname_box = driver.find_element(By.XPATH, xpath_to_lastname)
        lastname_box.send_keys("VALMIKI")
        time.sleep(2)

        xpath_to_employeeid = '//input[@class="oxd-input oxd-input--active"]'
        employeeid = driver.find_element(By.XPATH, xpath_to_employeeid)
        employeeid.send_keys("4461")
        time.sleep(2)

        xpath_to_checkbox = '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]'
        checkbox_element = driver.find_element(By.XPATH, xpath_to_checkbox)
        checkbox_element.click()
        time.sleep(2)

        #xpath_to_username1 = "//input[@class='oxd-input oxd-input--active'][3]"
        xpath_to_username1 = '//input[@autocomplete="off"]'
        username1_element = driver.find_element(By.XPATH, xpath_to_username1)
        username1_element.send_keys("BasuValmiki22")
        time.sleep(2)

        xpath_to_password1 = '//input[@type="password"][1]'
        password_element1 = driver.find_element(By.XPATH, xpath_to_password1)
        password_element1.send_keys("Basu@1234")
        time.sleep(2)

        #xpath_to_password1c = '//input[@type="password"][2]'
        password_element1c = driver.find_element(By.XPATH, "(//input[@type='password'])[2]")
        password_element1c.send_keys("Basu@1234")
        time.sleep(2)

        xpath_to_save = '//button[@type="submit"]'
        save_element = driver.find_element(By.XPATH, xpath_to_save)
        save_element.click()
        time.sleep(2)

        # xpath for Nickname
        xpath_to_nickname = '//label[text()="Nickname"]/following::div[1]/input'
        nickname_element = driver.find_element(By.XPATH, xpath_to_nickname)
        nickname_element.send_keys("basuu")
        time.sleep(2)

        # xpath for id
        xpath_to_id = '//label[text()="Other Id"]/following::div[1]/input'
        id_element = driver.find_element(By.XPATH, xpath_to_id)
        id_element.send_keys("1432")
        time.sleep(2)

        #xpath for DL
        xpath_to_dl = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
        dl_element = driver.find_element(By.XPATH, xpath_to_dl)
        dl_element.send_keys("143256")
        time.sleep(2)

        # xpath for DL date
        xpath_to_dldate = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
        dldate_element = driver.find_element(By.XPATH, xpath_to_dldate)
        dldate_element.send_keys("2022-12-17")
        time.sleep(5)

        #xpath for SSN number
        xpath_to_ssn = '//label[text()="SSN Number"]/following::div[1]/input'
        ssn_element = driver.find_element(By.XPATH, xpath_to_ssn)
        ssn_element.send_keys("1432")
        time.sleep(5)

        # xpath for SIN number
        xpath_to_sin = '//label[text()="SIN Number"]/following::div[1]/input'
        sin_element = driver.find_element(By.XPATH, xpath_to_sin)
        sin_element.send_keys("0987")
        time.sleep(5)

        # xpath for DOB
        xpath_to_dob = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'
        dob_element = driver.find_element(By.XPATH, xpath_to_dob)
        dob_element.send_keys("1999-01-01")
        time.sleep(5)

        # xpath for Gender
        xpath_to_gender = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
        gender_element = driver.find_element(By.XPATH, xpath_to_gender)
        gender_element.click()
        time.sleep(5)

         # xpath for Militaryservice
        xpath_to_military = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input'
        military_element = driver.find_element(By.XPATH, xpath_to_military)
        military_element.send_keys("yes")
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

ss = Project1()
ss.test()
