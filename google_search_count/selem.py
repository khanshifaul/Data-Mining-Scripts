from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
from time import sleep
from random import randint
import re
import nopecha
import urllib.parse

options = Options()
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_extension("caahalkghnhbabknipmconmbicpkcopl.crx")
driver = webdriver.Chrome(options=options)


def create_url():
    df = pd.read_excel('T-Music Combination.xlsx')
    keywords = []
    genre = df['Music Genre'].unique().tolist()
    genre = [x for x in genre if pd.notnull(x)]
    instrument = df['Instrument'].unique().tolist()
    instrument = [x for x in instrument if pd.notnull(x)]
    ethnicity = df['Ethnicity'].unique().tolist()
    ethnicity = [x for x in ethnicity if pd.notnull(x)]
    for a in genre:
        for b in instrument:
            for c in ethnicity:
                keyword = str(urllib.parse.quote(
                    a)) + ' ' + str(urllib.parse.quote(b)) + ' ' + str(urllib.parse.quote(c))
                keywords.append(keyword)

    print(len(keywords))

    keywords_col = []
    urls = []
    for keyword in keywords:
        keyword_joined = "+".join(keyword.split())
        # print(keyword)
        keywords_col.append(keyword)
        # construct the google search URL
        url = 'https://www.google.com/search?q=' + keyword_joined
        urls.append(url)
    new_df = pd.DataFrame()
    new_df['keyword'] = keywords_col
    new_df['url'] = urls
    new_df.apply(lambda col: col.drop_duplicates().reset_index(drop=True))

    # write the output dataframe to an Excel file
    new_df.to_excel('url_file.xlsx', index=False)


def google_login():
    driver.get('https://www.google.com')
    sleep(3)
    signin_btn = driver.find_element(By.XPATH, '//*[@id="gb"]/div/div[2]/a')
    signin_btn.click()
    sleep(2)
    username = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
    username.send_keys('lookcool222')
    username.send_keys(Keys.RETURN)
    sleep(5)
    passwd = driver.find_element(
        By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
    passwd.send_keys('lookcool222')
    passwd.send_keys(Keys.RETURN)
    sleep(10)


def captcha_solve():
    print('Solving captcha')
    nopecha.api_key = 'YOUR_API_KEY'
    # Call the Recognition API
    clicks = nopecha.Recognition.solve(
        type='recaptcha',
        task='Select all squares with vehicles.',
        image_urls=['https://nopecha.com/image/demo/recaptcha/4x4.png'],
        grid='4x4'
    )

    # Print the grids to click
    print(clicks)


def scrape():
    df = pd.read_excel('url_file.xlsx')
    link = df['url'].unique().tolist()
    link = [x for x in link if pd.notnull(x)]
    urls = []
    result_counts = []
    url_col = []
    for l in link:
        urls.append(l)
    i = 0
    for i, url in enumerate(urls[i:], start=i):
        i += 1
        url = url+'&hl=en'
        driver.get(url)
        driver.implicitly_wait(5)

        if driver.current_url != url:
            print(driver.current_url)
            sleep(15)
            url_col.append(url)
            result_counts.append("result_count_text")
            new_df = pd.DataFrame()
            new_df['url'] = url_col
            new_df['result_count'] = pd.Series(result_counts)
            new_df.apply(
                lambda col: col.drop_duplicates().reset_index(drop=True))
            new_df.to_excel('output_file'+str(i)+'.xlsx', index=False)
        elif driver.current_url == url:
            result_count = driver.find_element(By.ID, "result-stats")
            result_count_text = driver.find_element(By.ID, "result-stats").text
            result_count_text = int(re.findall(
                r'\d+', result_count_text.replace(',', ''))[0])
            url_col.append(url)
            result_counts.append(result_count_text)
            print(str(i) + ' ' + url + ' ' + str(result_count_text))
            if i % 20 == 0 or i == 350:
                new_df = pd.DataFrame()
                new_df['url'] = url_col
                new_df['result_count'] = pd.Series(result_counts)
                new_df.apply(
                    lambda col: col.drop_duplicates().reset_index(drop=True))
                new_df.to_excel('output_file'+str(i)+'.xlsx', index=False)


# google_login()
# create_url()
scrape()
