from trip import Trip

class Driver:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    

    def my_trips(self):
        temp=[]
        for i in range(len(Trip._all)):
            if Trip._all[i].driver == self:
                temp.append(Trip._all[i])
        return temp
                

    def my_trip_summaries(self):
        temp=[]
        for i in range(len(Trip._all)):
            if Trip._all[i].driver == self:
                temp.append(str(Trip._all[i].start)+ ' to '+str(Trip._all[i].destination))
        return temp