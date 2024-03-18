from scrapper.InternalLinksScrapper import InternalLinksScrapper


class Thread1:
    @staticmethod
    def run():
        url = input("Enter the URL to analyze: ")
        scrapper = InternalLinksScrapper()
        scrapper.extract_internal_links(url)
        print("Internal Links:")
        # Recursive call to treat each page
        for link in scrapper.links:
            scrapper.extract_internal_links(url)
            print(link)

if __name__ == "__main__":
    Thread1.run()
