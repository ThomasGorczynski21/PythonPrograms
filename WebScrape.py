import sys
print(sys.path)
sys.path.append('/Users/tom_8/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0/LocalCache/local-packages/Python311/site-packages')


## this script is meant to search google, but unsure if they allow it.

import requests
from bs4 import BeautifulSoup

def google_search(keyword):
    url = f'https://www.duckduckgo.com/search?q={keyword}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.find_all('div', class_='tF2Cxc')

        for result in search_results:
            title_element = result.find('h3', class_='LC20lb DKV0Md')
            link_element = result.find('a')
            
            if title_element and link_element:
                title = title_element.text
                link = link_element['href']
                print(f'Title: {title}\nURL: {link}\n')
    else:
        print(f'Request failed with status code {response.status_code}')

if __name__ == '__main__':
    keyword = input('Enter the keyword to search: ')
    google_search(keyword)
