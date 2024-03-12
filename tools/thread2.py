import threading


class Thread2(threading.Thread):
    def run(self):
        print("Exécution du thread 2")


my_thread = Thread2()
my_thread.start()
