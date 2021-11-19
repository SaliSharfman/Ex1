class CallForElevator:

    def __init__(self, time:float, src:int, dst:int):
        self.__time=float(time)
        self.__src =int(src)
        self.__dst=int(dst)
        self.__allc=-1

    def __repr__(self)->str:
        return f"{self.name}  {self.__time} {self.__src} {self.__dst} {self.x} {self.__allc}\n  "

    def __str__(self) -> str:
        return f"{self.name}  {self.__time} {self.__src} {self.__dst} {self.x} {self.__allc}\n  "

    def get_time(self)->float:
        return  (self.__time)

    def get_source(self)->int:
        return (self.__src)

    def get_dst(self)->int:
        return (self.__dst)
    #be algorithm nahnis int le allocation
    #allocation of call for elevator
    def set_allc(self,allocation:int)->None:
        self.__allc = allocation
        #this function is for csv
    def get_allc(self)->int:
        return self.__allc
