import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


class InternalLinksScrapper:
    def __init__(self, url):
            self.url = url

    def get_links_with_html(self):
        try:
            # requête HTTP GET pour récupérer le contenu de la page
            response = requests.get(self.url)

            # si la requête a réussi (code de statut 200)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                links = soup.find_all('a')
                # stockage des urls dans une liste
                links_list = []

                for link in links:
                    href = link.get('href')
                    if href:
                        # si l'url du lien contient "html"
                        parsed_link = urlparse(href)
                        if "html" in parsed_link.path:
                            links_list.append(href)

                return links_list
            else:
                print("Request failed with status code :", response.status_code)
                return None
        except Exception as e:
            print("Error :", str(e))
            return None


url = "https://www.cleor.com/"
link_scrapper = InternalLinksScrapper(url)
links = link_scrapper.get_links_with_html()
if links:
    print(f"Links found on the page : {url}")
    for link in links:
        print(link)
else:
    print(f"No links found for the url : {url}")
