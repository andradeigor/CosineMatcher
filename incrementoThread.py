#/* Disciplina: Programacao Concorrente */
#/* Prof.: Silvana Rossetto */
#/* Módulo 4 - Laboratório: 7 */
#/* Codigo: exemplo de uso de variavel compartilhada em Python */ 

from threading import Thread
from threading import Lock

#classe variavel compartilhada
class Variavel():
    def __init__(self):
        self.valor = 0
        self.lock = Lock()

    def incrementa(self):
        self.lock.acquire()
        self.valor += 1
        self.lock.release()

    def getValor(self):
        return self.valor

#classe da thread
class IncrementaThread(Thread):
    def __init__(self, id, variavel):
        super().__init__()
        self.threadid = id
        self.variavel = variavel

    def run(self):
        print("Thread", self.threadid)
        for _ in range(100000):
            self.variavel.incrementa()

#fluxo principal
if __name__ == '__main__':
    #cria variavel compartilhada
    var = Variavel()
    #cria e dispara as threads
    threads = [IncrementaThread(i, var) for i in range(2)]
    for thread in threads:
        thread.start()
    #aguarda as threads terminarem
    for thread in threads:
        thread.join()
    #exibe o valor da variavel
    print("variavel = ", var.getValor())        
