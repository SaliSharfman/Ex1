from CallForElevator import CallForElevator
import csv
class Calls_List:

    def __init__(self,csv_file):


        self.load_csv(csv_file)



    def load_csv(self, csv_file):

     rows = []
     with open(csv_file,'r') as file:

        csvreader =csv.reader(file)
        for row in csvreader:
            o=CallForElevator(name=row[0], time=row[1], src=row[2], dst=row[3], x=0, allc=0)
            rows.append(o)
     self.rows_list =rows



