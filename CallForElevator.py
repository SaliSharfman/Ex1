class CallForElevator:

    def __init__(self, time:float, src:int, dst:int):
        self.time=float(time)
        self.src =int(src)
        self.dst=int(dst)
        self.allc=-1
    def __repr__(self)->str:
        return f"{self.name}  {self.time} {self.src} {self.dst} {self.x} {self.allc}\n  "

    def __str__(self) -> str:
        return f"{self.name}  {self.time} {self.src} {self.dst} {self.x} {self.allc}\n  "

    def get_time(self)->float:
        return  (self.time)

    def get_source(self)->int:
        return (self.src)

    def get_dst(self)->int:
        return (self.dst)
    #be algorithm nahnis int le allocation
    #allocation of call for elevator
    def set_allc(self,allocation:int)->None:
        self.allc = allocation
        #this function is for csv
    def get_allc(self)->int:
        return self.allc
