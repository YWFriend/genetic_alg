from random import randint
from typing import Callable


class Individual:
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

    def info(self):
        print(self.genotype, ' = ', self.phenotype)

    def count_phenotype(self):
        self.phenotype = self.health_func(self.genotype)

    def mutate(self, mutation_min: int, mutation_max: int) -> None:
        mutated_gen = self.create_gen(mutation_min, mutation_max)

        self.genotype[randint(0, len(self.genotype) - 1)] = mutated_gen

        while self.genotype.count(mutated_gen) > 1:
            mutated_gen = self.create_gen(mutation_min, mutation_max)

    @staticmethod
    def create_individual(genotype_array: list, attac_function: Callable[[list], int]):
        return Individual(
            genotype=genotype_array,
            phenotype=attac_function(genotype_array),
            health_func=attac_function
        )

    @staticmethod
    def create_gen(mutation_min: int, mutation_max: int) -> list[int]:
        return [randint(mutation_min, mutation_max), randint(mutation_min, mutation_max)]
