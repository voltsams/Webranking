import queue
import threading
from scrapper.ImageAltScrapper import ImageAltScrapper


class Thread2(threading.Thread):
    def __init__(self, links_queue):
        super().__init__()
        self.links_queue = links_queue

    def run(self):
        while True:
            try:
                # Récupérer un lien de la file d'attente
                current_link = self.links_queue.get_nowait()
                print(f"Traitement du lien : {current_link}")
                # Créez une instance de ImageAltScrapper pour chaque lien et exécutez-la
                image_scrapper = ImageAltScrapper(self.links_queue.get_nowait())
                image_scrapper.start()
                image_scrapper.join()
            except queue.Empty:
                # Si la file d'attente est vide, sortir de la boucle infinie
                break
        print("Thread2 finished")
