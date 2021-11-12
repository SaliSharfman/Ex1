

from Building import Building
from Elevators import Elevators
import json
from  CallForElevator import CallForElevator
from  Calls_List import Calls_List


def main():
    #b = Building()
    b = Building("B2.json")
    print(b.minFloor)

    call = CallForElevator()
    call.load_csv("Calls_a.csv")
    print(call)








if __name__ == '__main__':
    main()
