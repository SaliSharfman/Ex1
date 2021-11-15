from typing import Final

UP:Final = 1
LEVEL:Final = 0
DOWN:Final = -1
ERROR = -2



#UP = 1, LEVEL = 0, DOWN = -1, ERROR = -2;

class Elevator:

   def __init__(self, id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime)->None:
      self.id = id
      self.speed = speed
      self.minFloor = minFloor
      self.maxFloor = maxFloor
      self.closeTime = closeTime
      self.openTime = openTime
      self.startTime = startTime
      self.stopTime = stopTime

   def __repr__(self) -> str:
      return f"repr _id:{self.id} speed:{self.speed} minFloor:{self.minFloor} " \
             f"maxFloor:{self.maxFloor} closeTime:{self.closeTime} " \
             f"openTime:{self.openTime} startTime:{self.startTime} stopTime:{self.stopTime}"

   def getMinFloor(self)->int:
      return self.minFloor
   def getMaxFloor(self)->int:
      return self.maxFloor
   def getTimeForOpen(self)->float:
      return self.openTime
   def getTimeForClos(self)->float:
      return self.closeTime
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


   def getID(self)->int:
      return self.id
