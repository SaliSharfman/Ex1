from typing import Final
from CallForElevator import CallForElevator
UP: Final = 1
LEVEL: Final = 0
DOWN: Final = -1
ERROR = -2



#UP = 1, LEVEL = 0, DOWN = -1, ERROR = -2;

class Elevator:

   def __init__(self, id:int, speed:float, minFloor:int, maxFloor:int, closeTime:float, openTime:float, startTime:float, stopTime:float):
      self.__id = int(id)
      self.__speed = float(speed)
      self.__minFloor = int(minFloor)
      self.__maxFloor = int(maxFloor)
      self.__closeTime = float(closeTime)
      self.__openTime = float(openTime)
      self.__startTime = float(startTime)
      self.__stopTime = float(stopTime)
      self.__elevCalls = []
      self.__elevTime = 0

   def printTime(self):
      print(self.__elevTime)

   def getTime(self):
      return self.__elevTime

   def getCall(self, i: int):
      return self.__elevCalls[i]

   def __repr__(self) -> str:
      return f"repr _id:{self.__id} speed:{self.__speed} minFloor:{self.__minFloor} " \
             f"maxFloor:{self.__maxFloor} closeTime:{self.__closeTime} " \
             f"openTime:{self.__openTime} startTime:{self.__startTime} stopTime:{self.__stopTime} elevTime:{self.__elevTime} "
   def __str__(self)->str:
      return f"repr _id:{self.__id} speed:{self.__speed} minFloor:{self.__minFloor} " \
             f"maxFloor:{self.__maxFloor} closeTime:{self.__closeTime} " \
             f"openTime:{self.__openTime} startTime:{self.__startTime} stopTime:{self.__stopTime}"

   # def __add__(self, call: CallForElevator):
   #    if isinstance(call, CallForElevator):
   #       return self.__elevCalls.append(call)
   def __add__(self, x):
      if isinstance(x, CallForElevator):
         return self.__elevCalls.append(x)
      else:
         self.__elevTime += x
         return self


   def workTime(self, src, dest):
      worktime = self.getTimeForOpen() + self.getTimeForClos() + self.getStartTime() + self.getStopTime()
      return abs(src - dest) / self.getSpeed() + worktime

   def endCall(self, call:CallForElevator):
      time = call.get_time()
      for c in self.__elevCalls:
         if c.get_time() + self.workTime(call.get_source(), call.get_dst()) < time:
            self.__elevCalls.remove(c)
   def getMinFloor(self)->int:
      return self.__minFloor
   def getMaxFloor(self)->int:
      return self.__maxFloor
   def getTimeForOpen(self)->float:
      return self.__openTime
   def getTimeForClos(self)->float:
      return self.__closeTime
   def getCalls(self)->list:
      return self.__elevCalls
   def getSpeed(self)->float:
      return self.__speed
   def getStartTime(self)->float:
      return self.__startTime
   def getStopTime(self)->float:
      return self.__stopTime
   def getCalls(self)->list:
      return self.__elevCalls
   def getID(self)->int:
      return self.__id
