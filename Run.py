from tools.Thread1 import Thread1
from tools.Thread2 import Thread2
import queue


def main():
    # Créer une instance de queue pour stocker les liens
    links_queue = queue.Queue()

    # Créer une instance de Thread1 avec la queue des liens en paramètre
    thread1 = Thread1(links_queue)

    # Créer une instance de Thread2 avec la queue des liens en paramètre
    thread2 = Thread2(links_queue)

    # Démarre le Thread1
    thread1.start()
    thread1.join()
    print(f" links_queue*************** {links_queue.qsize()}")

    # Démarre le Thread2
    thread2.start()

    # Termine le Thread2
    thread2.join()


if __name__ == "__main__":
    main()
