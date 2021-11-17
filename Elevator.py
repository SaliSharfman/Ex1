from typing import Final
from CallForElevator import CallForElevator
UP:Final = 1
LEVEL:Final = 0
DOWN:Final = -1
ERROR = -2



#UP = 1, LEVEL = 0, DOWN = -1, ERROR = -2;

class Elevator:

   def __init__(self, id:int, speed:float, minFloor:int, maxFloor:int, closeTime:float, openTime:float, startTime:float, stopTime:float):
      self.id = int(id)
      self.speed = float(speed)
      self.minFloor = int(minFloor)
      self.maxFloor = int(maxFloor)
      self.closeTime = float(closeTime)
      self.openTime = float(openTime)
      self.startTime = float(startTime)
      self.stopTime = float(stopTime)
      self.elevCalls = []

   def __repr__(self) -> str:
      return f"repr _id:{self.id} speed:{self.speed} minFloor:{self.minFloor} " \
             f"maxFloor:{self.maxFloor} closeTime:{self.closeTime} " \
             f"openTime:{self.openTime} startTime:{self.startTime} stopTime:{self.stopTime}"
   def __str__(self)->str:
      return f"repr _id:{self.id} speed:{self.speed} minFloor:{self.minFloor} " \
             f"maxFloor:{self.maxFloor} closeTime:{self.closeTime} " \
             f"openTime:{self.openTime} startTime:{self.startTime} stopTime:{self.stopTime}"

   def __add__(self, other: CallForElevator):
      if isinstance(other, CallForElevator):
         return self.elevCalls.append(other)

   def workTime(self, src, dest):
      worktime = self.getTimeForOpen() + self.getTimeForClos() + self.getStartTime() + self.getStopTime()
      return abs(src - dest) / self.getSpeed() + worktime

   def endCall(self, call:CallForElevator):
      time = call.get_time()
      for c in self.elevCalls:
         if c.get_time() + self.workTime(call.get_source(), call.get_dst()) < time:
            self.elevCalls.remove(c)
   def getMinFloor(self)->int:
      return self.minFloor
   def getMaxFloor(self)->int:
      return self.maxFloor
   def getTimeForOpen(self)->float:
      return self.openTime
   def getTimeForClos(self)->float:
      return self.closeTime
   def getCalls(self)->list:
      return self.elevCalls
   def getState(self)->int:
      pass
   def goTo(self)->bool:
      pass
   def stop(self)->bool:
      pass
   def getSpeed(self)->float:
      return self.speed
   def getStartTime(self)->float:
      return self.startTime
   def getStopTime(self)->float:
      return self.stopTime
   def getCalls(self)->list:
      return self.elevCalls
   def getID(self)->int:
      return self.id
