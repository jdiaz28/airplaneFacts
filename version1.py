import flightradar24
import math
from math import *
import requests
import json
import random

def rawFlightList():
    fr = flightradar24.Api()
    airlines = fr.get_airlines()
    alaskaAirlinesCode = 'ASA'
    hawaiianAirlinesCode = 'HAL'
    southwestAirlinesCode = 'SWA'
    jetblueAirwaysCode = 'JBU'
    deltaAirlinesCode = 'DAL'
    frontierAirlinesCode = 'FFT'
    spiritAirlinesCode = 'NKS'
    americanAirlinesCode = 'AAL'
    unitedAirlinesCode = 'UAL'

    alaskaFlights = fr.get_flights(alaskaAirlinesCode)
    hawaiianFlights = fr.get_flights(hawaiianAirlinesCode)
    southwestFlights = fr.get_flights(southwestAirlinesCode)
    jetblueFlights = fr.get_flights(jetblueAirwaysCode)
    deltaFlights = fr.get_flights(deltaAirlinesCode)
    frontierFlights = fr.get_flights(frontierAirlinesCode)
    spiritFlights = fr.get_flights(spiritAirlinesCode)
    americanFlights = fr.get_flights(americanAirlinesCode)
    unitedFlights = fr.get_flights(unitedAirlinesCode)

    alaskaFlightList = []
    for i in alaskaFlights.values():
        alaskaFlightList.append(i)

    hawaiianFlightList = []
    for i in hawaiianFlights.values():
        hawaiianFlightList.append(i)

    southwestFlightList = []
    for i in southwestFlights.values():
        southwestFlightList.append(i)

    jetblueFlightList = []
    for i in jetblueFlights.values():
        jetblueFlightList.append(i)

    deltaFlightList = []
    for i in deltaFlights.values():
        deltaFlightList.append(i)

    frontierFlightList = []
    for i in frontierFlights.values():
        frontierFlightList.append(i)

    spiritFlightList = []
    for i in spiritFlights.values():
        spiritFlightList.append(i)

    americanFlightList = []
    for i in americanFlights.values():
        americanFlightList.append(i)

    unitedFlightList = []
    for i in unitedFlights.values():
        unitedFlightList.append(i)

    for x in range (0,2):
        alaskaFlightList.pop(0)
        hawaiianFlightList.pop(0)
        southwestFlightList.pop(0)
        jetblueFlightList.pop(0)
        deltaFlightList.pop(0)
        frontierFlightList.pop(0)
        spiritFlightList.pop(0)
        americanFlightList.pop(0)
        unitedFlightList.pop(0)
    alaskaFlightList.pop()
    hawaiianFlightList.pop()
    southwestFlightList.pop()
    jetblueFlightList.pop()
    deltaFlightList.pop()
    frontierFlightList.pop()
    spiritFlightList.pop()
    americanFlightList.pop()
    unitedFlightList.pop()

    finalDict = {'alaska': alaskaFlightList,'hawaiian': hawaiianFlightList, 'southwest':southwestFlightList,
                 'jetblue':jetblueFlightList, 'delta':deltaFlightList, 'frontier': frontierFlightList,
                 'spirit': spiritFlightList, 'american': americanFlightList, 'united': unitedFlightList}


    return alaskaFlightList, hawaiianFlightList, southwestFlightList, jetblueFlightList, deltaFlightList, \
           frontierFlightList, spiritFlightList, americanFlightList, unitedFlightList

def pullData(alaska, hawaiian, south, jet, delta, frontier, spirit, american, united):
    totalFlightCodes = []
    totalStartLoc = []
    totalEndLoc = []
    latY = []
    longX = []
    for e in alaska:
        totalFlightCodes.append(e[16])
        totalStartLoc.append(e[11])
        totalEndLoc.append(e[12])
        latY.append(e[1])
        longX.append(e[2])
    for e in hawaiian:
        totalFlightCodes.append(e[16])
        totalStartLoc.append(e[11])
        totalEndLoc.append(e[12])
        latY.append(e[1])
        longX.append(e[2])
    for e in south:
        totalFlightCodes.append(e[16])
        totalStartLoc.append(e[11])
        totalEndLoc.append(e[12])
        latY.append(e[1])
        longX.append(e[2])
    for e in jet:
        totalFlightCodes.append(e[16])
        totalStartLoc.append(e[11])
        totalEndLoc.append(e[12])
        latY.append(e[1])
        longX.append(e[2])
    for e in delta:
        totalFlightCodes.append(e[16])
        totalStartLoc.append(e[11])
        totalEndLoc.append(e[12])
        latY.append(e[1])
        longX.append(e[2])
    for e in frontier:
        totalFlightCodes.append(e[16])
        totalStartLoc.append(e[11])
        totalEndLoc.append(e[12])
        latY.append(e[1])
        longX.append(e[2])
    for e in spirit:
        totalFlightCodes.append(e[16])
        totalStartLoc.append(e[11])
        totalEndLoc.append(e[12])
        latY.append(e[1])
        longX.append(e[2])
    for e in american:
        totalFlightCodes.append(e[16])
        totalStartLoc.append(e[11])
        totalEndLoc.append(e[12])
        latY.append(e[1])
        longX.append(e[2])
    for e in united:
        totalFlightCodes.append(e[16])
        totalStartLoc.append(e[11])
        totalEndLoc.append(e[12])
        latY.append(e[1])
        longX.append(e[2])

    return totalFlightCodes, totalStartLoc, totalEndLoc, latY, longX

def calcDistance(y1,x1,y2,x2):
    #distance = math.hypot(x2 - x1,y2 - y1)

    """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees)
        """
    # convert decimal degrees to radians
    y1, x1, y2, x2 = map(radians, [y1, x1, y2, x2])

    # haversine formula
    dlon = y2 - y1
    dlat = x2 - x1
    a = sin(dlat / 2) ** 2 + cos(x1) * cos(x2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r

def findLocation():
    ipInformation = 'http://api.ipstack.com/check?access_key=5bcf499c57462858a9bea4eb407267d6&format=1'
    r = requests.get(ipInformation)
    j = json.loads(r.text)
    lat = j['latitude']
    long = j['longitude']
    city = j['city']
    state = j['region_name']
    return lat, long, city, state

def findRandomPlane(planeLat, planeLong):
    randomPlane = random.randint(1,len(planeLat))
    planeLatX = planeLat[randomPlane]
    planeLongY = planeLong[randomPlane]
    return planeLatX, planeLongY


def startCount(allLocations, userAirport):
    location = userAirport
    ourlist = []
    for x in range(0,len(allLocations)):
        if (allLocations[x] == location):
            ourlist.append(x)
    return len(ourlist)

def endCount(allEndLocations, userArrivalAirport):
    newList = []
    endLocation = userArrivalAirport
    for x in range(0,len(allEndLocations)):
        if(allEndLocations[x] == endLocation):
            newList.append(x)
    return len(newList)

def guessAirport():
    w,x,y,state = findLocation()
    airportDict = {
        "Alabama":"BHM",
        "Alaska":"ANC",
        "Arizona":"PHX",
        "Arkansas":"LIT",
        "California":"LAX",
        "Colorado":"DEN",
        "Connecticut":"BDL",
        "Delaware":"ILG",
        "Florida": "MIA",
        "Georgia": "ATL",
        "Hawaii": "HNL",
        "Idaho": "BOI",
        "Illinois": "ORD",
        "Indiana": "IND",
        "Iowa": "DSM",
        "Kansas": "ICT",
        "Kentucky": "CVG",
        "Louisiana": "MSY",
        "Maine": "PWM",
        "Maryland": "BWI",
        "Massachusetts": "BOS",
        "Michigan": "DTW",
        "Minnesota": "MSP",
        "Mississippi": "JAN",
        "Missouri": "MCI",
        "Montana": "BIL",
        "Nebraska": "OMA",
        "Nevada": "LAS",
        "New Hampshire": "MHT",
        "New Jersey": "EWR",
        "New Mexico": "ABQ",
        "New York": "JFK",
        "North Carolina": "CLT",
        "North Dakota": "FAR",
        "Ohio": "CLE",
        "Oklahoma": "OKC",
        "Oregon": "PDX",
        "Pennsylvania": "PHL",
        "Rhode Island": "PVD",
        "South Carolina": "CHS",
        "South Dakota": "FSD",
        "Tennessee": "BNA",
        "Texas": "DFW",
        "Utah": "SLC",
        "Vermont": "BTV",
        "Virginia": "DCA",
        "Washington": "SEA",
        "West Virginia": "CRW",
        "Wisconsin": "MKE",
        "Wyoming": "JAC",
    }
    guess = airportDict.get(state)
    return guess



#here are our list, now we need to pull info
totalAlaska, totalHawaiian, totalSouth, totalJet, totalDelta, totalFrontier, totalSpirit, totalAmerican, totalUnited = \
    rawFlightList()
#now we have the codes, where they start, end, latitude, and longitude
flightCodes, startLocations, endLocations, y, x = pullData(totalAlaska, totalHawaiian, totalSouth, totalJet, totalDelta,
                                            totalFrontier,
                               totalSpirit, totalAmerican,
         totalUnited)
# print(len(flightCodes))
# print(len(startLocations))
# print(len(endLocations))
# print(y[0])
# print(x[0])
# print(flightCodes[0])
print("Welcome to Plane Factuals!")
print("Here, using real flight data, you can learn all kinds of airplane facts!")
print("Look at all of the stuff you can do!")
print("1. How many flights from the 9 biggest US airlines are there in the air right now?\n2. How far am I from a "
      "random airplane?\n3. How many planes are leaving from my city?\n4. How many planes are coming to my city?\n5. ("
      "BETA) How many planes are leaving from my city?\n6. (BETA) How many planes are coming to my city?")
print("Type the number and hit enter to select that option.")
choice = int(input("I choose: "))
if (choice == 1):
    print(len(flightCodes))
elif (choice == 2):
    userLat, userLong , userCity, userState = findLocation()
    planeLat, planeLong = findRandomPlane(y, x)
    print("Mhmmm...")
    print("I see you are located in " + userCity + ", " + userState)
    print("A random plane is about " + str(calcDistance(planeLat, planeLong, userLat, userLong)) + " kilometers near "
                                                                                                   "you "
                                                                                                   "at "
                                                                                              "this very moment!")
elif (choice == 3):
    print("Please enter your airport code, for example if you are in Atlanta, Atlanta Hartsfield-Jackson's airport "
          "code is ATL.")
    location = input("Airport Code: ")
    print("From your airport there are only about " + str(startCount(startLocations, location)) + " airplanes set to "
                                                                                                  "leave!")
elif (choice == 4):
    print("Please enter your airport code, for example if you are in Atlanta, Atlanta Hartsfield-Jackson's airport "
          "code is ATL.")
    endLocation = input("Airport Code: ")
    print("To your airport there are only about " + str(endCount(endLocations, endLocation)) + " airplanes set to "
                                                                                               "arrive!")
elif (choice == 5):
    print("This is a BETA version of choice 3. In this version, you do not have to enter your airport code, "
          "instead I will guess the airport you were likely to choose.")
    print("Disclaimer: I pick the largest/busiest airport in your state, not the closest in proximity to you.")
    print("I think your airport code is: " + guessAirport())
    print("From your airport there are only about " + str(startCount(startLocations, guessAirport())) + " airplanes "
                                                                                                        "set "
                                                                                                     "to "
                                                                                                  "leave!")
elif (choice == 6):
    print("This is a BETA version of choice 3. In this version, you do not have to enter your airport code, "
          "instead I will guess the airport you were likely to choose.")
    print("Disclaimer: I pick the largest/busiest airport in your state, not the closest in proximity to you.")
    print("I think your airport code is: " + guessAirport())
    print("To your airport there are only about " + str(endCount(endLocations, guessAirport())) + " airplanes set to "
                                                                                               "arrive!")
else:
    print('Mhmm, please try again mister "I didn\'t read the instructions"')

