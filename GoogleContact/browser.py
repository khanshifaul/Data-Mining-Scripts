from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


options = Options()
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
# options.add_argument("start-maximized")
options.add_argument('disable-infobars')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--disable-blink-features=AutomationControlled')
# # options.add_extension("caahalkghnhbabknipmconmbicpkcopl.crx")

options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# driver = webdriver.Chrome(".\webdriver\chromedriver.exe", options=options)

driver = webdriver.Chrome(options=options)
