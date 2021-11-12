import json

from Elevators import Elevators


class Building(object):

    def __init__(self, file):

        self.load_json(file)

    def load_json(self, file):
        elevator_list = []
        with open(file, "r")as f:
            d = json.load(fp=f)
            self.minFloor = d["_minFloor"]
            self.maxFloor = d["_maxFloor"]
            for elev in d["_elevators"]:
                el = Elevators(id=elev["_id"], speed=elev["_speed"], minFloor=elev["_minFloor"],
                               maxFloor=elev["_maxFloor"],
                               closeTime=elev["_closeTime"], openTime=elev["_openTime"],
                               startTime=elev["_startTime"],
                               stopTime=elev["_stopTime"])
                elevator_list.append(el)
            self.elevators = elevator_list

        return self
    def getBuildingName(self)->str:
        pass
    def minFloor(self)->int:
        pass
    def maxFloor(self)->int:
        pass
    def numberOfElevator(self)->int:
        pass
    def getElevator(self)->Elevators:
        pass

