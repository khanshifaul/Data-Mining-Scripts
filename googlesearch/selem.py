from selenium import webdriver
from selenium.webdriver.common.by import By
# from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.chrome.options import Options
import pandas as pd
from time import sleep
from random import randint

# options = EdgeOptions()
# options.use_chromium = True
# driver = Edge(options=options)
options = Options()
# options.headless = True
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
options.add_extension("caahalkghnhbabknipmconmbicpkcopl.crx")
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")
driver.find_element_by_xpath('//*[@id="gb"]/div/div[2]/a').click()
# driver.find_element_by_xpath('//*[@id="gb"]/div/div[1]/a').click()


# read the input excel file
df = pd.read_excel('T-Music Combination.xlsx')

# concatenate the three columns into a single column
keywords = []
genre = df['Music Genre'].unique().tolist()
genre = [x for x in genre if pd.notnull(x)]
instrument = df['Instrument'].unique().tolist()
instrument = [x for x in instrument if pd.notnull(x)]
ethnicity = df['Ethnicity'].unique().tolist()
ethnicity = [x for x in ethnicity if pd.notnull(x)]
link = df['Google Search Link'].unique().tolist()
link = [x for x in link if pd.notnull(x)]

# for a in genre:
#     for b in instrument:
#         for c in ethnicity:
#             keyword = str(a) + ' ' + str(b) + ' ' + str(c)
#             keywords.append(keyword)

# print(len(keywords))

keywords_col = []
urls = []
result_counts = []
url_col = []
# for keyword in keywords:
#     keyword_joined = "+".join(keyword.split())
#     # print(keyword)
#     keywords_col.append(keyword)
#     # construct the google search URL
#     url = 'https://www.google.com/search?q=' + keyword_joined
#     urls.append(url)

for l in link:
    urls.append(l)

# Open Chrome and navigate to the URL
# pyautogui.hotkey('alt', 'tab')
# pyautogui.position()

i = 1420
for i, url in enumerate(urls[i:], start=i):
    i += 1
    driver.get(url+'&hl=en')
    driver.implicitly_wait(5)
    result_count = driver.find_element_by_id("result-stats")
    if result_count is None:
        driver.implicitly_wait(5)
        new_df = pd.DataFrame()
        # new_df['keyword'] = keywords_col
        new_df['url'] = url_col
        new_df['result_count'] = pd.Series(result_counts)
        new_df.apply(lambda col: col.drop_duplicates().reset_index(drop=True))

        # write the output dataframe to an Excel file
        new_df.to_excel('output_file'+str(i)+'.xlsx', index=False)
    elif result_count is not None:
        result_count_text = driver.find_element_by_id("result-stats").text
        result_count_text = int(''.join(filter(str.isdigit, result_count_text)))
        url_col.append(url)
        result_counts.append(result_count_text)
        print(str(i) + ' ' + url + ' ' + str(result_count_text))
        if (i%20==0):
            driver.get('google.com')
            element.click()
            new_df = pd.DataFrame()
            # new_df['keyword'] = keywords_col
            new_df['url'] = url_col
            new_df['result_count'] = pd.Series(result_counts)
            new_df.apply(lambda col: col.drop_duplicates().reset_index(drop=True))

            # write the output dataframe to an Excel file
            new_df.to_excel('output_file'+str(i)+'.xlsx', index=False)
