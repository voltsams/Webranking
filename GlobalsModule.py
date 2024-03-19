import threading
import entities.PageModule as PageModule
from entities.SingletonPatternDictionaryOfPagesModule import SingletonListOfWebPages

singleton_list = SingletonListOfWebPages.__new__(cls=SingletonListOfWebPages)


class Globals:
    siteBaseUrl = ""
    #dic_of_pages = dict()

    @staticmethod
    def prompt_user_to_enter_url(cls):
        cls.siteBaseUrl = input("Enter the URL to analyze : ")
        #cls.dic_of_pages = dict()


class GlobalPages:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.pages = dict()
        return cls._instance

    def add_page(self, url: str, page_instance: PageModule.Page):
        with self._lock:
            self.pages[url] = page_instance

    def get_page(self, url: str):
        with self._lock:
            return self.pages[url]

# Example usage:
# Creating pages
# page1 = Page("https://example1.com")


# Adding pages to global variable
# global_pages = GlobalPages()
# global_pages.add_page("https://example1.com", page1)


# Retrieving pages
# print(global_pages.get_page("https://example1.com").url)
