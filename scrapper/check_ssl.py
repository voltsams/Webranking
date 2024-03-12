import requests


def check_ssl(url):
    response = requests.get(url)
    if response.status_code != 200:
        return "Error: Could not access the website"
    if response.url.startswith('https://'):
        return "The website has a valid SSL certificate"
    else:
        return "The website does not have a valid SSL certificate"


# Usage
url = input("Enter the website URL: ")
result = check_ssl(url)
print(result)
