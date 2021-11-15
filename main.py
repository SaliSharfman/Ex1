
from Building import Building
from  Calls_List import Calls_List
from Ex1 import Ex1
from CallForElevator import  CallForElevator
import sys
def main():
    #b = Building()

    #print(b.elevators)
    #print("elevator size in building is " +str(b.ElevSize()))





  #  one_call = CallForElevator(0,0,0,0)

   # call_l = Calls_List("Calls_a.csv")
    #print(call_l.rows_list)
    #OA = Our_Algo(b,call_l)
    #Ex1.py
    #B1.json
    #C2.csv
    #out.csv
    firstargument = sys.argv[0]
    secondargument = sys.argv[1]
    thirdargument = sys.argv[3]

    fourdargument = sys.argv[4]

    calls = Calls_List(secondargument)
    b = Building(thirdargument)
    #we will work on this function
    #in Ex1
    #calls.set_to_scv(fourdargument)
    #Ex1.py B1.json C2.csv out.csv
    syses = []
    syses.append(firstargument)
    syses.append(secondargument)
    syses.append(thirdargument)
    syses.append(fourdargument)
    print(syses)
      
    #our_algo = Ex1(calls,b,fourdargument)


