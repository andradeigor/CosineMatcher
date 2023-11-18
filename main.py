from TemplateMatching import TemplateMaching
from ParallelTemplateMatching import ParallelTemplateMaching
import numpy as np
import sys
import time


def main():
    try:
        if (len(sys.argv) < 3):
            print(
                f"A chamada ao arquivo deve ser: python3 {sys.argv[0]} <caminho da imagem> <caminho do template> (opcicionalente, nº de cpus)")
            return
        if (len(sys.argv) >= 3):
            tp = ParallelTemplateMaching(sys.argv[1],
                                         sys.argv[2], sys.argv[3])
        else:
            tp = ParallelTemplateMaching(sys.argv[1],
                                         sys.argv[2])
    except:
        print(
            f"Ocorreu um erro durante a leitura dos arquivos {sys.argv[1]} e {sys.argv[2]}")
        return
    inicio = time.time()
    resultado = tp.templateMatching()
    resultadoFiltrado = np.where(resultado >= 0.8)
    tp.drawRectangles(resultadoFiltrado)
    fim = time.time()
    tp.print()
    print(f'Rodou por {(fim-inicio)//60} minutos e {(fim-inicio)%60} segundos')


if __name__ == "__main__":
    main()
