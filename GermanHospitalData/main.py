from time import sleep
import pandas as pd
from browser import driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

mainurl = "https://www.firmenabc.at/result.aspx?what=&where=1030+Wien&exact=false&inTitleOnly=false&l=&si=0&iid=&sid=-1&did=&cc="
driver.get(mainurl)
sleep(5)

driver.execute_script("document.querySelector('#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection').click()")
original_window = driver.current_window_handle

data = []

for x in range(0,2):
    links = driver.find_elements(By.CSS_SELECTOR, 'div.result-content > a')
    for link in links[:5]:
        url = link.get_attribute('href')
        driver.switch_to.new_window('tab')
        driver.get(url)
        sleep(5)
        # name = driver.find_element(By.CSS_SELECTOR, '#main-container > div > div.col-sm-8.main-col > div.company.pull-left > div.company-content.media.card > div.media-body > div.card-heading.mobile-portrait-row > div:nth-child(2)').text
        name = driver.find_element(By.XPATH, '//*[@id="main-container"]/div/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]').text
        try:
            mail = driver.find_element(By.CSS_SELECTOR, 'div.mobile-portrait-row.mail > a').text
        except NoSuchElementException:
            mail = 'Not found'
        print(str(links.index(link)+1) + '. ' + url + ' | ' + name + ' | ' + mail + '\n')
        data.append({'url': url, 'name': name, 'mail': mail})
        driver.close()
        driver.switch_to.window(original_window)
    df = pd.DataFrame(data)
    df.to_excel('snapshot_' + str(x) + '_FirmenABC_1030.xlsx')
    driver.find_element(By.XPATH, '//*[@id="main-container"]/div[1]/div[1]/nav/a[2]').click()
    sleep(5)

df = pd.DataFrame(data)
print('-- -- '*10 + 'Scraping Finished ' + '-- -- '*10)

df.to_excel('FirmenABC_1030.xlsx')
print('-- -- '*10 + 'XLSX File Created ' + '-- -- '*10)

