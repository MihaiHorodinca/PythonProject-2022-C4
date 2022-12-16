import csv
import sys
import statistics
import matplotlib.pyplot as plt

AGE_COLUMN_NAME: str = "varsta"
SEX_COLUMN_NAME = "sex"
IQ_COLUMN_NAME = "IQ"
NAT_COLUMN_NAME = "nationalitate"


def main():
    fileName = sys.argv[1]

    compute_basic_stats(fileName)

    compute_plot(fileName)


"""
This method is tasked with reading the contents of the given file and printing in console some basic age statistics.
The values printed are: mean, median, min, max, standard deviation and the quartiles.
It also computes the covariance between the age and the IQ.

:param fileName: this is the path to the csv file (it can be "in.csv" or the absolute path)
:returns: nothing (prints out the values)
"""


def compute_basic_stats(fileName):
    ageList = []
    sexList = []
    IQList = []
    natList = []

    with open(fileName, 'r') as file:
        valueDict = csv.DictReader(file)

        for row in valueDict:
            ageList.append(int(row[AGE_COLUMN_NAME]))
            sexList.append(row[SEX_COLUMN_NAME])
            IQList.append(int(row[IQ_COLUMN_NAME]))
            natList.append(row[NAT_COLUMN_NAME])

    print(ageList)
    print(statistics.mean(ageList))
    print(statistics.median(ageList))
    print(min(ageList))
    print(max(ageList))
    print(statistics.stdev(ageList))
    print(statistics.quantiles(ageList))

    print(statistics.covariance(ageList, IQList))


"""
This method is tasked with reading the contents of the given file and computing the age/IQ plot.
The age/IQ values are grouped in 7-year ranges and averaged for a clearer understanding of the data on the cart.
All of the actual data points are also visible in the background.

:param fileName: this is the path to the csv file (it can be "in.csv" or the absolute path)
:returns: nothing (prints out the plot)
"""


def compute_plot(fileName):
    with open(fileName, 'r') as file:
        valueDict = csv.DictReader(file)

        # Save (age, IQ) tuples for all the data points and sort them by age
        plotValues = [(int(row[AGE_COLUMN_NAME]), int(row[IQ_COLUMN_NAME])) for row in valueDict]
        plotValues.sort(key=lambda x: x[0])

        # First plot where X is the ageGroup and Y is the average for that group
        plt.plot([ageGroup for ageGroup in range(20, 90, 7)],
                 [int(
                     statistics.mean([int(x[1]) for x in plotValues if (ageGroup - 4 <= x[0] <= ageGroup + 4)]))
                     for ageGroup in range(20, 90, 7)],
                 'o--',
                 color='grey'
                 )

        # Background plot where X is the age and Y is the IQ
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


main()
