from TemplateMatching import TemplateMaching
from ParallelTemplateMatching import ParallelTemplateMaching
import time


def main():
    tp = ParallelTemplateMaching("./images/btgimage.jpg",
                                 "./templates/btgtemplate.jpg")
    inicio = time.time()
    tp.templateMatching()
    fim = time.time()
    print(f'Rodou por {(fim-inicio)//60} minutos e {(fim-inicio)%60} segundos')


if __name__ == "__main__":
    main()
