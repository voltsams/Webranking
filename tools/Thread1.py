import threading
import scrapper.InternalLinksQueueModule as queueModule
import GlobalsModule
import entities.PageModule as PageModule

from scrapper.CheckPageSpeed import CheckPageSpeed
from scrapper.InternalLinksScrapper import InternalLinksScrapper

InternalPagesDict = dict()


class Thread1(threading.Thread):
    def run(self):
        GlobalsModule.Globals.prompt_user_to_enter_url(cls=GlobalsModule.Globals)
        scrapper = InternalLinksScrapper()
        scrapper.extract_internal_links(GlobalsModule.Globals.siteBaseUrl)
        print("Internal Links:")
        # Recursive call to treat each page
        try:
            for link in scrapper.links:
                scrapper.extract_internal_links(GlobalsModule.Globals.siteBaseUrl)
                queueModule.internal_links_queue.put(link)

                self.consume_queue()
        except Exception as e:
            print(f"Erreur rencontrée : {Exception}")

            # https://www.cleor.com/

    def consume_queue(self):
        current_link = queueModule.internal_links_queue.get()
        print("je consomme , ", current_link)
        current_page = PageModule.Page(current_link)

        # TODO MOVE DECLARATION OF SINGLETON

        GlobalsModule.singleton_list.add_page(current_link, current_page)
        print("test vsa ", GlobalsModule.singleton_list.__str__())

        # TODO le receveur doit dire au déclencheur de l'evvenement qu'il a terminé le traitement
        # TODO Créer variable partagée Dictionaire de page
        # TODO Créer UI avec chargement multithread des valeurs
        thread_check_page_speed = CheckPageSpeed(current_link)
        thread_check_page_speed.start()
        thread_check_page_speed.join()

        #print(
            #f"CURRENT TIME LOADING PAGE {GlobalsModule.singleton_list.list_of_web_pages[current_link].loadingTime:.3f} "
            #f"|||META {GlobalsModule.singleton_list.list_of_web_pages[current_link].hasMetaDescription} \n")
        # checkH1.hasH1
        print(current_link)
