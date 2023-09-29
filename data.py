import csv
import copy

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

myInventoryList = []

with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ',')

    for row in list(csvReader)[1:]:
        currentVehicle = copy.deepcopy(myVehicle)
        currentVehicle["vin"] = row[0]  
        currentVehicle["make"] = row[1]  
        currentVehicle["model"] = row[2]  
        currentVehicle["year"] = row[3]  
        currentVehicle["range"] = row[4]  
        currentVehicle["topSpeed"] = row[5]  
        currentVehicle["zeroSixty"] = row[6]  
        currentVehicle["mileage"] = row[7]  
        myInventoryList.append(currentVehicle)



for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{}: {}".format(key, value))
        print("-----")
        