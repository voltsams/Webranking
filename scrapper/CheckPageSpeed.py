import requests
import time
import threading
import entities.PageModule
from entities import PageModule
import GlobalsModule


class CheckPageSpeed(threading.Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url
    page_load_time = 0.0
    # create an instance of an event
    eventPageLoaded = threading.Event()

    def run(self):
        # TODO Give a list and implements the work on the list

        # Send a GET request to the given URL and record the start time
        start_time = time.time()
        response = requests.get(self.url)
        # Record the end time and calculate the page load time
        end_time = time.time()
        self.page_load_time = end_time - start_time
        self.eventPageLoaded.set()
        # Print the page load time in seconds
        print(f"Page load time: {self.page_load_time:.2f} seconds")
        GlobalsModule.singleton_list.list_of_web_pages[self.url].loadingTime = self.page_load_time
        print("Temps d'exécution du CPU : ", time.process_time())
        print("Execution dans le thread CheckPageSpeed")
