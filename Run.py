import tools.Thread1 as Thread1
import tools.Thread2 as Thread2

thread1 = Thread1.Thread1()
thread2 = Thread2.Thread2()

thread1.run()
thread1.join()
thread2.run()
