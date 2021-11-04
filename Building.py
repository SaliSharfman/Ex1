import json
class Building:

    #have to pass this aka self so i could assight my "fields"
    #have to push here all carestiristics of Boaz code
    #we getting string as json
    def __init__(self,B_name_j):
        self.x = 0
        #self.buildingName = B_name
        j_initer(self,B_name_j)
        #now we need to call to function that in down page






def j_initer(self,b_name):
 with open(b_name) as f:
   data = json.load(f)
 for B in data['B11']:
    print(B)
str = 'hello'
print(type('B1.json'))

