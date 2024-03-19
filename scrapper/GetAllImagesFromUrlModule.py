import os
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse
#TODO secure ?
def download_image(url, directory):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            filename = os.path.basename(urlparse(url).path)
            with open(os.path.join(directory, filename), 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def download_all_images(url, directory):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            img_tags = soup.find_all('img')
            img_urls = [urljoin(url, img['src']) for img in img_tags if 'src' in img.attrs]
            with ThreadPoolExecutor(max_workers=5) as executor:  # Adjust max_workers as needed
                executor.map(lambda img_url: download_image(img_url, directory), img_urls)
    except Exception as e:
        print(f"Error fetching images from {url}: {e}")

if __name__ == "__main__":
    url = input("Enter the URL: ")
    directory = input("Enter the directory to save images: ")

    if not os.path.exists(directory):
        os.makedirs(directory)

    download_all_images(url, directory)