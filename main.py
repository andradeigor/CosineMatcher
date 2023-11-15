from TemplateMatching import TemplateMaching
from ParallelTemplateMatching import ParallelTemplateMaching
import time


def main():
    tp = ParallelTemplateMaching("./images/btgimage.jpg",
                                 "./templates/btgtemplate.jpg", 4)
    inicio = time.time()
    result = tp.templateMatching()
    fim = time.time()
    print((fim - inicio)/60)
    print(result)


if __name__ == "__main__":
    main()
