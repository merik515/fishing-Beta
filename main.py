#fishing beta
import random
import time
from colorama import Fore
import replit




def clear_console():
  """Clears the console."""
  # os.system("clear")
  # print("\r\x1Bc\r")
  replit.clear()
#clears screen

Lake = {
    "Fish":["Bass","Walleye","Crappie","Perch","Nessie"],
    "Odds":[700,600,900,600,1]
}

Ocean = {
  "Fish":["???","Salmon","Grouper","Mahi-mahi","Bluefin Tuna","Shark",f"{Fore.WHITE}a {Fore.RED}Colossal squid"],
  "Odds":[1,500,600,400,50,100,3]
}
River = {
  "Fish":["Bass","Pike","Catfish","Bluegill","Trout"],
  "Odds":[600,500,300,900,400]
}
#list of fish in different places (unfinished)



def fishingspot(str):
    caught = ""
    points = 0
    print("starting fishing at the "+str+"...")
    time.sleep(random.randint(1,3))
    if random.random() < .5:
      if str == "Lake":
        caught = random.choices(Lake["Fish"],Lake["Odds"])[0]
        points = random.choices(fish[caught]["Range_weight"], weights = fish[caught]["Weights"])[0]
      elif str == "Ocean":
        caught = random.choices(Ocean["Fish"],Ocean["Odds"])[0]
        points = random.choices(fish[caught]["Range_weight"], weights = fish[caught]["Weights"])[0]
      elif str == "River":
        caught = random.choices(River["Fish"],River["Odds"])[0]
        points = random.choices(fish[caught]["Range_weight"], weights = fish[caught]["Weights"])[0]
      if fish[caught]["Color"] == Fore.RED:
        print(f"You caught {fish[caught]['Color']}{caught}{Fore.WHITE} and earned {Fore.YELLOW}{points}{Fore.WHITE} points!")
      else:
        print(f"You caught a {fish[caught]['Color']}{caught}{Fore.WHITE} and earned {Fore.YELLOW}{points}{Fore.WHITE} points!")
    else:
      print("You didn\"t catch anything :(")
    return points
#this code decides if you caught a fish and what fish you caught and how many points it is worth.

options = ["OCEAN","RIVER","LAKE","L","O","R"]
# defines all possible allowed inputs for location

fish = {
"Bass":{"Range_weight":[1,2,3,4,5,6,7,8,9,10], "Weights":[10,9,8,7,6,5,4,3,2,1],"Color":Fore.GREEN},
"Salmon":{"Range_weight":list(range(5,21)),"Weights": list(range(21,5,-1)), "Color":Fore.GREEN},
"Pike":{"Range_weight":list(range(3,13)),"Weights":list(range(13,3,-1)),"Color":Fore.GREEN},
"???":{"Range_weight":list(range(200,5000)),"Weights":list(range(5000,200,-1)),"Color":Fore.RED},
"Catfish":{"Range_weight":list(range(5,26)),"Weights":list(range(26,5,-1)),"Color":Fore.BLUE},
"Crappie":{"Range_weight":list(range(1,3)),"Weights":list(range(3,1,-1)),"Color":Fore.GREEN},
"Walleye":{"Range_weight":list(range(3,13)),"Weights":list(range(13,3,-1)),"Color":Fore.GREEN},
"Perch":{"Range_weight":list(range(1,9)),"Weights":list(range(9,1,-1)),"Color":Fore.GREEN},
"Bluegill":{"Range_weight":list(range(1,3)),"Weights":list(range(3,1,-1)),"Color":Fore.GREEN},
"Trout":{"Range_weight":list(range(7,16)),"Weights":list(range(16,7,-1)),"Color":Fore.BLUE},
"Nessie":{"Range_weight":list(range(200,501)),"Weights":list(range(501,200,-1)),"Color":Fore.RED},
"Grouper":{"Range_weight":list(range(5,16)),"Weights":list(range(16,5,-1)),"Color":Fore.GREEN},
"Mahi-mahi":{"Range_weight":list(range(10,31)),"Weights":list(range(31,10,-1)),"Color":Fore.BLUE},
"Bluefin Tuna":{"Range_weight":list(range(50,201)),"Weights":list(range(201,50,-1)),"Color":Fore.MAGENTA},
"Shark":{"Range_weight":list(range(30,71)),"Weights":list(range(71,30,-1)),"Color":Fore.MAGENTA},
f"{Fore.WHITE}a {Fore.RED}Colossal squid":{"Range_weight":list(range(200,601)),"Weights":list(range(601,200,-1)),"Color":Fore.RED}
}
  # list of all fish and all needed info
running = True
main = True
total_points = 0
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
        total_points = total_points + fishingspot(place)
        print(f"Your total number of points is {total_points}!")
  if place != None:
    restart = input("would you like to continue fishing? Yes(Y), No(N) ").upper()
    if restart == "Y":
      total_points = total_points + fishingspot(place)
      print(f"Your total number of points is {total_points}!")
    elif restart == "YES":
      total_points = total_points + fishingspot(place)
      print(f"Your total number of points is {total_points}!")
    elif restart == "N":
      main = True
    elif restart == "NO":
      main = True
    else:
      print("Not a valid option")
# this is the "main menu" of the code where the user decides where they want to go.
