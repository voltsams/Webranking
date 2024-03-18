class Globals:
    siteBaseUrl = ""


    @staticmethod
    def prompt_user_to_enter_url(cls):
        cls.siteBaseUrl = input("Enter the URL to analyze : ")
