from random import shuffle, randint, random
from copy import deepcopy
from numpy import mean
from individ import Individual
from typing import Callable


class Population:
    def __init__(
            self,
            population: list[Individual],
            phenotype: float
    ):
        self.population: list[Individual] = population
        self.phenotype: float = phenotype

    def count_phenotype(self):
        self.phenotype = float(mean(list(map(lambda x: x.phenotype, self.population))))

    def info(self):
        for individual in self.population:
            individual.info()
        print("Average phenotype of population =", self.phenotype)

    def sort(self):
        self.population.sort(key=lambda i: i.phenotype, reverse=bool(1))

    def get_individual_size(self) -> int:
        return len(self.population[0].genotype)

    def crossover(self, limit: int, mutation_probability: float, mutation_min: int, mutation_max: int) -> bool:
        shuffle(self.population)
        previous_ind = self.population[0]

        for key, ind in enumerate(self.population):
            if key % 2 != 0:
                for i in range(randint(1, len(ind.genotype) // 2)):
                    ind.genotype[i], previous_ind.genotype[i] = previous_ind.genotype[i], ind.genotype[i]

                previous_ind.count_phenotype()

            for pos, gen in enumerate(ind.genotype):  # Exclusion of repeated genes in the genotype
                while ind.genotype.count(gen) > 1:
                    gen = Individual.create_gen(mutation_min, mutation_max)
                    ind.genotype[pos] = gen

            if random() < mutation_probability:  # Mutation
                ind.mutate(mutation_min, mutation_max)

            ind.count_phenotype()

            if ind.phenotype == limit or previous_ind.phenotype == limit:
                return bool(1)

            previous_ind = ind
        return bool(0)

    def selection(self):
        pop_for_selection = deepcopy(self.population[:len(self.population) // 2])
        self.population = pop_for_selection + deepcopy(pop_for_selection)

    def breeding(self, iteration_count: int, limit: int):
        self.info()

        for i in range(iteration_count):
            result = self.crossover(limit, 0.3, 0, 7)
            self.sort()
            self.info()
            self.selection()
            print('Generation: ', i + 1)
            if result:
                print('Result achieved, successful individual:')
                self.population[0].info()

                break
            else:
                self.count_phenotype()

    @staticmethod
    def create_population(
            population_size: int,
            genotype_func: Callable[[], list],
            attack_function: Callable[[list], int]
    ):
        assert population_size // 2 != 0, 'Size must be even'

        pop = [Individual.create_individual(genotype_func(), attack_function) for _ in range(population_size)]

        return Population(
            population=pop,
            phenotype=float(mean(list(map(lambda x: x.phenotype, pop)))),
        )
