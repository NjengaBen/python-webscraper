import requests
from bs4 import BeautifulSoup
# req = requests.get("https://aitoptools.com/tool/creasquare/")
req = requests.get('https://aitoptools.com/')

records = []

if req.status_code == 200:
    soup = BeautifulSoup(req.content, 'html.parser')
    h2_elements = soup.find_all('div', class_="jet-listing")    

    # for h2_element in h2_elements:
    #     print(h2_element.get_text())

    
    for response in h2_elements:
        element = response.find_all('div', class_='jet-listing-dynamic-field__content')
        # listingArr = []        
        print(element)
                   
        

        # for elem in element:            
        #     title = elem.get_text().strip() 
            # print(title)
            
        #     record = {
        #         "Element": title
        #     }
        

        #     records.append(record)            
            
        # print(records)      

# for record in records:
#     print(record)

else:
    print("Failed to retrieve the page. Status code: ", req.status_code)
