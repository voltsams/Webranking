import requests
import string
from bs4 import BeautifulSoup
from entities.Word import Word


class WordFrequency:
    def get_Word_Frequency(self,url):
        # url = input("Enter the URL of the web page: ")

        response = requests.get(url)
        html_content = response.content

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        text = soup.get_text()

        words = self.get_words(text)
        # print(words)

        word_list = []
        # check word frequency
        for word in words:
            word_list.append(Word(word, words.count(word), 100 / len(words) * words.count(word)))

        return word_list


    def get_words(self,text):
        translating = str.maketrans('', '', string.punctuation)
        text = text.translate(translating)

        text = text.replace("\n", "")
        text = text.replace("\r", " ")

        only_words = text.split(" ")
        only_words = [x for x in only_words if x != '']

        return only_words