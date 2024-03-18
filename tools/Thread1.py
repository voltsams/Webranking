from scrapper.InternalLinksScrapper import InternalLinksScrapper


class Thread1:
    @staticmethod
    def run():
        url = input("Enter the URL to analyze: ")
        scrapper = InternalLinksScrapper()
        scrapper.extract_internal_links(url)
        print("Internal Links:")
        for link in scrapper.links:
            print(link)


if __name__ == "__main__":
    Thread1.run()
