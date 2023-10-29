#/* Disciplina: Programacao Concorrente */
#/* Prof.: Silvana Rossetto */
#/* Módulo 4 - Laboratório: 7 */
#/* Codigo: mostra que processos filhos nao compartilham variaveis */ 

from multiprocessing import Process

#classe variavel compartilhada
class Variavel():
    def __init__(self):
        self.valor = 0

    def incrementa(self):
        self.valor += 1

    def getValor(self):
        return self.valor

#classe do processo
class Incrementa(Process):
    def __init__(self, id, variavel):
        super().__init__()
        self.procid = id
        self.variavel = variavel

    def run(self):
        print("Processo", self.procid)
        for _ in range(100000):
            self.variavel.incrementa()
        print('Processo {0}: variavel {1}'.format(self.procid, var.getValor()))

#fluxo principal
if __name__ == '__main__':
    var = Variavel()
    var.incrementa()
    print("Main: variavel = ", var.getValor())        
    #cria e dispara os processos
    processos = [Incrementa(i, var) for i in range(2)]
    for p in processos:
        p.start()
    #aguarda os processos filhos terminarem
    for p in processos:
        p.join()
    #exibe o valor da variavel
    print("Main: variavel = ", var.getValor())        
