# Rny8's MSFS2020 Plane chooser


import random
class plane:
    def __init__(self, name, speed, mileage, type, id):
        self.name = name
        self.speed = speed
        self.mileage = mileage
        self.type = type
        self.id = id

class planes:
    def __init__(self):
        self.planes = self.planeList()
    
    def getPlane(self, chosenPlane):
        for plane in self.planes:
            if plane.id == chosenPlane:
                return plane
    
    planeList = [
        plane("Cessna 152", 126, 415, 1, 1),
        plane("Cessna 172", 163, 639, 1, 2),
        plane("Bonanza G36", 176, 920, 1, 3),
        plane("Test", 5000, 5000, 3, 4)
    ]
        
def game():
    print("Welcome to this stupid ass pointless plane chooser!\n")
    aircraftType = input("What type of aircraft would you like? Please enter the number corresponding with the type of aircraft! \n 1: Propellor \n 2: Jet \n 3: Rotary \n 4: Any \n Input: ")
    aircraftRange = input("Perfect! Now how far would you like to fly?(input must be NUMBERS only): ")
    possibleAircraft = []
    for plane in planes.planeList:
        if plane.mileage >= int(aircraftRange):
            if plane.type == int(aircraftType):
                possibleAircraft.append(plane)
    randomNumber = random.randint(0, len(possibleAircraft))
    if len(possibleAircraft) == 0:
        print("No aircraft found! Please retry with new requirements\n")
        game()
    print(f"Chosen aircraft is: {possibleAircraft[randomNumber].name}\n Range is: {possibleAircraft[randomNumber].mileage}\n Speed: {possibleAircraft[randomNumber].speed}\n")
    
    game()

game()