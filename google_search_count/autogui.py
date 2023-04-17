import pandas as pd
import pyautogui
import time
from random import randint
import pyperclip
import urllib.parse
# read the input excel file


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
                keyword = str(urllib.parse.quote(a)) + ' ' + str(urllib.parse.quote(b)) + ' ' + str(urllib.parse.quote(c))
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

def scrape():
    df = pd.read_excel('url_file.xlsx')
    link = df['url'].unique().tolist()
    link = [x for x in link if pd.notnull(x)]
    result_counts = []
    url_col = []
    urls = []
    for l in link:
        urls.append(l)

    # Open Chrome and navigate to the URL
    pyautogui.hotkey('alt', 'tab')
    # pyautogui.position()

    i = 0
    j = 350
    for i, url in enumerate(urls[i:], start=i):
        i += 1
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.typewrite(url)
        pyautogui.press('enter')
        # Copy text
        pyautogui.moveTo(x=1065, y=269)
        time.sleep(randint(6, 8))
        pyautogui.doubleClick()
        # time.sleep(1)
        pyautogui.hotkey('ctrl', 'c')
        # time.sleep(randint(1, 2))
        x = pyperclip.paste()
        print(str(i) + ' ' + url + ' ' + x)
        url_col.append(url)
        result_counts.append(x)
        # time.sleep(randint(1, 4))
        if (i % 20 == 0):
            time.sleep(3)
            pyautogui.hotkey('ctrl', 'w')
            pyautogui.hotkey('ctrl', 'r')
            # time.sleep(1)
            pyautogui.hotkey('ctrl', 't')
            new_df = pd.DataFrame()
            # new_df['keyword'] = keywords_col
            new_df['url'] = url_col
            new_df['result_count'] = pd.Series(result_counts)
            new_df.apply(lambda col: col.drop_duplicates().reset_index(drop=True))

            # write the output dataframe to an Excel file
            new_df.to_excel('output_file'+str(i)+'.xlsx', index=False)

create_url()