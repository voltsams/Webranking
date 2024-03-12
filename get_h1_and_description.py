import requests
from bs4 import BeautifulSoup


def get_h1_and_description():
    url = input("Enter the URL of the web page: ")

    # Make a request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the title h1 tag and get its content
    h1_title = soup.find_all('h1')
    for h1_title in h1_title:
        print('balise h1 trouvée : ' + h1_title.getText())

    # Find the meta description tag and get its content
    meta_description = soup.find('meta', {'name': 'description'})
    if meta_description:
        print('Meta description found: ' + meta_description['content'])
    else:
        print('No meta description found')


get_h1_and_description()
