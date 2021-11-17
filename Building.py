import json

from Elevator import Elevator
#we do have list here

class Building(object):

    def __init__(self, numelevs:int):
       self.elevators=[]
       self.elevSize=numelevs
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

