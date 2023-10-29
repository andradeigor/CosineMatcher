#extraido de: "Python 3 Object-oriented Programming" (Cap 13), Dusty Phillips, 2nd edition, 2015

from threading import Thread
from multiprocessing import cpu_count
import time
import os

class MuchCPU(Thread):
    def run(self):
        print(os.getpid())
        for i in range(200000000):
            pass

if __name__ == '__main__':
    threads = [MuchCPU() for f in range(cpu_count())]
    start = time.time()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('work took {} seconds'.format(time.time() - start))
