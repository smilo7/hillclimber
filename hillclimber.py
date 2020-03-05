'''
Author: Milo
Date: Feb/March 2020
Project: Hillclimber optimization implementation for a packing problem.
'''

import numpy as np
import matplotlib.pyplot as plt
import random

#bag capacity
capacity = 20
current_best = 0

#item containing a benefit value and volume value
class Item:
    def __init__(self, id, benefit, volume):
        self.id = id
        self.benefit = benefit
        self.volume = volume

#make list of items
items = []
items.append(Item('a', 5, 3))
items.append(Item('b', 6, 2))
items.append(Item('c', 1, 4))
items.append(Item('d', 9, 5))
items.append(Item('e', 2, 8))
items.append(Item('f', 8, 9))
items.append(Item('g', 4, 10))
items.append(Item('h', 3, 1))
items.append(Item('i', 7, 6))
items.append(Item('j', 10, 7))

#A hillclimber!
class Hillclimber:
    def __init__(self, genotype, capacity=20):
        self.genotype = genotype # in the case of the packing problem genotyp is the list of possible items
        self.phenotype = np.random.randint(2, size=10)
        self.current_fitness = 0 #initially no fitness
        self.capacity = capacity
        self.fitness_log = []
        self.volume_log = []

    #gets the current fitness
    def fitness(self, pheno):
        sum_volume = 0
        sum_benefit = 0
        for phen, geno in zip(pheno, self.genotype):
            if (phen == 1): #if gene is on
                sum_volume += geno.volume
                sum_benefit += geno.benefit

        if sum_volume > self.capacity: #if its greater than capacity should return 0. overcapacity solutions are not very fit
            return 0
        else:
            return sum_benefit #otherwise return the total of all benefits

    def get_volume(self, pheno):
        sum_volume = 0
        for phen, geno in zip(pheno, self.genotype):
            if (phen == 1): #if gene is on
                sum_volume += geno.volume
        return sum_volume

    def mutate(self):
        #make a copy of the current phenotype
        copy = np.copy(self.phenotype)
        #mutation_rate = 0.7
        num = random.randint(1,4) # number of genes to flip
        for _ in range(0, num):
            r = random.randint(0,9) #choose a random gene to flip each time
            copy[r] = int(not copy[r])
            #if copy[r] == 1:
            #    copy[r] = 0
            #else:
            #    copy[r] = 1

        return copy

    def evolve(self):
        for _ in range (0,300):
            new_mutation = self.mutate()
            #print(new_mutation)
            if (self.fitness(new_mutation) > self.fitness(self.phenotype)):
                self.phenotype = new_mutation
                #print("hello")
                #print(self.fitness(new_mutation))
                #print(self.fitness(self.phenotype))
            self.fitness_log.append(self.fitness(self.phenotype))
            self.volume_log.append(self.get_volume(self.phenotype))
        return self.phenotype, self.get_volume(self.phenotype)
    


def make_population_of_climbers(number):
    climbers = []
    for each in range(0, number):
        climbers.append(Hillclimber(items))
    for each in climbers:
        each.evolve()
    return climbers


#climber = Hillclimber(items)
#climber.evolve()
#print(climber.fitness_log[99:])

population = make_population_of_climbers(20)

#plot graph of fitness over generations


plt.style.use('seaborn')
#plt.plot(climber.fitness_log, label="fitness")
#plt.plot(climber.volume_log, label="volume")
#plt.legend()
for each in population:
    plt.plot(each.fitness_log)
    print(each.fitness_log[299:])


plt.xlabel("Generations")
plt.ylabel("Fitness")

#print("fitness at end:", climber.current_fitness)