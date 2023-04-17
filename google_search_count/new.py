import pandas as pd
import requests
from bs4 import BeautifulSoup
import random
from time import sleep
from random import randint
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
#     print(keyword)
#     keywords_col.append(keyword)
#     # construct the google search URL
#     url = 'https://www.google.com/search?q=' + keyword_joined
#     print(url)
#     urls.append(url)
for l in link:
    urls.append(l)

i = 1340
for i, url in enumerate(urls[1340:1400], start=1340):
    i += 1
    # set multiple user agent strings
    headers_list = [
        {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'},
        # {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44',
        #  'Referer': 'https://www.google.com/'}
    ]
    # choose a random header
    headers = random.choice(headers_list)
    # send a GET request to the URL with the headers
    response = requests.get(url, headers=headers)
    sleep(randint(1, 5))
    # parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'lxml')
    print(soup)
    # extract the search result count from the HTML using soup.find()
    result_count_elem = soup.find('div', {'id': 'result-stats'})

    if result_count_elem is None:
        print('error')
        break
    elif result_count_elem is not None:
        result_count_text = result_count_elem.text
        # extract only numbers from text
        result_count = int(''.join(filter(str.isdigit, result_count_text)))
        str(result_count)
        print(str(i) + ' ' + url + ' ' + result_count)
        
        # create a new DataFrame with the desired column and values
new_df = pd.DataFrame()
# new_df['keyword'] = keywords_col
new_df['url'] = url_col
new_df['result_count'] = result_counts
new_df.apply(lambda col: col.drop_duplicates().reset_index(drop=True))

# write the output dataframe to an Excel file
new_df.to_excel('output_file'+str(i)+'.xlsx', index=False)
