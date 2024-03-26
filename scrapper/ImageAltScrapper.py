import threading
import requests
from bs4 import BeautifulSoup


class ImageAltScrapper(threading.Thread):
    def __init__(self, links_queue):
        super().__init__()
        self.links_queue = links_queue

    def run(self):
        # Faites une requête à l'URL
        response = requests.get(self.links_queue)
        # Analysez le contenu HTML de la page en utilisant BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        # Trouvez toutes les balises d'image sur la page
        images = soup.find_all('img')
        # Vérifiez si chaque image a un attribut "alt" ou non
        for image in images:
            if 'alt' in image.attrs:
                print(f"L'image avec la source '{image['src']}' a un attribut 'alt'.")
            else:
                print(f"L'image avec la source '{image['src']}' n'a pas d'attribut 'alt'.")
