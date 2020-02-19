# Author Tomas O'Malley
# Classes used in Thompsons construction
# Week 6 - 17-02-2020
class State:
	# Every state has 0,1 or 2 edges from it
	edges = []

	#Label for the arrows , None means epsilon
	label= None

	# Is this an accept state?

	# Constructor for the class.
	def __init__(self, label=None , edges=[]):
		self.edges=edges
		self.label=label

myinstance = State(label='a' , edges=[])
myotherinstance = State(edges=[myinstance])
print(myinstance.label)
print(myotherinstance.edges[0])

class Frag:
	# start state of NFA Fragment
	start= None
	# Accept state of NFA fragment
	accept = None

	# Constructor

	def __init__(self , start , accept):
		self.start = start
		self.accept = accept

myinstance = State(label='a' , edges=[])
myotherinstance = State(edges=[myinstance])
myfrag = Frag(myinstance,myotherinstance)

#Print output
print(myinstance.label)
print(myotherinstance.edges[0])
print(myfrag)

