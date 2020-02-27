#Author     : Tomas O'Malley
#Date       : 27/02/2020
#Progran    : Automaton Fragments
#References : Ian McLoughlin week 7 lab


class State:
    #Every State ahs 0,1 or 2 edges from it
    edges = []
    
    # label for the arrows . None means epsilon
    label = None
    
    # Constructor for the class.
    def __init__(self, label=None, edges=[]):
        self.edges = edges
        self.label = label
        
    
class Frag:
    # Start state of NFA fragment
    start = None
    
    #Accept state of NFA fragment 
    accept = None 
    
    # Constructor.
    def__init__(self, start , accept):
    self.start = start 
    self.accept = accept
    
myInstance = State(label='a', edges=[])
myotherinstance = State(edges=[myInstance])
myFrag = Frag(myinstance , myotherinstance)

print(myinstance.label)
print(myotherinstance.edges[0])
print(myfrag)