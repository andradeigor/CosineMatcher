#extraido de: "Python 3 Object-oriented Programming" (Cap 13), Dusty Phillips, 2nd edition, 2015

from multiprocessing import Process, cpu_count
import time
import os

class MuchCPU(Process):
    def run(self):
        print(os.getpid())
        for i in range(200000000):
            pass
#Pay special attention to the if __name__ == '__main__': guard around the module
#level code that prevents it to run if the module is being imported, rather than run
#as a program. This is good practice in general, but when using multiprocessing on
#some operating systems, it is essential. Behind the scenes, multiprocessing may have
#to import the module inside the new process in order to execute the run() method.
#If we allowed the entire module to execute at that point, it would start creating new
#processes recursively until the operating system ran out of resources.
if __name__ == '__main__':
    procs = [MuchCPU() for f in range(cpu_count())]
    t = time.time()
    for p in procs:
        p.start()
        p.run()
    for p in procs:
        p.join()
    print('work took {} seconds'.format(time.time() - t))
    
