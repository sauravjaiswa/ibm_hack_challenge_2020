#IBM-Hack Allotment Code
#Model

class User:
    origin=-99
    destination=-99
    distance=-99
    
    def __init__(self,origin,destination,distance):
        self.origin=origin
        self.destination=destination
        self.distance=distance
        
    def __repr__(self):
        return repr((self.origin, self.destination, self.distance))