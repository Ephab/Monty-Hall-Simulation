import random

def montyHall(swap: bool, numOfDoors: int):
    prize = random.randint(0, numOfDoors - 1)
    userChoice = random.randint(0, numOfDoors - 1)

    emptyDoors = [i for i in range(numOfDoors) if i != prize and i != userChoice]
    removedDoors = random.sample(emptyDoors, numOfDoors - 2)
    remainingDoors = [i for i in range(numOfDoors) if i not in removedDoors]

    if swap:
        if userChoice == remainingDoors[0]:
            userChoice = remainingDoors[1]
        else:
            userChoice = remainingDoors[0]

    return 1 if userChoice == prize else 0

def autoRun(times: int, swap: bool, numOfDoors: int):
    wins = 0
    for _ in range(times):
        if montyHall(swap, numOfDoors) == 1:
            wins += 1
    return wins

def main():
    try:
        runTimes = int(input("How many times do you want to run the game?   "))
        numOfDoors = int(input("\nHow many doors do you want in the game?\n-(More doors means swapping has a better probability of resulting in a win)-   "))

        if runTimes < 1 or numOfDoors < 3:
            raise ValueError
        
    except ValueError:
        print("\n- Please make sure that (run times is > 1) and that (number of doors > 3) -\n")
        return

    print("After swapping we got the correct door: ", autoRun(runTimes, True, numOfDoors), " times after running", runTimes, " times")
    print("without swapping we got the correct door: ", autoRun(runTimes, False, numOfDoors), " times after running", runTimes, " times")

if __name__ == "__main__":
    main()