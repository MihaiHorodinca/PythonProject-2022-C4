import csv
import sys
import statistics
import matplotlib.pyplot as plt

fileName = sys.argv[1]

varsta = []
sex = []
IQ = []
nationalitate = []

with open(fileName, 'r') as file:
    valueDict = csv.DictReader(file)

    for row in valueDict:
        varsta.append(int(row["varsta"]))
        sex.append(row["sex"])
        IQ.append(int(row["IQ"]))
        nationalitate.append(row["nationalitate"])

print(varsta)
print(statistics.mean(varsta))
print(statistics.median(varsta))
print(min(varsta))
print(max(varsta))
print(statistics.stdev(varsta))
print(statistics.quantiles(varsta))

print(statistics.covariance(varsta, IQ))

with open(fileName, 'r') as file:
    valueDict = csv.DictReader(file)

    plotValues = [(int(row["varsta"]), int(row["IQ"])) for row in valueDict]
    plotValues.sort(key=lambda x: x[0])

    plt.plot([ageGroup for ageGroup in range(20, 90, 7)],
             [int(statistics.mean([int(x[1]) for x in plotValues if (ageGroup - 4 <= x[0] and x[0] <= ageGroup + 4)])) for ageGroup in range(20, 90, 7)],
             'o--',
             color='grey'
             )

    plt.plot([value[0] for value in plotValues],
             [value[1] for value in plotValues],
             'o',
             color='grey',
             alpha=0.3
             )

    plt.xlabel('Varsta')
    plt.ylabel('IQ')

    plt.title('Raport demo')
    plt.axis([15, 92, 0, 150])
    plt.grid(axis='x', color='0.95')

    plt.show()
