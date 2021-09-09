from csvReader import packageHashTable

# Three trucks ready to be loaded.
truck1 = []
truck2 = []
truck3 = []

# Determines which package goes on which truck
def determinePriority(pkgNumID, delDeadline, delInstruct):
    # Lists of information to help determine the priority of a package
    deadlines = ['9:00 AM', '10:30 AM', 'EOD']
    instructions = ['', 'Can only be on truck 2', 'Delayed on flight---will not arrive to depot until 9:05 am',
                    'Wrong address listed']

    # Conditional statements to manually assign each package to a truck
    if delDeadline == deadlines[0] and delInstruct == instructions[0]:
        truck1.append(pkgNumID)
    elif delDeadline == deadlines[1] and delInstruct == instructions[0]:
        truck2.append(pkgNumID)
    elif delDeadline == deadlines[2] and delInstruct == instructions[0]:
        truck3.append(pkgNumID)

    elif delDeadline == deadlines[0] or delDeadline == deadlines[1] or delDeadline == deadlines[2]\
            and delInstruct == instructions[1]:
        truck2.append(pkgNumID)
    elif delDeadline == deadlines[0] or delDeadline == deadlines[1] or delDeadline == deadlines[2]\
            and delInstruct == instructions[2]:
        truck3.append(pkgNumID)
    elif delDeadline == deadlines[0] or delDeadline == deadlines[1] or delDeadline == deadlines[2]\
            and delInstruct == instructions[3]:
        truck3.append(pkgNumID)
    elif delDeadline == deadlines[0] or delDeadline == deadlines[1] or delDeadline == deadlines[2]\
            and delInstruct == instructions[4]:
        truck3.append(pkgNumID)

# This function manually loads the three trucks.
def loadTrucks():
    groupedPkgs = ['13', '14', '15', '16', '19', '20']
    delayedPkgs = ['25', '28', '32']
    pkgList = [str(i) for i in range(1,41)]

    # Packages that need to be on the same truck.
    for pkg in groupedPkgs:
        truck1.append(pkg)
        pkgList.remove(pkg)

    # Load the delayed packages onto the third truck.
    for pkg in delayedPkgs:
        truck3.append(pkg)
        pkgList.remove(pkg)

    # Determines the priority of each package.
    for package in pkgList:
        packageData = packageHashTable.retrieve(package)
        determinePriority(packageData[0], packageData[5], packageData[7])

    # Reorganizes packages to comply with the truck's maximum number of packages constraint.
    while len(truck1) < 15:
        excessPkg = truck3[-1]
        truck3.remove(excessPkg)
        truck1.append(excessPkg)


        
