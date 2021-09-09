from csvReader import packageHashTable, distanceMatrix
from hashTable import HashTable

# Stores all distances traveled from node to node.
totalRouteDistance = []

# Stores each truck's total route distance.
truckEndDistances = []

# Creates a new hash table object for distance data.
packageDistanceFromHubHashTable = HashTable()

# Nearest neighbor algorithm to find nearest unvisited node until all nodes have been visited.
def nearestNeighbor(truckNumber, currentAddress, packages):
    # Initializes a few variables.
    visitedAddress = ''
    lowestDistance = 15
    pkgList = packages
    truckNum = truckNumber

    # Iterates through packages on truck. Address is retrieved from the hash table and is passed to a function that
    # finds the distance between two given nodes.
    for item in pkgList:
        address = packageHashTable.retrieve(item)
        newDistance = findDistanceBetweenCities(currentAddress, address[1])

        # Updates the new lowest distance.
        if newDistance < lowestDistance:
            lowestDistance = newDistance
            visitedAddress = address[1]

    # Appends the new lowest distance into the total route distance list. Sums the current total route distance.
    # Assigns list of values to a variable.
    totalRouteDistance.append(lowestDistance)
    distanceFromHub = sum(totalRouteDistance)
    secondParam = [truckNum, visitedAddress, distanceFromHub]

    # Visited nodes data are inserted into a hash table and removed from the package list.
    for item in pkgList:
        address = packageHashTable.retrieve(item)
        if visitedAddress == address[1]:
            packageDistanceFromHubHashTable.insert(item, secondParam)
            pkgList.remove(item)

    # Once all packages have been delivered, truck returns to the hub.
    if len(pkgList) == 0:
        returnToHub = findDistanceBetweenCities(visitedAddress, 'HUB')
        totalRouteDistance.append(returnToHub)
        sumRoute = sum(totalRouteDistance)
        truckEndDistances.append(sumRoute)
        totalRouteDistance.clear()

    # Recursively calls the function until the package list is empty.
    while pkgList != []:
        nearestNeighbor(truckNum, visitedAddress, pkgList)

    # Returns the total distance traveled in one truck's route.
    return sum(totalRouteDistance)


# Helper function for core algorithm that finds distance between two given cities.
def findDistanceBetweenCities(firstCityParam, secondCityParam):
    # Initializes a few variables.
    firstCity = firstCityParam
    secondCity = secondCityParam
    firstCityIndex = 0
    secondCityIndex = 0
    firstDistanceList = []
    secondDistanceList = []

    # Find the two given cities in the distance matrix data structure and return the distance between them.
    for city in distanceMatrix:
        if city[1] == firstCity:
            firstDistanceList = city
            firstCityIndex = distanceMatrix.index(city)
        if city[1] == secondCity:
            secondDistanceList = city
            secondCityIndex = distanceMatrix.index(city)

    # Swaps each axis of the distance matrix if distance is not found.
    if firstCityIndex <= secondCityIndex:
        distanceFound = secondDistanceList[firstCityIndex + 2]
    else:
        distanceFound = firstDistanceList[secondCityIndex + 2]

    # Returns a float of the distance between two nodes.
    return float(distanceFound)

