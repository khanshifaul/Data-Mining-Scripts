from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chromeOptions = Options()
chromeOptions.debugger_address = "127.0.0.1:" + "8888"
# options.add_argument("--headless")
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("start-maximized")
chromeOptions.add_argument("disable-infobars")
chromeOptions.add_argument("--disable-dev-shm-usage")
chromeOptions.add_argument("--disable-blink-features=AutomationControlled")
# options.add_extension("caahalkghnhbabknipmconmbicpkcopl.crx")

# Run this command before
# chrome.exe --user-data-dir="%LOCALAPPDATA%\Google\Chrome\User Data" --remote-debugging-port=8888

driver = webdriver.Chrome(
    service=Service(
        executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe"
    ),
    options=chromeOptions,
)
