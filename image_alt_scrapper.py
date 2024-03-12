import img
import requests
from bs4 import BeautifulSoup


# Function to check if an image has an "alt" attribute
def has_alt_attribute(img):
    return "alt" in img.attrs
# Get the URL from the user
url = input("Enter the URL of the page to check: ")
# Make a request to the URL and get the HTML content
response = requests.get(url)
html_content = response.content
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
# Find all the image tags on the page
images = soup.find_all('img')
# Check if each image has an "alt" attribute or not
for image in images:
    if has_alt_attribute(image):
        print(f"The image with source '{image['src']}' has an 'alt' attribute.")
    else:
        print(f"The image with source '{image['src']}' does not have an 'alt' attribute.")
