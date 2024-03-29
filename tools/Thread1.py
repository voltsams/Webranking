import threading
from UI.gui import Globals
from scrapper.InternalLinksScrapper import InternalLinksScrapper


class Thread1(threading.Thread):
    def __init__(self, links_queue):
        super().__init__()
        self.links_queue = links_queue

    def run(self):
        # Utilisation de l'url récupéré depuis le gui
        url = Globals.siteBaseUrl
        if not url:
            print("URL non renseigné :( ")
            return

        scrapper = InternalLinksScrapper()
        scrapper.extract_internal_links(url)
        print("Internal Links:")
        # Recursive call to treat each page
        try:
            # Définir un ensemble pour stocker les liens déjà traités
            processed_links = set()

            # Extraction des liens internes une seule fois
            scrapper.extract_internal_links(url)
            for link in scrapper.links:
                # Vérifier si le lien a déjà été traité
                if link not in processed_links:
                    # Ajouter le lien à l'ensemble des liens traités
                    processed_links.add(link)
                    # Mettre le lien dans la file d'attente
                    self.links_queue.put(link)

            # Pas besoin de consommer la file d'attente ici

        except Exception as e:
            print(f"Erreur rencontrée : {e}")
