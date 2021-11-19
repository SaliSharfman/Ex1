from CallForElevator import CallForElevator

class Calls_List:

    def __init__(self):
        self.__callsList=[]

    def __add__(self, other: CallForElevator):
        if isinstance(other, CallForElevator):
            return self.__callsList.append(other)
    def getCalls(self) -> list:
        return self.__callsList

    def __str__(self):
        return self.__callsList.__str__()

    def __iter__(self):
        return iter(self.__callsList)

