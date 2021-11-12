from typing import Final

INIT: Final = 0
GOING2SRC: Final = 1
GOIND2DEST: Final = 2
DONE: Final = 3
UP: Final = 1
DOWN: Final = -1

class CallForElevator:

    def _init_(self, name='', time=0, src=0, dst=0, x=0, allc=-1) -> None:
        self.name=name
        self.time=time
        self.src =src
        self.dst=dst
        self.x=x
        self.allc=allc

    def getState(self) -> int:
        pass
    def getTime(self) -> float:
        pass
    def getSrc(self) -> int:
        return self.src
    def getDest(self) -> int:
        return self.dst
    def getType(self) -> int:
        if (self.src>self.dst):
            return DOWN
        else:
            return UP
    def allocatedTo(self) -> int:
        pass

    def _repr_(self)->str:
        return f"{self.name} {self.time} {self.src} {self.dst} {self.x} {self.allc}\n "