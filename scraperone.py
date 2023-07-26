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
toollink1=[]


for tool in toollist:
    for link in tool.find_all('a', href=True):               
        toollink.append(link['href'])   
    toollink1.append(link['href'])

for url in toollink1:
    r=requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    name = soup.find('h2', class_="elementor-heading-title elementor-size-default").text.strip("About ")
    reviews = soup.find('div', class_='elementor-star-rating__title').text.strip("()")
    ratings = soup.find('div', class_='elementor-star-rating').span.text.strip()

    tags = soup.find_all('a', class_='jet-listing-dynamic-terms__link')
    taglist=[]
    for tag in tags:
        tagname=tag.text.strip()
        taglist.append(tagname)

    imgSrc = soup.find('div', class_='elementor-widget-image').img['data-src']
    desc = soup.find_all('p')[2].text.strip()
   
    misc = soup.find_all('div', class_="jet-listing-dynamic-field__content")
    datalist=[]
    for infoName in misc:
        info = infoName.text.strip()
        datalist.append(info)
   
    misc_key = ["Data1", "Data2", "Data3", "Data4", "Data5"]
    misc_dict = {key:datalist[i] for i, key in enumerate(misc_key)}
    data = {
        "Name": name,
        "Website": url,
        "Review": reviews,
        "Rating": ratings,
        "Tags": taglist,
        "ImgSrc": imgSrc,
        "Desc":desc,
        "Misc":misc_dict
    }

    print(data)
