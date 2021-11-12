
class CallForElevator:

    def __init__(self, name='', time=0, src=0, dst=0, x=0, allc=0) -> None:
        self.name=name
        self.time=time
        self.src =src
        self.dst=dst
        self.x=x
        self.allc=allc


    def __repr__(self)->str:
        return f":{self.name}\n time:{self.time} src:{self.src} "


