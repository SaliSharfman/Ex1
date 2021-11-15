#assending and desending order






class MaxHeap(object):

    #kodem neathel oto
    def __init__(self):
        self.list = []
        #mispar rishon triviali

     #   add(self,num)

    def add(self, num):
        self.list.append(num)
        self.list.sort(reverse=True)

    def pop(self):
        self.list.remove(0)
