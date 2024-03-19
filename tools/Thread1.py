from scrapper.CheckPageSpeed import CheckPageSpeed
from scrapper.InternalLinksScrapper import InternalLinksScrapper
import scrapper.InternalLinksQueueModule as queueModule
import scrapper.check_ssl as tlsCheck
import GlobalsModule
import entities.PageModule as PageModule
import scrapper.GetH1AndDescription as hasH1Check
import entities.SingletonPatternDictionaryOfPagesModule as Pages


class Thread1:

    def run(self):
        GlobalsModule.Globals.prompt_user_to_enter_url(cls=GlobalsModule.Globals)
        scrapper = InternalLinksScrapper()
        scrapper.extract_internal_links(GlobalsModule.Globals.siteBaseUrl)
        print("Internal Links:")
        # Recursive call to treat each page
        for link in scrapper.links:
            scrapper.extract_internal_links(GlobalsModule.Globals.siteBaseUrl)
            queueModule.internal_links_queue.put(link)

            self.consume_queue()
            #https://www.cleor.com/

    def consume_queue(self):
        current_link = queueModule.internal_links_queue.get()
        current_page = PageModule.Page(current_link)

        # TODO MOVE DECLARATION OF SINGLETON
        singleton_list = Pages.SingletonListOfWebPages()
        singleton_list.add_page(current_link, current_page)

        current_page.hasTls = tlsCheck.check_tls(current_link)
#TODO le receuveur doit dire au déclencheur de l'evvenement qu'il a terminé le traitement
#TODO Créer variable partagée DIctionaire de page
#TODO Créer UI avec chargement multithread des valeurs
        thread_check_page_speed = CheckPageSpeed(current_link)
        thread_check_page_speed.start()
        thread_check_page_speed.eventPageLoaded.wait()
        singleton_list.list_of_web_pages[current_link] = thread_check_page_speed.page_load_time

        #checkH1 = hasH1Check.GetH1AndDescription(current_link)
        #checkH1.start()
        #checkH1.join()
        #current_page.hasH1 = checkH1.hasH1
        #current_page.hasMetaDescription = checkH1.hasMetaDescription
        print(f"CURRENT TIME LOADING PAGE {current_page.loadingTime:.3f} ||| META {current_page.hasMetaDescription} ||| H1")
        #checkH1.hasH1
        print(current_link)


if __name__ == "__main__":
    #Thread1.run(cls=Thread1)
    thread1 = Thread1()
    thread1.run()
