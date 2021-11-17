import collections

from Building import Building
from  Calls_List import Calls_List
from Ex2 import Ex1
from CallForElevator import  CallForElevator
import sys



def allcoateAnElevaotor(c=Calls_List, b=Building, fourArgument=""):  # need to changed CallForElevator as arguments
    argfour = fourArgument
    c = c
    b = b
    flag_first_time = True
    # we want all elevators
    # self.allcoateAnElevaotor()
    # elevatorim laavod itam
    elevators = Building.getAllElevators()

    elevAmount = b.numberOfElevator()
    # self.allcoateAnElevaotor()
    # i have the calls as field already

    chosenElevtor = -1
    infinity = float("inf")
    isSameDirc = False

    pass


def main():
    #allc = Calls_List('Calls_a.csv','out.csv')
   # allc.load_csv('Calls_a.csv')
   # allc.set_to_scv('out.csv')
   # b = Building('B2.json')
    #b.load_json('B2.json')
    #try:
        print("IAM AT EX1")
        firstargument = sys.argv[0]
        print("firste arg is = "+str(firstargument))
        secondargument = sys.argv[1]
        thirdargument = sys.argv[2]

        fourdargument = sys.argv[3]
        b = Building(secondargument)
        b.load_json(secondargument)
        calls = Calls_List(thirdargument,fourdargument)
        calls.load_csv(secondargument)
        calls.set_to_scv(fourdargument)


        #allc = Calls_List(secondargument,'out.csv')
        #our_algo.allcoateAnElevaotor()

    #except Exception:
      #  print("therese is no 5 arguments or its a Test")

    # our_algo = Ex1(calls,b,fourdargument)





