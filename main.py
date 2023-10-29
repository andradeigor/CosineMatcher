from TemplateMatching import TemplateMaching
from ParallelTemplateMatching import ParallelTemplateMaching
import time


def main():
    tp = ParallelTemplateMaching("./images/btgimage.jpg",
                                 "./templates/btgtemplate.jpg")
    inicio = time.time()
    result = tp.run()
    fim = time.time()
    print((fim - inicio)/60)
    print(result)


if __name__ == "__main__":
    main()
