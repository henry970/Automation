from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Selected browser we want to use to run this test
driver = webdriver.Chrome()


# open the site 
driver.get("https://stg-app.leatherback.co/signin/")

# Incrase the size of the window
driver.maximize_window()


# login page
# Enter email on the email field
Username = driver.find_element(By.ID, "email").send_keys("simigold@internetkeno.com")
time.sleep(2)

# Enter password on the password field
Password = driver.find_element(By.ID, "password-input").send_keys('Adaobi93@')
time.sleep(2)

# make password visisble 
Password = driver.find_element(By.ID, "password-btn").click()

# click the sigin button
click_BNT = driver.find_element(By.ID,"submit-btn").click()
time.sleep(5)

