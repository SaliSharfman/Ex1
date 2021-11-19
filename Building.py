import json

from Elevator import Elevator
#we do have list here

class Building(object):

    def __init__(self, numelevs:int):
       self.__elevators=[]
       self.__elevSize=numelevs

    #all elevators
    def getElevSize(self)->int:
        return self.__elevSize
    def getElevators(self)->list:
        return self.__elevators

    def __add__(self, other: Elevator):
        if isinstance(other, Elevator):
            return self.__elevators.append(other)

    def __str__(self):
        return self.__elevators.__str__()

    def __iter__(self):
        return iter(self.__elevators)

