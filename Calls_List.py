from CallForElevator import CallForElevator
import csv

#esh lanu po list kriot

class Calls_List:

    def __init__(self,csv_file):


        self.load_csv(csv_file)



    def load_csv(self, csv_file):

     rows = []
     with open(csv_file,'r') as file:

        csvreader =csv.reader(file)
        for row in csvreader:
            o=CallForElevator(name=row[0], time=row[1], src=row[2], dst=row[3], x=0, allc=0)
           # print(type(o.time))
            rows.append(o)
     self.rows_list =rows

    def cals_list(self)->list:
        return self.rows_list

    def cals_size(self)->int:
        return len(self.rows_list)
    #newline
    def set_to_scv(self) -> csv:
        with open('out.csv' , 'a',newline='') as f:
            # create the csv writer
            list = self.cals_list()
            cs = self.cals_size()
           # print(dir(list[0]))
            for i in range(cs):
               # list[i].set_allc(5)

                tup = (list[i].get_name(),
                       str(list[i].get_time())
                       ,str(list[i].get_source()),
                       str(list[i].get_dst()),
                       str(list[i].get_peulot()),
                       str(list[i].get_allc()))
                writer = csv.writer(f)
                writer.writerow(tup)

            # write a row to the csv file

            f.close()

   # def check_append(self)->N:
