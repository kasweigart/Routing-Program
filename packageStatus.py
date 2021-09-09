from csvReader import packageHashTable
import datetime
from nearestNeighbor import packageDistanceFromHubHashTable, packageHashTable, truckEndDistances

# List of each package's delivery times
truckEndTimes = []

# The 8:00AM start time when any truck may leave the hub.
truckStartTime = datetime.datetime(1, 1, 1, 8, 0, 0)

# This function calculates the time any given package was delivered.
def getPackageTimes():
    # After the first truck returns, this determines when the third truck may depart the hub.
    truck3StartTime = milesTraveledToTime(truckEndDistances[0], truckStartTime)

    # Iterate through all packages and get the time it took to deliver the package.
    for i in range(1,41):
        package = packageDistanceFromHubHashTable.retrieve(str(i))
        if package[0] == 1:
            truckEndTime = milesTraveledToTime(package[2], truckStartTime)
            truckEndTimes.append([i, truckEndTime])
        if package[0] == 2:
            truckEndTime = milesTraveledToTime(package[2], truckStartTime)
            truckEndTimes.append([i, truckEndTime])
        if package[0] == 3:
            truckEndTime = milesTraveledToTime(package[2], truck3StartTime)
            truckEndTimes.append([i, truckEndTime])


# Helper function that calculates the time traveled from a given distance.
def milesTraveledToTime(milesTraveled, truckStartTime):
    timeTraveled = milesTraveled / 18
    hoursToMinutes = timeTraveled * 60
    packageEndTime = truckStartTime + datetime.timedelta(minutes=hoursToMinutes)
    return packageEndTime


# The allPackageStatus function returns the current status of all packages.
def allPackageStatus(time):
    # Calls the getPackageTimes function to create a list of package delivery times.
    getPackageTimes()

    # # After the first truck returns, this determines when the third truck may depart the hub.
    truck3StartTime = milesTraveledToTime(truckEndDistances[0], truckStartTime)

    # Parses the user's time input value.
    hr, min = map(int, time.split(':'))
    selectedTime = datetime.datetime(1, 1, 1, hour=hr, minute=min)

    # Prints header to describe the data below.
    print('Package ID Number|Delivery Address|Delivery Deadline|Delivery City|Delivery Zip Code|Package Weight|Delivery Status')

    # Assigns each variable to the package's corresponding data point.
    for i in truckEndTimes:
        package = packageHashTable.retrieve(str(i[0]))
        packageIDNumber = package[0]
        delAddress = package[1]
        delCity = package[2]
        delZipCode = package[4]
        delDeadline = package[5]
        packageWeight = package[6]
        packageEndTime = i[1]
        delTime = packageEndTime.time()

        # Conditional statements to determine the delivery status of a package.
        if packageEndTime < selectedTime and packageEndTime < truck3StartTime:
            delStatus = 'Delivered'
        if packageEndTime > selectedTime and packageEndTime > truck3StartTime:
            delStatus = 'At the hub'
            delTime = selectedTime.time()
        if packageEndTime < selectedTime and packageEndTime > truck3StartTime:
            delStatus = 'Delivered'
        if packageEndTime > selectedTime and packageEndTime < truck3StartTime:
            delStatus = 'En route'
            delTime = selectedTime.time()

        # Displays information about each package
        print(packageIDNumber + '|' + delAddress + '|' + delDeadline + '|' + delCity + '|' + delZipCode + '|' +
              packageWeight + '|' + delStatus, delTime)

