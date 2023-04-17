from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
from time import sleep
from random import randint


df = pd.read_excel('drawing\Book1.xlsx')

drawing_numbers = df['Drawing Number'].unique().tolist()
drawing_numbers = [x for x in drawing_numbers if pd.notnull(x)]
titles = df['Title'].unique().tolist()
# titles = [x for x in drawing_numbers if pd.notnull(x)]

new_drawing_numbers = []
urls = []
new_titles =[]

# Setting up Chrome
options = Options()
# options.headless = True
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
# options.add_extension("caahalkghnhbabknipmconmbicpkcopl.crx")
driver = webdriver.Chrome(
    executable_path="drawing\chromedriver.exe", options=options)

# Opening the URL
driver.get("https://detail-library.co.uk/")
# find and click search button
for drawing_number in drawing_numbers:
    driver.execute_script("document.getElementById('et_top_search').click()")
    search = driver.find_element_by_xpath(
        '//*[@id="main-header"]/div[2]/div/form/input')
    search.send_keys(Keys.CONTROL+'a')
    search.send_keys(drawing_number)
    search.send_keys(Keys.RETURN)
    # getting current URL
    c_url = driver.current_url
    new_drawing_numbers.append(drawing_number)
    urls.append(c_url)
    new_titles.append(title)



new_df = pd.DataFrame()

new_df['Drawing Number'] = new_drawing_numbers
new_df['URL'] = pd.Series(urls)
new_df['Title'] = new_titles

# write the output dataframe to an Excel file
new_df.to_excel('drawing\output_file.xlsx', index=False)
driver.close()