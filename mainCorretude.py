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

        tpSequencial = ParallelTemplateMaching(sys.argv[1],
                                               sys.argv[2], 1)
        tpParalelo2 = ParallelTemplateMaching(sys.argv[1],
                                              sys.argv[2], 2)
        tpParalelo4 = ParallelTemplateMaching(sys.argv[1],
                                              sys.argv[2], 4)
        tpParalelo8 = ParallelTemplateMaching(sys.argv[1],
                                              sys.argv[2], 8)
    except Exception as e:
        print(
            f"Ocorreu um erro durante a leitura dos arquivos {sys.argv[1]} e {sys.argv[2]}")
        print(e)
        return

    resultadoSequencial = tpSequencial.templateMatching()
    resultadoParalelo2 = tpParalelo2.templateMatching()
    resultadoParalelo4 = tpParalelo4.templateMatching()
    resultadoParalelo8 = tpParalelo8.templateMatching()
    error2 = np.linalg.norm(resultadoSequencial - resultadoParalelo2)
    error4 = np.linalg.norm(resultadoSequencial - resultadoParalelo4)
    error8 = np.linalg.norm(resultadoSequencial - resultadoParalelo8)
    print(f'O erro obtido foi: {error2}, {error4}, {error8}')


if __name__ == "__main__":
    main()
