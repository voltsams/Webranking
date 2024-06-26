import threading

import requests
from bs4 import BeautifulSoup


class GetH1AndDescription(threading.Thread):
    def __init__(self, url: str):
        super().__init__()
        self.url = url
        self.hasH1 = False
        self.hasMetaDescription = False

    def run(self):
        print("URL :", self.url)
        # Make a request to the URL
        response = requests.get(self.url)

        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find the title h1 tag and get its content
        h1_title = soup.find_all('h1')
        for h1_title in h1_title:
            print('balise h1 trouvée : ' + h1_title.getText())
            self.hasH1 = True

        # Find the meta description tag and get its content
        meta_description = soup.find('meta', {'name': 'description'})
        if meta_description:
            print('Meta description found: ' + meta_description['content'])
            self.hasMetaDescription = True
        else:
            print('No meta description found')
            self.hasMetaDescription = False
