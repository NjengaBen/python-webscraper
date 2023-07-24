import requests
from bs4 import BeautifulSoup
req = requests.get("https://aitoptools.com?")

soup = BeautifulSoup(req.content, 'html.parser')
responses = soup.find('div', class_='jet-listing')

records =[]

for response in responses:
    getTitles = response.find_all('h2', class_='elementor-heading-title elementor-size-default')
    getRatings = response.find_all('div', class_='elementor-star-rating')    
    getReviews = response.find_all('div', class_='elementor-star-rating__title')
    getTags = response.find_all('a', class_='jet-listing-dynamic-terms__link')
    getImgSrc = response.find_all('div', class_='elementor-widget-image')
    getData = response.find_all('div', class_="jet-listing-dynamic-field__content")
    

    for titles, ratings, reviews, tags, imgsrcs, data in zip(getTitles, getRatings, getReviews, getTags, getImgSrc, getData):
        title = titles.get_text().strip()
        review = reviews.get_text().strip("()")
        rating = ratings.span.get_text()
        tag = tags.get_text().strip()
        imgSrc = imgsrcs.img['data-src']
        dt = data.get_text().strip()
        
    
        record = {
            "Title":title,
            "Reviews": review,
            "Rating": rating,
            "Tags": tag,
            "ImgUrl": imgSrc,
            "Data":{
                "Price": dt,
                "unknown": dt,
                "Category": dt,
                "Description": dt,
            }
        }

        records.append(record)

for record in records:
    print(record)



# print(responses)

