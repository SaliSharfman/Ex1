import json
class Building:

    #have to pass this aka self so i could assight my "fields"
    #have to push here all carestiristics of Boaz code
    def __init__(self):
        self.x = 0;






with open('Building_Data1') as f:
   data = json.load(f)
for state in data['Building_Data1']:
    print(state)


