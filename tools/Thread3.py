from threading import Thread
from scrapper.GetH1AndDescription import GetH1AndDescription
import queue


class Thread3(Thread):
    def __init__(self, url_queue):
        super().__init__()
        self.url_queue = url_queue

    def run(self):
        while True:
            try:
                url = self.url_queue.get_nowait()
                print("Traitement de l'URL :", url)

                get_h1_and_description = GetH1AndDescription(url)
                get_h1_and_description.start()
                get_h1_and_description.join()
            except queue.Empty:
                # Si la file d'attente est vide, sortir de la boucle infinie
                break
