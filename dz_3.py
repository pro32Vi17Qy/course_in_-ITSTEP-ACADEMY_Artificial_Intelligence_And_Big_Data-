import random


class Coda:
    impurities_counter = 0

    def __init__(self, impurities):
        self.impurities = impurities
        Coda.impurities_counter += 1

    def show_my_drink(self):
        if self.impurities_counter < 0:
            self.impurities_counter = 0
        if self.impurities_counter == 0:
            print("\nOrdinary carbonated water!")
        elif self.impurities_counter > 0:
            print(f"\nCarbonated water with {self.impurities_counter} molecules impurities")


random_returns = random.randint(1, 10)
for i in range(1):
    for i in range(random_returns):
        random_impurities = random.randint(-5, 5)
        impurities = Coda(random_impurities)
        Coda.impurities_counter += random_impurities
    impurities.show_my_drink()
