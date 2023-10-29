#/* Disciplina: Programacao Concorrente */
#/* Prof.: Silvana Rossetto */
#/* Módulo 4 - Laboratório: 7 */
#/* Codigo: "Hello World" usando threads em Python */

#https://docs.python.org/3/library/concurrency.html

from threading import Thread

#classe da thread
class HelloWorldThread(Thread):
    def __init__(self, id):
        super().__init__()
        self.threadid = id

    def run(self):
        print("Ola Mundo da thread", self.threadid)

#fluxo principal
if __name__ == '__main__':
    threads = [HelloWorldThread(i) for i in range(10)]
    for thread in threads:
        thread.start()
