from datetime import datetime
import random
from reservoirs.models import Reservoir
from water_consumption_domestic.models import WaterConsumptionDomestic
from month import Month

currentYear = datetime.now().year
currentMonth = datetime.now().month

START_YEAR = 2005

year_list = [y for y in range(START_YEAR, currentYear + 1)]

months_list = [m for m in range(1, 13)]


def run(*args):
    reservoirs = Reservoir.objects.all()

    for reservoir in reservoirs:
        for year in year_list:
            for month in months_list:
                if year == currentYear and month > currentMonth:
                    break

                water_consumption_domestic = WaterConsumptionDomestic(
                    reservoir=reservoir,
                    date=Month(year, month),
                    water_consumption_domestic=random.randint(20000, 40000),
                    population=random.randint(5000, 20000),
                    no_of_families=random.randint(1000, 5000),
                    no_of_housing_units=random.randint(1000, 5000),
                )

                print(water_consumption_domestic)

                water_consumption_domestic.save()
