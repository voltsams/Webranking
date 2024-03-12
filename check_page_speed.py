import requests
import time
import threading


def check_page_speed():
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

    # Création d'un thread
    my_thread = threading.Thread(target=check_page_speed)
    my_thread.start()


check_page_speed()
