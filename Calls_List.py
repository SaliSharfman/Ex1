from CallForElevator import CallForElevator
class Calls_List:

    def __init__(self):
        self.callsList=[]

    def __add__(self, other: CallForElevator):
        if isinstance(other, CallForElevator):
            return self.callsList.append(other)
    def getCalls(self)->list:
        return self.callsList

    def __str__(self):
        return self.callsList.__str__()

    def __iter__(self):
        return iter(self.callsList)

