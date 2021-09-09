# Kyle Sweigart, Student ID: 001521520

from nearestNeighbor import nearestNeighbor, truckEndDistances
from packageStatus import allPackageStatus
from loadTrucks import loadTrucks, truck1, truck2, truck3

# Calls the loadTrucks function and creates a list of packages for each truck
loadTrucks()

# Calls the nearestNeighbor algorithm three times with three separate parameters
# (truck number, starting node, list of packages).
nearestNeighbor(1,'HUB', truck1)
nearestNeighbor(2,'HUB', truck2)
nearestNeighbor(3,'HUB', truck3)

# Software name/version, author, and description.
print('WGUPS Routing Program v1.0.0')
print('Developed By: Kyle Sweigart\n')
print('This software will determine an efficient route and delivery distribution for WGUPS\'s Daily Local Deliveries.\n')

# User input that accepts one of two commands.
userInput = input("Enter one of the following commands:\n"
                  "'route' - Retrieves total distance traveled by all active delivery trucks.\n"
                  "'status' - Retrieves current status of all packages.\n")

# The route command adds each truck's total distance traveled together and displays the result.
if userInput == 'route':
    totalDistanceTraveled = sum(truckEndDistances)

    print('\n')
    print('Active delivery trucks successfully delivered 40 packages, traveling a total distance of '
          + str(round(totalDistanceTraveled, 1)) + ' miles.')

# The status command takes a time as input and passes the value to the allPackageStatus function.
if userInput == 'status':
    timeInput = input("Enter a specific time in this format: 'HH:MM'")

    # The allPackageStatus function returns the current status of all packages.
    allPackageStatus(timeInput)

