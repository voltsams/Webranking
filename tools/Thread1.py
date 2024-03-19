from scrapper.CheckPageSpeed import CheckPageSpeed
from scrapper.InternalLinksScrapper import InternalLinksScrapper
import scrapper.InternalLinksQueueModule as queueModule
import scrapper.check_ssl as tlsCheck
import GlobalsModule
import entities.PageModule as PageModule
import scrapper.GetH1AndDescription as hasH1Check
import entities.SingletonPatternDictionaryOfPagesModule as Pages

InternalPagesDict = dict()
class Thread1:
    @staticmethod
    def run(cls):
        GlobalsModule.Globals.prompt_user_to_enter_url(cls=GlobalsModule.Globals)
        scrapper = InternalLinksScrapper()
        scrapper.extract_internal_links(GlobalsModule.Globals.siteBaseUrl)
        print("Internal Links:")
        # Recursive call to treat each page
        for link in scrapper.links:
            scrapper.extract_internal_links(GlobalsModule.Globals.siteBaseUrl)
            queueModule.internal_links_queue.put(link)

            cls.consume_queue()

            # https://www.cleor.com/

    @staticmethod
    def consume_queue():
        current_link = queueModule.internal_links_queue.get()
        print("je consomme , ",current_link)
        current_page = PageModule.Page(current_link)

        # TODO MOVE DECLARATION OF SINGLETON

        GlobalsModule.singleton_list.add_page(current_link, current_page)
        print("test vsa ",GlobalsModule.singleton_list.__str__())

        # current_page.hasTls = tlsCheck.check_tls(current_link)

        # TODO le receveur doit dire au déclencheur de l'evvenement qu'il a terminé le traitement
        # TODO Créer variable partagée Dictionaire de page
        # TODO Créer UI avec chargement multithread des valeurs
        thread_check_page_speed = CheckPageSpeed(current_link)
        thread_check_page_speed.start()
        thread_check_page_speed.join()
        #thread_check_page_speed.eventPageLoaded.wait()

        #if current_link in GlobalsModule.singleton_list.list_of_web_pages:
         #   GlobalsModule.singleton_list.list_of_web_pages[current_link].loadingTime = thread_check_page_speed.page_load_time

        # checkH1 = hasH1Check.GetH1AndDescription(current_link)
        # checkH1.start()
        # checkH1.join()
        # current_page.hasH1 = checkH1.hasH1
        # current_page.hasMetaDescription = checkH1.hasMetaDescription
        print(
            f"CURRENT TIME LOADING PAGE {GlobalsModule.singleton_list.list_of_web_pages[current_link].loadingTime:.3f} ||| META {GlobalsModule.singleton_list.list_of_web_pages[current_link].hasMetaDescription} ||| H1")
        # checkH1.hasH1
        print(current_link)


#if __name__ == "__main__":
    # Thread1.run(cls=Thread1)
    # thread1 = Thread1()
    # thread1.run()
