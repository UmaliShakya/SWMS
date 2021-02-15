from datetime import datetime
import random
from reservoirs.models import Reservoir
from water_level.models import WaterLevel
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

                water_level = WaterLevel(
                    reservoir=reservoir,
                    date=Month(year, month),
                    water_level=random.randint(30000, 50000),
                    rainfall=random.randint(5, 25),
                    temperature=random.randint(25, 47),
                    evaporation=random.randint(2, 10)
                )

                print(water_level)

                water_level.save()
