from time import sleep
import pandas as pd
from browser import driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver.get("https://www.google.com")
driver.get("https://contacts.google.com/")
sleep(5)

def createContact():
    # Create Contact
    driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[1]/div/gm-coplanar-drawer/div/div/div/div[2]/div/div/div/button').click()
    # Create a Contact
    driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[1]/div/gm-coplanar-drawer/div/div/div/div[15]/div/div/span[1]').click()

    # First Name
    driver.find_element(By.XPATH, '/html/body/div[7]/c-wiz[3]/div/div[1]/div[2]/div/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[1]/div/label/input').send_keys("017987654321")

    # Phone Number
    driver.find_element(By.XPATH, '/html/body/div[7]/c-wiz[3]/div/div[1]/div[2]/div/div/div[4]/div/div/div[2]/div[1]/div[2]/label/input').send_keys("017987654321")

    # Save
    driver.find_element(By.CSS_SELECTOR, "#yDmH0d > c-wiz:nth-child(22) > div > div:nth-child(1) > div.FGgXHc > div > div.as9eHe > div.W3uv9d > div.KPfXEe.N2Njhc > div:nth-child(2) > button").click()

if (driver.current_url =="https://contacts.google.com/"):
    createContact()
else:
    # Go to Signin Page by clicking signin button
    signinBtn = driver.find_element(By.CSS_SELECTOR, "#gb > div > div.gb_Ud > a")
    signinBtn.click()
    driver.find_element(By.CSS_SELECTOR, "#identifierId").send_keys("felix33247@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#identifierNext > div > button").click()
    driver.find_element(By.CSS_SELECTOR, "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input").send_keys("Md$@kib760")
    driver.find_element(By.CSS_SELECTOR, "#passwordNext > div > button").click()



