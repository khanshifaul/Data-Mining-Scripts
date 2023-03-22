import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
import random
import urllib.parse

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
            keyword = urllib.parse.quote(keyword)
            keywords.append(keyword)

print(keywords)

print(len(keywords))


def scrape(keyword):
    i = 0
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

    # send a GET request to the URL with the headers
    response = requests.get(url, headers=headers)
    # parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'lxml')
    # extract the search result count from the HTML using soup.find()
    result_count_elem = soup.find('div', {'id': 'result-stats'})

    if result_count_elem is not None:
        result_count_text = result_count_elem.text

        # extract only numbers from text
        result_count = int(''.join(filter(str.isdigit, result_count_text)))
        return keyword, url, result_count


# loop through each search query and scrape the search result count using multithreading
result_counts = []
urls = []
with ThreadPoolExecutor() as executor:
    futures = [executor.submit(scrape, kw) for kw in keywords]
    for f in tqdm(as_completed(futures), total=len(keywords)):
        res = f.result()
        if res is not None:
            kw, url, result = res
            urls.append(url)
            result_counts.append(result)
            print(str(i)+ ' ' + url + ' ' + result_count)

# create a new DataFrame with the desired column and values
new_df = pd.DataFrame()

new_df['keyword'] = keywords
new_df['url'] = pd.Series(urls)
# new_df['result_count'] = result_counts

# write the output dataframe to an Excel file
new_df.to_excel('output_file.xlsx', index=False)
