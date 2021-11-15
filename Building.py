import json

from Elevator import Elevator


class Building(object):

    def __init__(self, file):
        self.buildingname = file

        self.load_json(file)




    def load_json(self, file) ->None:

        elevator_list = []
        with open(file, "r")as f:
            d = json.load(f)

            self.minFloor = d["_minFloor"]
            self.maxFloor = d["_maxFloor"]
            self.elevSize = len(d["_elevators"])

            for elev in d["_elevators"]:


                el = Elevator(id=elev["_id"], speed=elev["_speed"], minFloor=elev["_minFloor"],
                               maxFloor=elev["_maxFloor"],
                               closeTime=elev["_closeTime"], openTime=elev["_openTime"],
                               startTime=elev["_startTime"],
                               stopTime=elev["_stopTime"])
                elevator_list.append(el)
                #caunt_elev = caunt_elev + 1
            self.elevators = elevator_list
            f.close()


    def getBuildingName(self)->str:
        return self.buildingname
    def minFloor(self)->int:
        pass
    def maxFloor(self)->int:
        pass
    def numberOfElevator(self)->int:

        pass
    #all elevators
    def ElevSize(self):
        return len(self.elevators)

    def getElevator(self,place)->Elevator:
        return self.elevators[place]

