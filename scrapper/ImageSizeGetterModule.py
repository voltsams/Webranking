import threading
import requests
from bs4 import BeautifulSoup as bs

class ImageSizeGetter(threading.Thread):
    # load the webpage content
    r = requests.get('https://www.google.com/')

    # convert to beautiful soup
    soup = bs(r.content)

    # printing our web page
    print(soup.prettify())

    # getting image URL link:
    images = soup.select('div img')

    images_url = images[0]['src']

    images_url

    # downloading the image:

    img_data = requests.get(images_url).content

    with open('netflix.jpg', 'wb') as handler:

           handler.write(img_data)

