import json

from Elevator import Elevator
#we do have list here

class Building(object):

    def __init__(self, numelevs:int):
       self.elevators=[]
       self.elevSize=numelevs



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


    #all elevators
    def getElevSize(self)->int:
        return self.elevSize
    def getElevators(self)->list:
        return self.elevators

    def __add__(self, other: Elevator):
        if isinstance(other, Elevator):
            return self.elevators.append(other)

    def __str__(self):
        return self.elevators.__str__()

    def __iter__(self):
        return iter(self.elevators)

