from Building import Building
from CallForElevator import CallForElevator
from Calls_List import Calls_List
from Elevator import Elevator
import json
import csv
import sys


def timeForCall(src: int, dst: int, elev: Elevator):
    """
    Calculates and returns how much time takes to the Elevator to do the call
    @param src: source
    @param dst: destination
    @param elev: elevator
    @returns (float)time for call on Elevator elev:
    """
    return ((abs(dst - src)) / elev.getSpeed()) + elev.getTimeForOpen() + elev.getTimeForClos() + elev.getStartTime() + elev.getStopTime()


def LoadBuildingFromJson(building: str) -> Building:
    """
    Loads data from Json and crates class of Building and its elevators
    Each elevator in building is type of a class Elevator
    @param building: Json name of the building
    @returns: Building
    """
    with open(building, 'r') as building:
        building_dict = json.load(building)

    b = Building(len(building_dict["_elevators"]))
    elevators = building_dict.get("_elevators")

    for el in elevators:
        elev = Elevator(el["_id"],
                        el["_speed"],
                        el["_minFloor"],
                        el["_maxFloor"],
                        el["_closeTime"],
                        el["_openTime"],
                        el["_startTime"],
                        el["_stopTime"])
        b + elev  # Add an Elevator to Building using an operator '+' that we created in class Building
    return b


def GetCsvRows(call: str) -> list:
    with open(call, 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)
        return calls


def LoadCallsFromCsv(ca: str) -> Calls_List:
    all_calls = GetCsvRows(ca)
    calls = Calls_List()
    for c in all_calls:
        call_list = c
        call = CallForElevator(call_list[1], call_list[2], call_list[3])
        calls + call
    return calls



def allocateAnElevsToCalls(b: str, ca: str, output: str):
    building = LoadBuildingFromJson(b)
    elevators = building.getElevators()
    rows = GetCsvRows(ca)
    calls = LoadCallsFromCsv(ca)
    for c in calls:
        time = 999999
        elev_index = -1
        for e in building:
            if len(e.getCalls()) == 0:
                min_time = timeForCall(c.get_source(), c.get_dst(), e)
            else:

                min_time = timeForCall(c.get_source(), c.get_dst(), e) * len(e.getCalls())
                #min_time += e.getTime()

            if min_time < time:
                time = min_time
                elev_index = e.getID()
        c.set_allc(elevators[elev_index].getID())

        elevators[elev_index] + c  # Add call to Elevators's list using an operator '+' that we created
        elevators[elev_index] + time
        # print(elev_index)
        # elevators[elev_index].printTime()



    for e in building:
        e.printTime()

    rows_counter = 0
    for row in rows:
        row[5] = calls.getCalls()[rows_counter].get_allc()
        rows_counter += 1
    with open(output, 'w', newline="") as f:
        for row in rows:
            writer = csv.writer(f)
            writer.writerow(row)




if __name__ == '__main__':

    allocateAnElevsToCalls(str(sys[1]), str(sys[2]), str(sys[3]))


