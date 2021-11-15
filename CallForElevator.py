class CallForElevator:

    def __init__(self, name='', time=0, src=0, dst=0, x=0, allc=0) -> None:
        self.name=name
        self.time=float(time)
       # print("the time is ="+str(type(self.time)))
        self.src =int(src)
        self.dst=int(dst)
        self.x=int(x)
        self.allc=int(allc)


    def __repr__(self)->str:
        return f"{self.name}  {self.time} {self.src} {self.dst} {self.x} {self.allc}\n  "
    def get_name(self)->str:
        return self.name

    def get_time(self)->float:
        return  (self.time)

    def get_source(self)->int:
        return (self.src)

    def get_dst(self)->int:
        return (self.dst)
    def get_peulot(self)->int:
        return self.x
    #be algorithm nahnis int le allocation
    #allocation of call for elevator
    def set_allc(self,allocation:int)->None:

        self.allc = allocation
        #this function is for csv
    def get_allc(self)->int:
        return self.allc
