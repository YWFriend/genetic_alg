import numpy as np
from typing import Callable
from numpy import ndarray


class Individual:  # Класс, описывающий индивида
    genotype: list
    phenotype: int

    def __init__(
            self,
            genotype: list,
            phenotype: int = 0
    ) -> None:
        self.genotype: list = genotype
        self.phenotype: int = phenotype

    def info(self):  # Вывод на экран индивида
        print(self.genotype, ' = ', self.phenotype)

    @staticmethod
    def create_individual(genotype_array: list, attac_function: Callable):
        return Individual(
            genotype=genotype_array,
            phenotype=attac_function(genotype_array)
        )
