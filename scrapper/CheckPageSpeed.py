import requests
import time
import threading


class CheckPageSpeed(threading.Thread):
    def run(self):
        # TODO Give a list and implements the work on the list

        # Send a GET request to the given URL and record the start time
        start_time = time.time()
        response = requests.get()
        # Record the end time and calculate the page load time
        end_time = time.time()
        page_load_time = end_time - start_time
        # Print the page load time in seconds
        print(f"Page load time: {page_load_time:.2f} seconds")
        print("Temps d'exécution du CPU : ", time.process_time())
        print("Execution dans un thread")
