from Building import Building
from CallForElevator import CallForElevator
# all info is here
from Calls_List import Calls_List
from Elevator import Elevator
import json
import csv
import sys

def TimeForThatCall(src: int, dst: int, elev: Elevator):
    return ((abs(dst - src)) / elev.getSpeed()) + elev.getTimeForOpen() + elev.getTimeForClos() + elev.getStartTime() + elev.getStopTime()


def LoadBuildingFromJson(building: str) -> Building:
    with open(building, 'r') as building:
        building_dict = json.load(building)
    b = Building(len(building_dict["_elevators"]))
    elevators = building_dict.get("_elevators")
    for el in elevators:
        elev = Elevator(el["_id"], el["_speed"], el["_minFloor"], el["_maxFloor"], el["_closeTime"], el["_openTime"],
                        el["_startTime"], el["_stopTime"])
        b + elev
    return b

def GetCsvRows(call:str)->list:
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


def allocate_an_elevator(b: str, ca: str, output: str):
    building = LoadBuildingFromJson(b)
    elevators = building.getElevators()
    rows = GetCsvRows(ca)
    calls = LoadCallsFromCsv(ca)
    for c in calls:
        algo_time = int(calls.getCalls()[-1].get_time()+120)+1
        elev_index = -1
        for e in building:
            if len(e.getCalls()) == 0:
                min_time = TimeForThatCall(c.get_source(), c.get_dst(), e)
            else:
                min_time = TimeForThatCall(c.get_source(), c.get_dst(), e) * len(e.getCalls())
            if min_time < algo_time:
                algo_time = min_time
                elev_index = e.getID()
        c.set_allc(elevators[elev_index].getID())
        elevators[elev_index] + c

    rows_counter = 0
    for row in rows:
        row[5] = calls.getCalls()[rows_counter].get_allc()
        rows_counter += 1
    with open(output, 'w', newline="") as f:
        for row in rows:
            writer = csv.writer(f)
            writer.writerow(row)


if __name__ == '__main__':

    l = sys.argv
    allocate_an_elevator(str(l[1]), str(l[2]), str(l[3]))


