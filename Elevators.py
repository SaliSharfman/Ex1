from typing import Final



#UP = 1, LEVEL = 0, DOWN = -1, ERROR = -2;

class Elevators:

   def __init__(self, id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime)->None:
      self.id = id
      self.speed = speed
      self.minFloor = minFloor
      self.maxFloor = maxFloor
      self.closeTime = closeTime
      self.openTime = openTime
      self.stopTime = stopTime

   def _repr_(self) -> str:
      return f"repr _id:{self.id} speed:{self.speed} minFloor:{self.minFloor} " \
             f"maxFloor:{self.maxFloor} closeTime:{self.closeTime} " \
             f"openTime:{self.openTime} startTime:{self.stopTime} stopTime:{self.stopTime}"