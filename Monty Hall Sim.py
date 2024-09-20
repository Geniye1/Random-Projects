# SIMULATION VISUALLY DEMONSTRATING THE OUTCOME OF N TRIALS OF THE MONTY HALL PROBLEM. EXPECTED: 2/3 OF TRIALS WIN THE CAR, 1/3 WINS GOAT

# 1. Three choices, randomly choose one of them to have the car behind it
# 2. Contestant randomly chooses one of the doors
# 3. Host chooses one of the others doors (always the one with a goat)
# 4. Contestant will switch doors to the one they did not choose that hasn't been revealed
# 5. Record the outcome and, unless desired number of trials has been reached, GOTO 1
# 6. After the sim is over, display the results in a pie chart

# If the contestant doesn't switch, they have a 1/3 chance of winning. If they do switch, though, it becomes a 2/3 chance. This is because INITIALLY 
# it is 1/3 as the car is behind one of the three doors, while the other doors hold the remaining chances, 2/3. When Monty removes one of the doors,
# that probability does not change, and actually now all is held within the last door. So its either you have a 1/3 chance of winning if you stick
# to your initial choice or you switch doors and have a 2/3 chance of winning. Illogical, but this simulation proves it is true.

from random import randint
import matplotlib.pyplot as plt
import numpy as np

def Simulation(maxNumberOfTrials):
    # Run simulation for sticking to initial choice
    gamesNonswitchWon = 0
    gamesNonswitchLost = 0
    for i in range(0, maxNumberOfTrials):
        result = SimulationTrial(False)
        if result:
            gamesNonswitchWon += 1
        else:
            gamesNonswitchLost += 1

    plt.figure(0)
    pieChart = np.array([gamesNonswitchWon, gamesNonswitchLost])
    myLabels = ['Games won', 'Games lost']
    plt.title('Without Switching')
    plt.pie(pieChart, labels=myLabels)

    # Run simulation for switching to other door
    gamesSwitchWon = 0
    gamesSwitchLost = 0
    for i in range(0, maxNumberOfTrials):
        result = SimulationTrial(True)
        if result:
            gamesSwitchWon += 1
        else:
            gamesSwitchLost += 1

    plt.figure(1)
    pieChart = np.array([gamesSwitchWon, gamesSwitchLost])
    plt.title('With Switching')
    plt.pie(pieChart, labels=myLabels)

    plt.show()

def SimulationTrial(shouldSwitch):
    # 0 = Goat, 1 = Car
    doors = [0, 0, 0]

    # Randomly choose a door for the car
    doorIndexWithCar = randint(0, len(doors) - 1)
    doors[doorIndexWithCar] = 1

    # Contestant chooses one door
    contestantInitialDoorChoice = randint(0, len(doors) - 1)

    # Host chooses one of the other doors (specifically the one with the goat)
    # loop through, if it is equal to the contestants door or if it is the door with the car then skip, 
    # choose the door that is both not the contestants and also has the goat
    montyDoorChoice = 0
    for i in range(0, len(doors)):
        if i == contestantInitialDoorChoice or doors[i] == 1:
            continue
        montyDoorChoice = i
        break
    
    # Contestant switches doors to the one they did not choose and the host did not reveal
    # If you take the sum of the two choices then plug that into the equation y = (-x + 3) for x, you will get the door that was not revealed. I cannot believe I figured that out.
    if shouldSwitch:
        contestantFinalDoorChoice = -(contestantInitialDoorChoice + montyDoorChoice) + 3
    else:
        contestantFinalDoorChoice = contestantInitialDoorChoice

    return contestantFinalDoorChoice == doorIndexWithCar

    # print(f'Doors: {doors}')
    # print(f'Contest initially chose: {contestantInitialDoorChoice}')
    # print(f'Monty chose: {montyDoorChoice}')
    # print(f'Contestant Final Choice: {contestantFinalDoorChoice}')
    # print(f'Contestant won car? {contestantFinalDoorChoice == doorIndexWithCar}')

numOfTrials = 5000
Simulation(numOfTrials)
