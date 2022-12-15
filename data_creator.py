import sys
import random
import numpy as np

POSSIBLE_NATIONALITIES = ["RO", "USA", "PL", "RU", "CZ", "FR", "UK", "IN", "DE", "AE"]

fileName = sys.argv[1]

with open(fileName, 'w') as file:
    file.write("varsta,sex,IQ,nationalitate\n")
    for i in range(150):
        file.write(",".join([
            str(int(random.triangular(20, 78))),
            "M" if random.randint(0, 1) else "F",
            str(int(random.triangular(50, 120))),
            random.choice(POSSIBLE_NATIONALITIES)
        ]) + '\n')
