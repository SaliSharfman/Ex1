import csv
class CallForElevator:
    def _init_(self, name='', time=0, src=0, dst=0, x=0, allc=0) -> None:
        self.name=name
        self.time=time
        self.src =src
        self.dst=dst
        self.x=x
        self.allc=allc
        self.rows = []
        self.calls = []

    def _str_(self) -> str:
        return f":{self.name}\n time:{self.time} src:{self.src} "

    def load_csv(self, csv_file):
     with open(csv_file) as file:

        csvreader =csv.reader(file)
        for row in csvreader:
            o=CallForElevator(name=row[0], time=row[1], src=row[2], dst=row[3], x=0, allc=0)
            self.calls.append(o)
            self.rows.append(row)
    #print(calls[1].time)
    #print(calls)