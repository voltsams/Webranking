# Singleton Pattern needed to access page objects in thread safe way
# The key is the URL of the Page the value is the Page instance
class SingletonListOfWebPages:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.list_of_web_pages = {}

            # Example of adding a page
            # self.add_page("https://example.com", Page("https://example.com"))

            self._initialized = True

    def add_page(self, url, page_instance):
        self.list_of_web_pages[url] = page_instance


# Example usage:
# Creating pages
# page1 = Page("https://example1.com")

# Adding pages to singleton list
# singleton_list = SingletonListOfWebPages()
# singleton_list.add_page("https://example1.com", page1)

# Retrieving pages
# print(singleton_list.ListOfWebPages["https://example1.com"].url)
