import requests
from bs4 import BeautifulSoup

baseUrl = "https://aitoptools.com/"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

r = requests.get("https://aitoptools.com/")
soup = BeautifulSoup(r.content, 'html.parser')

toollist = soup.find_all('div', class_="elementor elementor-43")

toollink = []

for tool in toollist:
    for link in tool.find_all('a', href=True):
        toollink.append(link['href'])
    print(link['href'])
    

