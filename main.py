
from Building import Building
from  Calls_List import Calls_List
from Our_Algo import Our_Algo
from CallForElevator import  CallForElevator
def main():
    #b = Building()
    b = Building("B2.json")
    print(b.elevators)
    print("elevator size in building is " +str(b.ElevSize()))

    calls = Calls_List("Calls_a.csv")

    print("the size for calls list is = "+str(calls.cals_size()))
    print(calls.rows_list)

    calls.set_to_scv()
  #  one_call = CallForElevator(0,0,0,0)

   # call_l = Calls_List("Calls_a.csv")
    #print(call_l.rows_list)
    #OA = Our_Algo(b,call_l)








if __name__ == '__main__':
    main()
