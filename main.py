from ParallelTemplateMatching import ParallelTemplateMaching
import numpy as np
import sys
import time


def main():
    inicio = time.time()
    try:
        if (len(sys.argv) < 3):
            print(
                f"A chamada ao arquivo deve ser: python3 {sys.argv[0]} <caminho da imagem> <caminho do template> (opcicionalente, nº de cpus)")
            return
        if (len(sys.argv) > 3):
            tp = ParallelTemplateMaching(sys.argv[1],
                                         sys.argv[2], int(sys.argv[3]))
        else:
            tp = ParallelTemplateMaching(sys.argv[1],
                                         sys.argv[2])
    except Exception as e:
        print(
            f"Ocorreu um erro durante a leitura dos arquivos {sys.argv[1]} e {sys.argv[2]}")
        print(e)
        return
    fimCarregamento = time.time()
    print(f'demorou {fimCarregamento-inicio} para carregar as imagens.')
    resultado = tp.templateMatching()
    fimMathing = time.time()
    resultadoFiltrado = np.where(resultado >= 0.8)
    tp.drawRectangles(resultadoFiltrado)
    fimDesenho = time.time()
    tp.print()

    print(
        f'Rodou por {(fimMathing-fimCarregamento)//60} minutos e {(fimMathing-fimCarregamento)%60} segundos')
    print(
        f'O tempo total sequencial foi {(fimCarregamento-inicio) + (fimDesenho-fimMathing)}')


if __name__ == "__main__":
    main()
