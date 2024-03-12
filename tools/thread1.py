import threading
from scrapper.CheckPageSpeed import CheckPageSpeed


class Thread1(threading.Thread):

    threadCheckPageSpeed = CheckPageSpeed()
    threadCheckPageSpeed.start()
