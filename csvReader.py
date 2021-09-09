from hashTable import HashTable
import csv

# Instantiate new Hash Table object
packageHashTable = HashTable()

# Opens package file and reads data
with open('Package File.csv', encoding='utf-8-sig') as packageFile:
    readCSV = csv.reader(packageFile, delimiter=',')

    # Assigns comma delimited data to variables
    for entry in readCSV:
        pkgIdNum = entry[0]
        delAddress = entry[1]
        delCity = entry[2]
        delState = entry[3]
        delZipCode = entry[4]
        delBeginTime = entry[5]
        pkgWeight = entry[6]
        delInstruct = entry[7]

        # Bundles variables into 'value' parameter for hash table
        secondParam = [pkgIdNum, delAddress, delCity, delState, delZipCode, delBeginTime, pkgWeight, delInstruct]
        packageHashTable.insert(pkgIdNum, secondParam)

# Initialize nested list of lists of distance data.
distanceMatrix = []

# Opens distance table and reads data
with open('Distance Table.csv', encoding='utf-8-sig') as distanceTable:
    readCSV = csv.reader(distanceTable, delimiter=',')
    distanceMatrix = list(readCSV)

    # Parse city and zip code.
    for entry in distanceMatrix:
        entry[1] = entry[1].split('\n', 1)[0]


