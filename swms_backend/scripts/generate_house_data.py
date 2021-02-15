from datetime import datetime
import random
from reservoirs.models import Reservoir
from home_details.models import Home, HomeWaterConsumption
from month import Month

currentYear = datetime.now().year
currentMonth = datetime.now().month

START_YEAR = 2017

year_list = [y for y in range(START_YEAR, currentYear + 1)]

months_list = [m for m in range(1, 13)]


def run(*args):
    reservoirs = Reservoir.objects.all()

    for reservoir in reservoirs:

        i = 1

        for h in range(random.randint(25, 30)):
            home = Home(
                reservoir=reservoir,
                home_name=f"Home {i}",
                number_of_residents=random.randint(1, 7),
            )

            print(home)

            home.save()

            for year in year_list:
                for month in months_list:
                    if year == currentYear and month > currentMonth:
                        break

                    home_water_consumption = HomeWaterConsumption(
                        home=home,
                        date=Month(year, month),
                        water_consumption=random.randint(500, 1500),
                    )

                    print(home_water_consumption)

                    home_water_consumption.save()

            i += 1
