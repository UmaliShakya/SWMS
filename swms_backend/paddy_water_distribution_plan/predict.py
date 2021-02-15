# imports
import random as rnd
import prettytable as prettytable

# constance
populationSize = 10
numOfEliteSchedules = 1
tournamentSelectionSize = 3
mutationRate = 0.1

cu = 1233.48


class Data:

    def __init__(self, tanks, waterNeeds, availableCapacity):
        self.tanks = tanks
        self.water_needs = waterNeeds
        self.available_capacity = availableCapacity

        self._tanks = []
        self._availableCapacity = []
        self._waterNeeds = []

        # Inputs are stored as objects of relevant classes in arrays
        for i in range(0, len(self.water_needs)):
            self._waterNeeds.append(WaterNeeds(self.water_needs[i][0], self.water_needs[i][1], self.water_needs[i][2],
                                               self.water_needs[i][3], self.water_needs[i][4], self.water_needs[i][5],
                                               self.water_needs[i][6]))

        for i in range(0, len(self.available_capacity)):
            self._availableCapacity.append(
                AvailableCapacity(self.available_capacity[i][0], self.available_capacity[i][1],
                                  self.available_capacity[i][2], self.available_capacity[i][3],
                                  self.available_capacity[i][4], self.available_capacity[i][5]))

        for i in range(0, len(self.tanks)):
            self._tanks.append(
                Tank(self.tanks[i][0], self.tanks[i][1], self.tanks[i][2]))

    # Getters to get the stored data as objects
    def get_waterNeeds(self):
        return self._waterNeeds

    def get_availableCapacity(self):
        return self._availableCapacity

    def get_tanks(self):
        return self._tanks


# month should be pass as a parameter from the front end
class Schedule:
    def __init__(self, data):
        self.data = data
        # self.schemes = []
        self.month = 0
        self.schemeNum = 0
        self.isFitnessChanged = True
        # self.totalFromEachTank = []
        self.noOfConflicts = 0
        self.fitness = -1

    # to get the schemes which returns from initialize method
    def get_schemes(self):
        self.isFitnessChanged = True
        return self.schemes

    # to get the total amout of water get from each tank which returns from initialize method
    def get_totalFromEachTank(self):
        self.isFitnessChanged = True
        return self.totalFromEachTank

    # to get the number of conflicts calculateFitness method
    def get_numOfConflicts(self):
        return self.noOfConflicts

    # to get the fitness which returns calculateFitness method
    def get_fitness(self):
        if self.isFitnessChanged == True:
            self.fitness = self.calculateFitness()
            self.isFitnessChanged = False
        return self.fitness

    # initialize method of genetic algoruthm
    def initialize(self):
        tanks = self.data.get_tanks()
        wn = self.data.get_waterNeeds()
        ac = self.data.get_availableCapacity()
        # ac = [AvailableCapacity(self.data.available_capacity[])]
        # to get random water amounts from avalilable capacities of tanks
        fromNa = rnd.randrange(0, ac[self.month].get_nachchiduwaTank())
        fromNu = rnd.randrange(0, ac[self.month].get_nuwarawewaTank())
        fromThi = rnd.randrange(0, ac[self.month].get_thissawewaTank())
        fromThu = rnd.randrange(0, ac[self.month].get_thuruwilaTank())
        # to get the total water amount for a scheme
        total = fromNa + fromNu + fromThi + fromThu
        # total water amount released from each tanks for all the schemes
        totalFromNa = 0
        totalFromNu = 0
        totalFromThi = 0
        totalFromThu = 0
        self.schemes = []
        self.totalFromEachTank = []

        # for loop will execute for the number of tanks available
        for i in range(0, len(tanks)):
            newScheme = Scheme(self.schemeNum, tanks[i].get_name())
            self.schemeNum += 1

            newScheme.set_fullCapacity(tanks[i].get_tankCapacity())

            if i == 0:
                m_wn = wn[self.month].get_nachchiduwaScheme()
                m_ac = ac[self.month].get_nachchiduwaTank()

                # this loop will execute till total of random water amounts of all the tanks is equal to monthly
                # water need of Nachchiduwa scheme
                while total != m_wn:
                    fromNa = rnd.randrange(
                        0, ac[self.month].get_nachchiduwaTank())
                    fromNu = rnd.randrange(
                        0, ac[self.month].get_nuwarawewaTank())
                    fromThi = rnd.randrange(
                        0, ac[self.month].get_thissawewaTank())
                    fromThu = rnd.randrange(
                        0, ac[self.month].get_thuruwilaTank())
                    total = fromNa + fromNu + fromThi + fromThu
                    if total == m_wn:
                        fromNachchiduwa = fromNa
                        fromNuwarawewa = fromNu
                        fromThisawewa = fromThi
                        fromThuruwila = fromThu

                        newScheme.set_schemeWaterNeed(m_wn)
                        newScheme.set_currentCapacity(m_ac)
                        newScheme.set_fromNachchiduwa(fromNachchiduwa)
                        newScheme.set_fromNuwarawewa(fromNuwarawewa)
                        newScheme.set_fromThissawewa(fromThisawewa)
                        newScheme.set_fromThuruwila(fromThuruwila)

            if i == 1:
                m_wn = wn[self.month].get_nuwarawewaScheme()
                m_ac = ac[self.month].get_nuwarawewaTank()

                # this loop will execute till total of random water amounts of all the tanks is equal to monthly
                # water need of Nuwarawewa scheme
                while total != m_wn:
                    fromNa = rnd.randrange(
                        0, ac[self.month].get_nachchiduwaTank())
                    fromNu = rnd.randrange(
                        0, ac[self.month].get_nuwarawewaTank())
                    fromThi = rnd.randrange(
                        0, ac[self.month].get_thissawewaTank())
                    fromThu = rnd.randrange(
                        0, ac[self.month].get_thuruwilaTank())
                    total = fromNa + fromNu + fromThi + fromThu
                    if total == m_wn:
                        fromNachchiduwa = fromNa
                        fromNuwarawewa = fromNu
                        fromThisawewa = fromThi
                        fromThuruwila = fromThu

                        newScheme.set_schemeWaterNeed(m_wn)
                        newScheme.set_currentCapacity(m_ac)
                        newScheme.set_fromNachchiduwa(fromNachchiduwa)
                        newScheme.set_fromNuwarawewa(fromNuwarawewa)
                        newScheme.set_fromThissawewa(fromThisawewa)
                        newScheme.set_fromThuruwila(fromThuruwila)

            if i == 2:
                m_wn = wn[self.month].get_thisawewaScheme()
                m_ac = ac[self.month].get_thissawewaTank()

                # this loop will execute till total of random water amounts of all the tanks is equal to monthly
                # water need of Thisawewa scheme
                while total != m_wn:
                    fromNa = rnd.randrange(
                        0, ac[self.month].get_nachchiduwaTank())
                    fromNu = rnd.randrange(
                        0, ac[self.month].get_nuwarawewaTank())
                    fromThi = rnd.randrange(
                        0, ac[self.month].get_thissawewaTank())
                    fromThu = rnd.randrange(
                        0, ac[self.month].get_thuruwilaTank())
                    total = fromNa + fromNu + fromThi + fromThu
                    if total == m_wn:
                        fromNachchiduwa = fromNa
                        fromNuwarawewa = fromNu
                        fromThisawewa = fromThi
                        fromThuruwila = fromThu

                        newScheme.set_schemeWaterNeed(m_wn)
                        newScheme.set_currentCapacity(m_ac)
                        newScheme.set_fromNachchiduwa(fromNachchiduwa)
                        newScheme.set_fromNuwarawewa(fromNuwarawewa)
                        newScheme.set_fromThissawewa(fromThisawewa)
                        newScheme.set_fromThuruwila(fromThuruwila)

            if i == 3:
                m_wn = wn[self.month].get_thuruwilaScheme()
                m_ac = ac[self.month].get_thuruwilaTank()

                # this loop will execute till total of random water amounts of all the tanks is equal to monthly
                # water need of Thuruwila scheme
                while total != m_wn:
                    fromNa = rnd.randrange(
                        0, ac[self.month].get_nachchiduwaTank())
                    fromNu = rnd.randrange(
                        0, ac[self.month].get_nuwarawewaTank())
                    fromThi = rnd.randrange(
                        0, ac[self.month].get_thissawewaTank())
                    fromThu = rnd.randrange(
                        0, ac[self.month].get_thuruwilaTank())
                    total = fromNa + fromNu + fromThi + fromThu
                    if total == m_wn:
                        fromNachchiduwa = fromNa
                        fromNuwarawewa = fromNu
                        fromThisawewa = fromThi
                        fromThuruwila = fromThu

                        newScheme.set_schemeWaterNeed(m_wn)
                        newScheme.set_currentCapacity(m_ac)
                        newScheme.set_fromNachchiduwa(fromNachchiduwa)
                        newScheme.set_fromNuwarawewa(fromNuwarawewa)
                        newScheme.set_fromThissawewa(fromThisawewa)
                        newScheme.set_fromThuruwila(fromThuruwila)

            # to get the total water amount release from each tanks for all the schemes
            totalFromNa = totalFromNa + newScheme.get_fromNachchiduwa()
            totalFromNu = totalFromNu + newScheme.get_fromNuwarawewa()
            totalFromThi = totalFromThi + newScheme.get_fromThisawewa()
            totalFromThu = totalFromThu + newScheme.get_fromThuruwila()

            self.schemes.append(newScheme)

        self.totalFromEachTank = [totalFromNa,
                                  totalFromNu, totalFromThi, totalFromThu]

        return self

    def calculateFitness(self):
        ac = self.data.get_availableCapacity()
        self.noOfConflicts = 0
        totTanks = self.get_totalFromEachTank()
        calRemainingPercentage = 10
        remainingPercentage = []

        # highest fitness will be 1
        for i in range(0, len(totTanks)):
            # check if total amount get from a tank is greater than available water amount of that tank
            # if this condition id true number of conflicts will be increased by 1
            # and remainig water percentage of the tank will be calculated
            if i == 0:
                calRemainingPrecentage = (
                    (ac[self.month].get_nachchiduwaTank() - totTanks[i]) / 100)
                remainingPercentage.append(calRemainingPrecentage)
                if totTanks[i] > ac[self.month].get_nachchiduwaTank():
                    self.noOfConflicts = self.noOfConflicts + 1

            if i == 1:
                calRemainingPrecentage = (
                    (ac[self.month].get_nuwarawewaTank() - totTanks[i]) / 100)
                remainingPercentage.append(calRemainingPrecentage)
                if totTanks[i] > ac[self.month].get_nuwarawewaTank():
                    self.noOfConflicts = self.noOfConflicts + 1
            if i == 2:
                calRemainingPrecentage = (
                    (ac[self.month].get_thissawewaTank() - totTanks[i]) / 100)
                remainingPercentage.append(calRemainingPrecentage)
                if totTanks[i] > ac[self.month].get_thissawewaTank():
                    self.noOfConflicts = self.noOfConflicts + 1
            if i == 3:
                calRemainingPrecentage = (
                    (ac[self.month].get_thuruwilaTank() - totTanks[i]) / 100)
                remainingPercentage.append(calRemainingPrecentage)
                if totTanks[i] > ac[self.month].get_thuruwilaTank():
                    self.noOfConflicts = self.noOfConflicts + 1

        # if remaining precentage is not equal with each other number of conflicts will be increased by 1
        if remainingPercentage[0] != remainingPercentage[1]:
            self.noOfConflicts += 1
        if remainingPercentage[0] != remainingPercentage[2]:
            self.noOfConflicts += 1
        if remainingPercentage[0] != remainingPercentage[3]:
            self.noOfConflicts += 1
        if remainingPercentage[1] != remainingPercentage[2]:
            self.noOfConflicts += 1
        if remainingPercentage[1] != remainingPercentage[3]:
            self.noOfConflicts += 1
        if remainingPercentage[2] != remainingPercentage[3]:
            self.noOfConflicts += 1

        return 1 / (1.0 * self.noOfConflicts + 1)

    def printValues(self):
        for i in range(0, len(self.schemes)):
            print(self.schemes[i])

    def __str__(self):
        returnValue = ""
        for i in range(0, len(self.schemes)):
            returnValue += str(self.schemes[i]) + ","
        returnValue += str(self.schemes[len(self.schemes) - 1])
        return returnValue


class Population:
    def __init__(self, size, data):
        self.size = size
        self.data = data
        self.schedules = []

        # initialize method will executed for the number of population size
        for i in range(0, size):
            self.schedules.append(Schedule(self.data).initialize())

    def get_schedule(self):
        return self.schedules


class GeneticAlgorithm:

    def __init__(self, data):
        self.data = data

    def evolve(self, population):
        return self.mutatePopulation(self.crossoverPopulation(population))

    def crossoverPopulation(self, pop):
        crossoverPop = Population(0, self.data)

        for i in range(numOfEliteSchedules):
            crossoverPop.get_schedule().append(pop.get_schedule()[i])

        i = numOfEliteSchedules

        while i < populationSize:
            schedule1 = self.selectTournamentPopulation(pop).get_schedule()[0]
            schedule2 = self.selectTournamentPopulation(pop).get_schedule()[0]
            crossoverPop.get_schedule().append(self.crossoverSchedule(schedule1, schedule2))
            i += 1

        return crossoverPop

    def mutatePopulation(self, population):
        for i in range(numOfEliteSchedules):
            self.mutateSchedule(population.get_schedule()[i])
        return population

    def crossoverSchedule(self, schedule1, schedule2):
        crossover_schedule = Schedule(self.data).initialize()

        for i in range(0, len(crossover_schedule.get_schemes())):
            if rnd.random() > 0.5:
                crossover_schedule.get_schemes(
                )[i] = schedule1.get_schemes()[i]
            else:
                crossover_schedule.get_schemes(
                )[i] = schedule2.get_schemes()[i]
            return crossover_schedule

    def mutateSchedule(self, mutateSchedule):
        schedule = Schedule(self.data).initialize()
        for i in range(0, len(mutateSchedule.get_schemes())):
            if (mutationRate > rnd.random()):
                mutateSchedule.get_schemes()[i] = schedule.get_schemes()[i]
            return mutateSchedule

    def selectTournamentPopulation(self, pop):
        tournament_pop = Population(0, self.data)
        i = 0
        while i < tournamentSelectionSize:
            tournament_pop.get_schedule().append(
                pop.get_schedule()[rnd.randrange(0, populationSize)])
            i += 1
        tournament_pop.get_schedule().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_pop


# to store water consumption prediction data
class WaterNeeds:
    def __init__(self, ID, season, month, nachchiduwaScheme, nuwarawewaScheme, thisawewaScheme, thuruwilaScheme):
        self.ID = ID
        self.season = season
        self.month = month
        self.nachchiduwaScheme = nachchiduwaScheme
        self.nuwarawewaScheme = nuwarawewaScheme
        self.thisawewaScheme = thisawewaScheme
        self.thuruwilaScheme = thuruwilaScheme

        # getters

    def get_ID(self):
        return self.ID

    def get_season(self):
        return self.season

    def get_month(self):
        return self.month

    def get_nachchiduwaScheme(self):
        return self.nachchiduwaScheme

    def get_nuwarawewaScheme(self):
        return self.nuwarawewaScheme

    def get_thisawewaScheme(self):
        return self.thisawewaScheme

    def get_thuruwilaScheme(self):
        return self.thuruwilaScheme


# to store water capacity prediction data
class AvailableCapacity:
    def __init__(self, ID, month, nachchiduwaTank, nuwarawewaTank, thisawewaTank, thuruwilaTank):
        self.ID = ID
        self.month = month
        self.nachchiduwaTank = nachchiduwaTank
        self.nuwarawewaTank = nuwarawewaTank
        self.thisawewaTank = thisawewaTank
        self.thuruwilaTank = thuruwilaTank

    # getters

    def get_ID(self):
        return self.ID

    def get_month(self):
        return self.month

    def get_nachchiduwaTank(self):
        return self.nachchiduwaTank

    def get_nuwarawewaTank(self):
        return self.nuwarawewaTank

    def get_thissawewaTank(self):
        return self.thisawewaTank

    def get_thuruwilaTank(self):
        return self.thuruwilaTank


# for tank details
class Tank:
    def __init__(self, ID, name, tankCapacity):
        self.ID = ID
        self.name = name
        self.tankCapacity = tankCapacity

    # getters
    def get_ID(self):
        return self.ID

    def get_name(self):
        return self.name

    def get_tankCapacity(self):
        return self.tankCapacity


# to store data of schemes. One scheme get water from all the tanks instead of one tank.
class Scheme:
    def __init__(self, ID, tank):
        self.ID = ID
        self.tank = tank
        self.fullCapacity = 0
        self.schemeWaterNeed = 0
        self.currentCapacity = 0
        self.fromNachchiduwa = 0
        self.fromNuwarawewa = 0
        self.fromThisawewa = 0
        self.fromThuruwila = 0

    # getters

    def get_ID(self):
        return self.ID

    def get_tank(self):
        return self.tank

    def get_fullCapacity(self):
        return self.fullCapacity

    def get_schemeWaterNeed(self):
        return self.schemeWaterNeed

    def get_currentCapacity(self):
        return self.currentCapacity

    def get_fromNachchiduwa(self):
        return self.fromNachchiduwa

    def get_fromNuwarawewa(self):
        return self.fromNuwarawewa

    def get_fromThisawewa(self):
        return self.fromThisawewa

    def get_fromThuruwila(self):
        return self.fromThuruwila

    # setters
    def set_fullCapacity(self, fullCapacity):
        self.fullCapacity = fullCapacity

    def set_schemeWaterNeed(self, schemeWaterNeed):
        self.schemeWaterNeed = schemeWaterNeed

    def set_currentCapacity(self, currentCapacity):
        self.currentCapacity = currentCapacity

    def set_fromNachchiduwa(self, fromNachchiduwa):
        self.fromNachchiduwa = fromNachchiduwa

    def set_fromNuwarawewa(self, fromNuwarawewa):
        self.fromNuwarawewa = fromNuwarawewa

    def set_fromThissawewa(self, fromThisawewa):
        self.fromThisawewa = fromThisawewa

    def set_fromThuruwila(self, fromThuruwila):
        self.fromThuruwila = fromThuruwila

    def __str__(self):
        return '{0},{1},{2},{3},{4},{5},{6},{7}'.format(str(self.tank), str(self.fullCapacity),
                                                        str(self.schemeWaterNeed), str(
                                                            self.currentCapacity),
                                                        str(self.fromNachchiduwa), str(
                                                            self.fromNuwarawewa),
                                                        str(self.fromThisawewa), str(self.fromThuruwila))


# to display the outputs
class DisplayMgr:

    def __init__(self, data):
        self.data = data

    def print_availableData(self):
        print("> All available data")
        self.print_waterNeeds()
        # self.print_availableCapacity()
        # self.print_tankDetails()

    def print_waterNeeds(self):
        wNeeds = self.data.get_waterNeeds()
        wnTable = prettytable.PrettyTable(
            ['Month', 'Season', 'Nachchiduwa Scheme', 'Nuwarawewa Scheme', 'Thisawewa Scheme', 'Thuruwila Scheme'])
        for i in range(0, len(wNeeds)):
            month = wNeeds.__getitem__(i).get_month()
            season = wNeeds.__getitem__(i).get_season()
            NaScheme = wNeeds.__getitem__(i).get_nachchiduwaScheme()
            NuScheme = wNeeds.__getitem__(i).get_nuwarawewaScheme()
            ThiScheme = wNeeds.__getitem__(i).get_thisawewaScheme()
            ThuScheme = wNeeds.__getitem__(i).get_thuruwilaScheme()
            wnTable.add_row(
                [month, season, NaScheme, NuScheme, ThiScheme, ThuScheme])
        print(wnTable)

    def print_generations(self, population):
        schedules = population.get_schedule()
        generationTable = prettytable.PrettyTable(
            ['Schedule #', 'fitness', 'Total from each', 'No of Conflicts', 'schemes'])
        for i in range(0, len(schedules)):
            generationTable.add_row(
                [str(i), round(schedules[i].get_fitness(), 3), schedules[i].get_totalFromEachTank(),
                 schedules[i].get_numOfConflicts(), schedules[i]])
        print(generationTable)

    def print_schedule_as_table(self, schedule):
        schemes = schedule.get_schemes()
        table = prettytable.PrettyTable(
            ['Schedule #', 'Tank', 'Full Capacity', 'Scheme Water Need', 'Current Capacity', 'From Nachchiduwa',
             'From Nuwarawewa', 'From Thisawewa', 'From Thuruwila'])

        for i in range(0, len(schemes)):
            table.add_row(
                [str(i), schemes[i].get_tank(), schemes[i].get_fullCapacity(), schemes[i].get_schemeWaterNeed(),
                 schemes[i].get_currentCapacity(), schemes[i].get_fromNachchiduwa(
                ), schemes[i].get_fromNuwarawewa(),
                    schemes[i].get_fromThisawewa(), schemes[i].get_fromThuruwila()])
        print(table)


def main(tanks, available_capacity, water_needs):
    print(tanks)

    data = Data(tanks, water_needs, available_capacity)
    display1 = DisplayMgr(data)
    generationNumber = 0
    print("\n > Generation Number = " + str(generationNumber))
    Pop1 = Population(populationSize, data)
    Pop1.get_schedule().sort(key=lambda x: x.get_fitness(), reverse=True)
    display1.print_generations(Pop1)
    display1.print_schedule_as_table(Pop1.get_schedule()[0])

    geneticAlgorithm = GeneticAlgorithm(data)
    while Pop1.get_schedule()[0].get_fitness() != 1.0 and generationNumber < 10:
        generationNumber += 1
        print("\n> Generation # " + str(generationNumber))
        Pop1 = geneticAlgorithm.evolve(Pop1)
        Pop1.get_schedule().sort(key=lambda x: x.get_fitness(), reverse=True)
        display1.print_generations(Pop1)
        display1.print_schedule_as_table(Pop1.get_schedule()[0])
        print("\n\n")

    output = []

    for i in Pop1.get_schedule()[0].get_schemes():
        output.append({
            'tank': i.get_tank(),
            'full_capacity': i.get_fullCapacity(),
            'schema_water_needed': (int)(i.get_schemeWaterNeed()*cu),
            'current_capacity': (int)(i.get_currentCapacity()*cu),
            'from_nachchiduwa': (int)(i.get_fromNachchiduwa()*cu),
            'from_nuwarawewa': (int)(i.get_fromNuwarawewa()*cu),
            'from_thisawewa': (int)(i.get_fromThisawewa()*cu),
            'from_thuruwila': (int)(i.get_fromThuruwila()*cu),
        })

    return output


def generate_paddy_water_distribution_plan(data_list):

    # tanks = [[1, 'Nachchaduwa', 45150], [2, 'Nuwara Wewa', 36050],
    #          [3, 'Thisawewa', 3500], [4, 'Thuruwila Wewa', 5190]]

    tanks = [
        [1, data_list[0]['reservoir'].name, data_list[0]['reservoir'].capacity],
        [2, data_list[1]['reservoir'].name, data_list[1]['reservoir'].capacity],
        [3, data_list[2]['reservoir'].name, data_list[2]['reservoir'].capacity],
        [4, data_list[3]['reservoir'].name, data_list[3]['reservoir'].capacity],
    ]

    output = []

    for i in range(len(data_list[0]['predicted_water_levels'])):

        # available_capacity = [[1, 'January', 29, 35, 35, 27]]

        available_capacity = [[1, 'January',
                               (int)(
                                   data_list[0]['predicted_water_levels'][i]['water_level']/cu),
                               (int)(
                                   data_list[1]['predicted_water_levels'][i]['water_level']/cu),
                               (int)(
                                   data_list[2]['predicted_water_levels'][i]['water_level']/cu),
                               (int)(
                                   data_list[3]['predicted_water_levels'][i]['water_level']/cu),
                               ]]

        # water_needs = [[1, 'Maha', 'January', 30, 33, 35, 30]]

        water_needs = [[1, 'Maha', 'January',
                        (int)(
                            data_list[0]['predicted_water_consumptions'][i]['water_consumption_paddy']/cu),
                        (int)(
                            data_list[1]['predicted_water_consumptions'][i]['water_consumption_paddy']/cu),
                        (int)(
                            data_list[2]['predicted_water_consumptions'][i]['water_consumption_paddy']/cu),
                        (int)(
                            data_list[3]['predicted_water_consumptions'][i]['water_consumption_paddy']/cu),
                        ]]

        output.append({
            'date': data_list[0]['predicted_water_levels'][i]['date'],
            'data': main(tanks, available_capacity, water_needs),
        })

    return output
