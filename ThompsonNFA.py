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

class Fragment:
	# start state of NFA Fragment
	start= None
	# Accept state of NFA fragment
	accept = None

	# Constructor
	def __init__(self , start , accept):
		self.start = start
		self.accept = accept

def shunt(infix):
	# Convert input input  to a stack ish list
	infix = list(infix)[::-1]


	#Tomas Omalley 
	# The shunting yard Algorithm 

	# Convert input to a stack like list.

	# Operator Stack.
	opers = []

	# Output list.
	postfix = []

	# Operator precedence
	prec = {'*': 100 , '.': 80, '|': 60, ')': 40 , '(':20}

	# Loop through the input one character at a time. 
	while infix:
		# Pop a character from the input
		c=infix.pop()

		# Decide what to do based on the character.
		if c=='(':
			# Push an open bracket to the opers stack.
			opers.append(c)
		elif c==')':
			# Pop the operators stack until you find an (.
			while opers[-1] != '(':
				postfix.append(opers.pop())
			# Get rid of the '('.
			opers.pop()
		elif c in prec:
			# Push any operators on the opers stack with higher prec to the output.
			while opers and prec[c] < prec[opers[-1]]:
				postfix.append(opers.pop())
			# Push c to the operator stack.
			opers.append(c)
		else:
			# Typicallu , we just push the character to the output.
			postfix.append(c)
		
	while opers:
		postfix.append(opers.pop())

	return ''.join(postfix)



def regex_compile(infix):
	postfix = shunt(infix)
	postfix = list(postfix)[::-1]

	nfa_stack = []

	while postfix:
		# pop a character from postfix.
		c = postfix.pop()
		if c =='.':
			# Pop two fragments off the stack
			frag1=nfa_stack.pop()
			frag2=nfa_stack.pop()
			# Point frag2s accept state at frag 1s start state.
			frag2.accept.edges.append(frag1.start)
			# Create new instance of fragment to represent the new NFA. 
			newfrag = Fragment(frag2.start.frag1.accept)
			# Push the new NFA to the NFA stack
			nfa_stack.append(newfrag)
		elif c =='|':
			# Pop two fragments off the stack.
			frag1 = nfa_stack.pop()
			frag2 = nfa_stack.pop()
			# Create new start and accept states
			accept = State()
			start = State(edges=[frag2.start , frag1.start])
			# Point the old accept states at the new one
			frag2.accept.edges.append(accept)
			frag1.accept.edges.append(accept)
			newfrag=Fragment(start,accept)
			nfa_stack.append(newfrag)
		elif c =='*':
			# 
			frag = nfa_stack.pop()
			accept = State()
			start = State(edges[frag.start,accept])
			frag.accept.edges.append(frag.accept)
			newfrag = Fragment(start , accept)
			nfa_stack.append(newfrag)

		else:
			accept = State()
			start = State(label=c, edges=[accept])
			newfrag =  Fragment(start,accept)
			nfa_stack.append(newfrag)




def match(regex,s):
	# This function will return true if and only if the regular expression
	# Regex fully matches the string s .It False otherwise.

	# Compile the regualr exoression into nfa
	nfa = regex_compile(regex) 
	return nfa

print(match("a.b|b*", "bbbbb"))








