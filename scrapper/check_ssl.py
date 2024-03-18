import requests


def check_tls(url):
    response = requests.get(url)
    if response.status_code != 200:
        # "Error: Could not access the website"
        return False
    #TODO X'''''''''''D
    if response.url.startswith('https://'):
        # "The website has a valid SSL certificate"
        return True
    else:
        #"The website does not have a valid SSL certificate"
        return False


# Usage
#url = input("Enter the website URL: ")
#result = check_tls(url)
#print(result)
