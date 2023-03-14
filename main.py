# fishing beta
import random
import time
from colorama import Fore
import replit


def clear_console():
    """Clears the console."""
    # os.system('clear')
    # print("\r\x1Bc\r")
    replit.clear()


# clears screen

Lake = ["Bass"]

Ocean = ["Salmon"]

River = ["Bass"]
# list of fish in different places (unfinished)

Salmon_weight = []
for i in range(5, 21):
    Salmon_weight.append(i)
# all possible salmon weights


def fishingspot(str):
    caught = ""
    points = ""
    print("starting fishing at the " + str + "...")
    time.sleep(random.randint(1, 3))
    if random.random() < 0.5:
        if str == "Lake":
            caught = random.choices(Lake)
            points = random.choices(
                fish[caught]["Range_weight"], weights=fish[caught]["Weights"]
            )[0]
        if str == "Ocean":
            caught = random.choices(Ocean)
            points = random.choices(
                fish[caught]["Range_weight"], weights=fish[caught]["Weights"]
            )[0]
        if str == "River":
            caught = random.choices(River)
            points = random.choices(
                fish[caught]["Range_weight"], weights=fish[caught]["Weights"]
            )[0]
    print("Testing!", caught, "  ", points)


# this code decides if you caught a fish and what fish you caught and how many points it is worth.

options = ["OCEAN", "RIVER", "LAKE", "L", "O", "R"]
# defines all possible allowed inputs for location

fish = {
    "Bass": {
        "Range_weight": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Weights": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    },
    "Salmon": {
        "Range_weight": Salmon_weight,
        "Weights": [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    },
}
# list of all fish and all needed info

running = True
main = True
while running == True:
    if main == True:
        place = input("Choose a location to fish: River(R), Lake(L), Ocean(O) ").upper()
        if place in options:
            if place == "RIVER" or place == "R":
                place = "River"
            elif place == "OCEAN" or place == "O":
                place = "Ocean"
            elif place == "LAKE" or place == "L":
                place = "Lake"
            main = False
        else:
            print("Not a valid option")
            place = None
        if place != None:
            fishingspot(place)
    main = True
    # this is the "main menu" of the code where the user decides where they want to go
