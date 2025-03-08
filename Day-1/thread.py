import threading

def count():
    for i in range(10000000):
        pass

thread1 = threading.Thread(target=count)
thread2 = threading.Thread(target=count)

thread1.start()
thread2.start()
print("wating..")
thread1.join()
thread2.join()
print("Done")
