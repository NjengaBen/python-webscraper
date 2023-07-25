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
    for links in tool.find_all('h2', class_="elementor-heading-title elementor-size-default"):
        link = links.text.strip()       
        toollink.append(baseUrl+link)
print(toollink)
    

