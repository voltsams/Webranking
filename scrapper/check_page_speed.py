import requests
import time
import threading


class CheckPageSpeed(threading.Thread):
    def run(self):
        # Prompt user to enter the URL to check
        url = input("Enter the URL to check page speed: ")
        # Send a GET request to the given URL and record the start time
        start_time = time.time()
        response = requests.get(url)
        # Record the end time and calculate the page load time
        end_time = time.time()
        page_load_time = end_time - start_time
        # Print the page load time in seconds
        print(f"Page load time: {page_load_time:.2f} seconds")
        print("Execution dans un thread")
