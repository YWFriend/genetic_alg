from typing import Callable


class Individual:  # Класс, описывающий индивида
    genotype: list
    phenotype: int
    health_func: Callable[[list], int]

    def __init__(
            self,
            genotype: list,
            phenotype: int,
            health_func: Callable[[list], int]
    ) -> None:
        self.genotype: list = genotype
        self.phenotype: int = phenotype
        self.health_func: Callable[[list], int] = health_func

    def info(self):  # Вывод на экран индивида
        print(self.genotype, ' = ', self.phenotype)

    def check_health(self):
        self.phenotype = self.health_func(self.genotype)

    @staticmethod
    def create_individual(genotype_array: list, attac_function: Callable[[list], int]):
        return Individual(
            genotype=genotype_array,
            phenotype=attac_function(genotype_array),
            health_func=attac_function
        )
