import pandas as pd
import numpy as np
from deap import base, creator, tools
import random

GENERATION_COUNT = 40


def geneticAlgorithm(water_usage_data, total_water_usage, total_water_output):

    def n_per_product_lower():
        return np.random.uniform(low=0.25, high=0.4, size=len(water_usage_data))

    def n_per_product_middle():
        return np.random.uniform(low=0.6, high=1.0, size=len(water_usage_data))

    def n_per_product_higher():
        return np.random.uniform(low=0.7, high=1.3, size=len(water_usage_data))

    def evaluate(individual):
        individual = individual[0]
        total_water_usage = sum(
            x*y for x, y in zip(water_usage_data, individual))
        return abs(total_water_output-total_water_usage),

    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()

    if (total_water_output-total_water_usage) >= 0:
        print('high')
        toolbox.register("n_per_product", n_per_product_higher)
    else:
        if total_water_output >= (total_water_usage/2):
            print('middle')
            toolbox.register("n_per_product", n_per_product_middle)
        else:
            print('low')
            toolbox.register("n_per_product", n_per_product_lower)

    toolbox.register("individual", tools.initRepeat,
                     creator.Individual, toolbox.n_per_product, n=1)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", evaluate)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=3)

    pop = toolbox.population(n=300)

    # Evaluate the entire population
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    # CXPB  is the probability with which two individuals
    #       aare crossed
    #
    # MUTPB is the probability for mutating an individual
    CXPB, MUTPB = 0.5, 0.2

    # Extracting all the fitnesses of
    fits = [ind.fitness.values[0] for ind in pop]

    # Variable keeping track of the number of generations
    g = 0

    # Begin the evolution
    while g < GENERATION_COUNT:
        # A new generation
        g = g + 1
        print("-- Generation %i --" % g)

        # Select the next generation individuals
        offspring = toolbox.select(pop, len(pop))
        # Clone the selected individuals
        offspring = list(map(toolbox.clone, offspring))

        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1[0], child2[0])
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant[0])
                del mutant.fitness.values

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        pop[:] = offspring

        # Gather all the fitnesses in one list and print the stats
        fits = [ind.fitness.values[0] for ind in pop]

        length = len(pop)
        mean = sum(fits) / length
        sum2 = sum(x*x for x in fits)
        std = abs(sum2 / length - (mean)**2)**0.5

        print(
            f'Minimum : {min(fits)}, Maximum : {max(fits)}, Mean : {mean}, Standard Deviation : {std}')

    best = pop[np.argmin([toolbox.evaluate(x) for x in pop])]
    return best[0].tolist()


def generate_water_distribution_plan(predicted_water_outputs, predicted_water_consumptions):
    water_level_list = [i['water_level'] for i in predicted_water_outputs]

    total_water_consumption = []
    consumption_list = []

    for i in range(len(predicted_water_consumptions[0]['data'])):
        sum = 0
        l = []
        for j in range(len(predicted_water_consumptions)):
            num = predicted_water_consumptions[j]['data'][i]['water_consumption']
            sum += num
            l.append(num)

        total_water_consumption.append(sum)
        consumption_list.append(l)

    output_list = []

    for i in range(len(water_level_list)):
        output_list.append(geneticAlgorithm(
            consumption_list[i], total_water_consumption[i], water_level_list[i]))

    result = [[a*b for a, b in zip(i, j)]
              for i, j in zip(consumption_list, output_list)]

    date_list = [i['date'] for i in predicted_water_outputs]

    home_list = [i['home'] for i in predicted_water_consumptions]

    output = []

    for i in range(len(date_list)):
        d = []
        for j in range(len(home_list)):
            d.append({
                'home': home_list[j],
                'value': result[i][j]
            })

        output.append({
            'date': date_list[i],
            'data': d
        })

    return output
