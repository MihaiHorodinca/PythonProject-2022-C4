import copy
import csv
import sys
import statistics

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
