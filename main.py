
from Building import Building
from  Calls_List import Calls_List
from Our_Algo import Our_Algo

def main():
    #b = Building()
    b = Building("B2.json")
    print(b.elevators)
    print("elevator size is " +str(b.ElevSize()))

    #call = CallForElevator()
    # call.load_csv("Calls_a.csv")
    # print(call)

   # call_l = Calls_List("Calls_a.csv")
    #print(call_l.rows_list)
    #OA = Our_Algo(b,call_l)








if __name__ == '__main__':
    main()