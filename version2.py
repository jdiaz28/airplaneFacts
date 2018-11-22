import flightradar24
import math
from math import *
import requests
import json
import random
import time
import timeit

start = timeit.default_timer()

def rawFlightList():
    fr = flightradar24.Api()
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
    alaskaHeaders = []
    for i in alaskaFlights:
        alaskaHeaders.append(i)
    alaskaHeaders.pop()
    alaskaHeaders.pop(0)
    alaskaHeaders.pop(0)

    alaskaData = []
    for x in range(len(alaskaHeaders)):
        alaskaData.append(alaskaFlights[alaskaHeaders[x]])

    hawaiiFlights = fr.get_flights(hawaiianAirlinesCode)
    hawaiiHeaders = []
    for i in hawaiiFlights:
        hawaiiHeaders.append(i)
    hawaiiHeaders.pop()
    hawaiiHeaders.pop(0)
    hawaiiHeaders.pop(0)

    hawaiiData = []
    for x in range(len(hawaiiHeaders)):
        hawaiiData.append(hawaiiFlights[hawaiiHeaders[x]])

    southewestFlights = fr.get_flights(southwestAirlinesCode)
    southwestHeaders = []
    for i in southewestFlights:
        southwestHeaders.append(i)
    southwestHeaders.pop()
    southwestHeaders.pop(0)
    southwestHeaders.pop(0)

    southwestData = []
    for x in range(len(southwestHeaders)):
        southwestData.append(southewestFlights[southwestHeaders[x]])

    jetblueFlights = fr.get_flights(jetblueAirwaysCode)
    jetblueHeaders = []
    for i in jetblueFlights:
        jetblueHeaders.append(i)
    jetblueHeaders.pop()
    jetblueHeaders.pop(0)
    jetblueHeaders.pop(0)

    jetblueData = []
    for x in range(len(jetblueHeaders)):
        jetblueData.append(jetblueFlights[jetblueHeaders[x]])

    deltaFlights = fr.get_flights(deltaAirlinesCode)
    deltaHeaders = []
    for i in deltaFlights:
        deltaHeaders.append(i)
    deltaHeaders.pop()
    deltaHeaders.pop(0)
    deltaHeaders.pop(0)

    deltaData = []
    for x in range(len(deltaHeaders)):
        deltaData.append(deltaFlights[deltaHeaders[x]])

    frontierFlights = fr.get_flights(frontierAirlinesCode)
    frontierHeaders = []
    for i in frontierFlights:
        frontierHeaders.append(i)
    frontierHeaders.pop()
    frontierHeaders.pop(0)
    frontierHeaders.pop(0)

    frontierData = []
    for x in range(len(frontierData)):
        frontierData.append(frontierFlights[frontierHeaders[x]])

    spiritFlights = fr.get_flights(spiritAirlinesCode)
    spiritHeaders = []
    for i in spiritFlights:
        spiritHeaders.append(i)
    spiritHeaders.pop()
    spiritHeaders.pop(0)
    spiritHeaders.pop(0)

    spiritData = []
    for x in range(len(spiritHeaders)):
        spiritData.append(spiritFlights[spiritHeaders[x]])

    americanFlights = fr.get_flights(americanAirlinesCode)
    americanHeaders = []
    for i in americanFlights:
        americanHeaders.append(i)
    americanHeaders.pop()
    americanHeaders.pop(0)
    americanHeaders.pop(0)

    americanData = []
    for x in range(len(americanHeaders)):
        americanData.append(americanFlights[americanHeaders[x]])

    unitedFlights = fr.get_flights(unitedAirlinesCode)
    unitedHeaders = []
    for i in unitedFlights:
        unitedHeaders.append(i)
    unitedHeaders.pop()
    unitedHeaders.pop(0)
    unitedHeaders.pop(0)

    unitedData = []
    for x in range(len(unitedHeaders)):
        unitedData.append(unitedFlights[unitedHeaders[x]])




    return alaskaData, hawaiiData, southwestData, jetblueData, deltaData, frontierData, spiritData, americanData, unitedData

def pullData(alaska, hawaii, southwest, jetblue, delta, frontier, spirit, american, united):
    totalFlightCodes = []
    totalStartLoc = []
    totalEndLoc = []
    latY = []
    longX = []

    for x in range(len(alaska)):
        totalFlightCodes.append(alaska[x][16])
        totalStartLoc.append(alaska[x][11])
        totalEndLoc.append(alaska[x][12])
        latY.append(alaska[x][1])
        longX.append(alaska[x][2])

    for x in range(len(hawaii)):
        totalFlightCodes.append(hawaii[x][16])
        totalStartLoc.append(hawaii[x][11])
        totalEndLoc.append(hawaii[x][12])
        latY.append(hawaii[x][1])
        longX.append(hawaii[x][2])

    for x in range(len(southwest)):
        totalFlightCodes.append(southwest[x][16])
        totalStartLoc.append(southwest[x][11])
        totalEndLoc.append(southwest[x][12])
        latY.append(southwest[x][1])
        longX.append(southwest[x][2])

    for x in range(len(jetblue)):
        totalFlightCodes.append(jetblue[x][16])
        totalStartLoc.append(jetblue[x][11])
        totalEndLoc.append(jetblue[x][12])
        latY.append(jetblue[x][1])
        longX.append(jetblue[x][2])

    for x in range(len(delta)):
        totalFlightCodes.append(delta[x][16])
        totalStartLoc.append(delta[x][11])
        totalEndLoc.append(delta[x][12])
        latY.append(delta[x][1])
        longX.append(delta[x][2])

    for x in range(len(frontier)):
        totalFlightCodes.append(frontier[x][16])
        totalStartLoc.append(frontier[x][11])
        totalEndLoc.append(frontier[x][12])
        latY.append(frontier[x][1])
        longX.append(frontier[x][2])

    for x in range(len(spirit)):
        totalFlightCodes.append(spirit[x][16])
        totalStartLoc.append(spirit[x][11])
        totalEndLoc.append(spirit[x][12])
        latY.append(spirit[x][1])
        longX.append(spirit[x][2])

    for x in range(len(american)):
        totalFlightCodes.append(american[x][16])
        totalStartLoc.append(american[x][11])
        totalEndLoc.append(american[x][12])
        latY.append(american[x][1])
        longX.append(american[x][2])

    for x in range(len(united)):
        totalFlightCodes.append(united[x][16])
        totalStartLoc.append(united[x][11])
        totalEndLoc.append(united[x][12])
        latY.append(united[x][1])
        longX.append(united[x][2])






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
    #using api.ipstak.com to find location data from the users IP address
    #place your personal api key here
    apiKey = '5bcf499c57462858a9bea4eb407267d6'
    ipInformation = 'http://api.ipstack.com/check?access_key=' + apiKey + '&format=1'
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

def totalData():
    print("gathering all data")
    keys = ['flightCode','startLocation','endLocation','latitude','longitude']
    flightCodes, startLocations, endLocations, latitude, longitude = pullData(totalAlaska, totalHawaiian, totalSouth,
                                                                        totalJet,
                                                               totalDelta,
                                                               totalFrontier,
                                                               totalSpirit, totalAmerican,
                                                               totalUnited)
    values = [flightCodes, startLocations, endLocations, latitude, longitude]
    dictionary = dict(zip(keys,values))
    print(dictionary)
    print(dictionary['flightCode'])

    everything = []
    for x in range(0,len(flightCodes)):
        everything.append(flightCodes[x])
        everything.append(startLocations[x])
        everything.append(endLocations[x])
        everything.append(latitude[x])
        everything.append(longitude[x])
    print(everything)






rawAlaska, rawHawaii, rawSouthwest, rawJetblue, rawDelta, rawFrontier, rawSpirit, rawAmerican, rawUnited = rawFlightList()

#now we have the codes, where they start, end, latitude, and longitude
flightCodes, startLocations, endLocations, y, x = pullData(rawAlaska, rawHawaii, rawSouthwest, rawJetblue, rawDelta, rawFrontier, rawSpirit, rawAmerican, rawUnited)






print("Welcome to Plane Factuals!")
print("Here, using real flight data, you can learn all kinds of airplane facts!")
print("Look at all of the stuff you can do!")
print("1. How many flights from the 9 biggest US airlines are there in the air right now?\n2. How far am I from a "
      "random airplane?\n3. How many planes are leaving from my city?\n4. How many planes are coming to my city?\n5. ("
      "BETA) How many planes are leaving from my city?\n6. (BETA) How many planes are coming to my city?")
print("Type the number and hit enter to select that option.")

stop = timeit.default_timer()
loadingTime = stop - start

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

elif (choice == 7):
    print("Loading time is: " + str(loadingTime))
else:
    print('Mhmm, please try again mister "I didn\'t read the instructions"')
