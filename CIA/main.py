from time import sleep
import pandas as pd
from browser import driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver.get("https://www.cia.gov/the-world-factbook/countries/barbados/")
sleep(5)

country_name = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/div/div[1]/h1').text
print(country_name)

# """Introduction
# Geography
# People and Society
# Environment
# Government
# Economy
# Energy
# Communications
# Transportation
# Military and Security
# Transnational Issues"""

