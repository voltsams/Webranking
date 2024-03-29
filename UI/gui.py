import queue
import tkinter as tk
from GlobalsModule import Globals
from tools.Thread1 import Thread1
from tools.Thread2 import Thread2
from tools.Thread3 import Thread3


class URLInputGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("URL Input")

        # Récupère la taille de l'écran
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # Définit la taille de la fenêtre comme la taille de l'écran
        self.master.geometry(f"{screen_width}x{screen_height}")

        self.url_label = tk.Label(master, text="Enter the URL to analyze:")
        self.url_label.pack()

        self.url_entry = tk.Entry(master)
        self.url_entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.submit_url)
        self.submit_button.pack()

    def submit_url(self):
        url = self.url_entry.get()
        Globals.prompt_user_to_enter_url(url)
        print("URL submitted:", url)

        # Lancer le traitement des threads une fois que l'URL est récupérée
        start_thread_processing()


def start_thread_processing():
    # Crée une instance de queue pour stocker les liens
    links_queue = queue.Queue()

    # Récupère l'URL à analyser
    url = Globals.siteBaseUrl

    # Créer les instances des Thread avec la queue des liens en paramètre
    thread1 = Thread1(links_queue)
    thread2 = Thread2(links_queue)
    thread3 = Thread3(links_queue)

    # -------- Ordre de gestion des Thread ----------
    thread1.start()
    thread1.join()
    print(f" links_queue*************** {links_queue.qsize()}")

    # Démarre le Thread2
    thread2.start()

    # Démarre le Thread3
    thread3.start()

    # Attends la fin des Threads2 et Thread3
    thread2.join()
    thread3.join()

    print("Tous les threads ont terminé leur travail.")
