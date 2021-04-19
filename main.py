import numpy as np 
import math
import statistics

from numpy.random import randint
from numpy.random import random as rand
from matplotlib import pyplot as plt



def fitness_function(genes_list):
    genes_fitness_value_list = []
    for x in range(len(genes_list)):
        genes_fitness_value_list.append(genes_list[x].count(1))
        #print(genes_list[x].count(1))

    return genes_fitness_value_list


def fitness_function_decimal(genes_list):
    genes_fitness_value_list = []
    
    for gene in genes_list:
        partial_sum = 0 
        for bits in range(len(gene)):
            partial_sum = 10 - gene[bits] + partial_sum
            
        genes_fitness_value_list.append(partial_sum / 9)
       
        
    return genes_fitness_value_list


def check_supergen(genes_list, genes_fitness_value_list, bits_longitud, i_iteration, super_genes_position_list):
    for index in range(len(genes_list)):
        if index not in super_genes_position_list:
            if genes_fitness_value_list[index] == bits_longitud:
                print(len(super_genes_position_list)+1,'º SUPER GEN FOUND:', '\nITERATION: ',i_iteration, '\nGEN: ', genes_list[index], '\nPOSITION: ', index,'\n\n')
                super_genes_position_list.append(index)
            
            #else:
                #print('NOTHING INTERESTING HAS BEEN FOUN YET.. ITERATION: ', i_iteration,'/IDGEN: ', index, ' GEN: ', genes_list[index])
    return super_genes_position_list
    

def tournament_selection(genes_list, genes_fitness_value_list):
    lucky_gen_spaces = 3
    best_gen_position = randint(len(genes_list))
    for x in randint(0, len(genes_list), lucky_gen_spaces - 1):
        if genes_fitness_value_list[x] > genes_fitness_value_list[best_gen_position]:
            #print(x)
            best_gen_position = x
    
    return genes_list[best_gen_position]


def crossover(parent1, parent2, p_cross):
    child1, child2 = parent1.copy(), parent2.copy()
    
    if rand() < p_cross:
        pt = randint(1, len(parent1)-2)
        child1 = parent1[:pt] + parent2[pt:]
        child2 = parent2[:pt] + parent1[pt:]

    return child1, child2



def mutation(childs, p_mut):
    
    for child in childs:
        for i in range(len(child)):
            if rand() < p_mut:
                child[i] = 1 - child[i]
    return childs


def mutation_decimal(childs, p_mut):
    
    for child in childs:
        for i in range(len(child)):
            if rand() < p_mut:
                child[i] = randint(1, 10)
    return childs


def genetic_algorithm(n_iterations, bits_longitud, population_size, p_cross, p_mut):
    max_fitness_values, min_fitness_values, average_fitness_values, super_genes_position_list = [], [], [], []
  
    genes_list = [randint(0, 2, bits_longitud).tolist() for _ in range(population_size)]   
    for i_iteration in range(n_iterations):
        genes_fitness_value_list =  fitness_function(genes_list)
        super_genes_position_list = check_supergen(genes_list, genes_fitness_value_list, bits_longitud, i_iteration, super_genes_position_list)
        
        selected = [tournament_selection(genes_list, genes_fitness_value_list) for _ in range(population_size)]
        children = []

        #create the childrens
        for i in range (0, population_size, 2):
            parent1, parent2  = selected[i], selected[i+1]
            childs = crossover(parent1, parent2, p_cross)
            childs = mutation(childs, p_mut)
            children.extend(childs)

        genes_list = children
        max_fitness_values.append(max(genes_fitness_value_list))
        min_fitness_values.append(min(genes_fitness_value_list))
        average_fitness_values.append(statistics.mean(genes_fitness_value_list))
    
    
    x = range(n_iterations)
    plt.plot(x, max_fitness_values)
    plt.plot(x, average_fitness_values)
    plt.plot(x, min_fitness_values)
    
    plt.legend(["Max ", "Average ", "Min "], loc ="lower right")
    plt.xlabel("ITERACIONES")
    plt.ylabel("FITNESS VALUE")
    plt.show()

        

def genetic_algorithm_decimal_gene(n_iterations, bits_longitud, population_size, p_cross, p_mut):
    max_fitness_values, min_fitness_values, average_fitness_values, super_genes_position_list = [], [], [], []
    genes_list = [randint(1, 10, bits_longitud).tolist() for _ in range(population_size)]
    
    for i_iteration in range(n_iterations):
        genes_fitness_value_list =  fitness_function_decimal(genes_list)
        super_genes_position_list = check_supergen(genes_list, genes_fitness_value_list, bits_longitud, i_iteration, super_genes_position_list)
        
        selected = [tournament_selection(genes_list, genes_fitness_value_list) for _ in range(population_size)]
        children = []

        #create the childrens
        for i in range (0, population_size, 2):
            parent1, parent2  = selected[i], selected[i+1]
            childs = crossover(parent1, parent2, p_cross)
            childs = mutation_decimal(childs, p_mut)
            children.extend(childs)

        genes_list = children
        max_fitness_values.append(max(genes_fitness_value_list))
        min_fitness_values.append(min(genes_fitness_value_list))
        average_fitness_values.append(statistics.mean(genes_fitness_value_list))

    x = range(n_iterations)
    plt.plot(x, max_fitness_values)
    plt.plot(x, average_fitness_values)
    plt.plot(x, min_fitness_values)
    
    plt.legend(["Max ", "Average ", "Min "], loc ="lower right")
    plt.xlabel("ITERACIONES")
    plt.ylabel("FITNESS VALUE")
    plt.show()

        


def main():
    n_iterations = 300
    bits_longitud = 20
    population_size = 100
    p_cross = 0.7
    p_mut = 0.001
    #genetic_algorithm(n_iterations, bits_longitud, population_size, p_cross, p_mut)
    genetic_algorithm_decimal_gene(n_iterations, bits_longitud, population_size, p_cross, p_mut)




if __name__ == '__main__':
    main()

