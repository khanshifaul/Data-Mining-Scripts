import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
import random
import time
from random import randint
import numpy as np


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

for a in genre:
    for b in instrument:
        for c in ethnicity:
            keyword = str(a) + ' ' + str(b) + ' ' + str(c)
            keywords.append(keyword)

print(len(keywords))

result_counts = []
urls = []

i = 0
for keyword in keywords:
    i += 1
    keyword_joined = "+".join(keyword.split())
    # construct the google search URL
    url = 'https://www.google.com/search?q=' + keyword_joined
    # set multiple user agent strings
    headers_list = [
        {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'},
        {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'},
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'},
        {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0'}
    ]

    # choose a random header
    headers = random.choice(headers_list)
    time.sleep(randint(1,5))
    # send a GET request to the URL with the headers
    res = requests.get(url, headers=headers)
    # parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(res.content, 'lxml')
    # extract the search result count from the HTML using soup.find()
    result_count_elem = soup.find('div', {'id': 'result-stats'})
    if result_count_elem is None:
      print('error: result_count_elem not found')
    else:
        result_count_text = result_count_elem.text
        # extract only numbers from text
        result_count = int(''.join(filter(str.isdigit, result_count_text)))
        urls.append(url)
        result_counts.append(str(result_count))
        print(str(i)+ ' ' + url + ' ' + str(result_count))
        


# loop through each search query and scrape the search result count using multithreading


# create a new DataFrame with the desired column and values
new_df = pd.DataFrame()

new_df['keyword'] = keywords
new_df['url'] = urls
new_df['result_count'] = result_counts

# write the output dataframe to an Excel file
new_df.to_excel('output_file.xlsx', index=False)
