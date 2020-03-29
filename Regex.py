# Author : Tomas O'Malley
# ID : G0036128
# PROGRAM : NFA BUILDER
# Weighting  : 50%
# Module : Graph Theory

class State:

  """A state with one or two edges, all edges labelled by label."""

  # Constructor.
  def __init__(self, label=None, edges=None):
    # Every state has 0, 1, or 2 edges from it.
    self.edges = edges if edges else []
    # Label for the arrows. None means epsilon.
    self.label = label

class Fragment:

	"""An NFA Fragment with a start state and an accept state"""

	# Constructor
	def __init__(self , start , accept):
		# start state of NFA Fragment
		self.start = start
		# Accept state of NFA fragment
		self.accept = accept

def shunt(infix):

	"""Function which returns the infix expression in postfix"""

	# Convert input input  to a stack ish list
	infix = list(infix)[::-1]

	# Operator Stack Output list.

	opers , postfix = [] ,[]

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

def compile(infix):

	"""Returns an NFA Fragment representing the infix regular expression """

	# Convert infix to postfix
	postfix = shunt(infix)
	# Make a postfix  stack of characters 
	postfix = list(postfix)[::-1]

	# A stack for NFA Fragemnts
	nfa_stack = []

	while postfix:
		# pop a character from postfix.
		c = postfix.pop()
		if c =='.':
			# Pop two fragments off the stack
			frag1=nfa_stack.pop()
			frag2=nfa_stack.pop()
			# Point frags accept state at frag 1s start state.
			frag2.accept.edges.append(frag1.start)
			# new start state is frag 2's
			start = frag2.start
			# new accept state is frag 2's
			accept = frag1.accept
			newfrag = Fragment(start , accept)
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
		
		elif c =='*':
			# Pop a single fragment off the stack
			frag = nfa_stack.pop()
			# Create new start and accept .
			accept = State()
			start = State(edges=[frag.start,accept])
			# Point the arrows.
			frag.accept.edges =[frag.start , accept]
		

		else:
			accept = State()
			start = State(label=c, edges=[accept])

			newfrag =  Fragment(start,accept)
		# Create new instance of Fragment to represent the new NFA
		nfa_stack.append(newfrag)

	# Push the new NFA to the Stack
	return nfa_stack.pop()

# Add a state to a set, and follow all of the epsilon arorws.

def followes (state , current):

	#Only do something when we havent already seen the state.
	if state  not in current:
	# Put the state itself into current
		current.add(state)
		# see whether state is labelled by e(pslion).
		if state.label is None:
		# Loop through the states pointed to by this state.
			for x in state.edges:
			# Follow all of their epsilson too
				followes(x,current)

def match(regex, s):

	"""This function will return true if and only if the regular expression"""
	# Regex fully matches the string s .It False otherwise.


	# Compile the regualr exoression into nfa
	nfa = compile(regex) 

	# Try to macth the regular exoression  to the string s.
	# The current set of states .
	current =  set()
	# Add the first state , and follow all e(psilon) arrows.
	followes(nfa.start, current)

	# The previous set of states.
	previous = set ()

	# loop over characters in s 
	for  c in s:
		# Keep track of where we were.
		previous = current
		# Create a new empty set for the states we're about to be in
		current = set ()
		# Loop through the previous states.
		for state in previous:
			# Only follow arrows not labelled by (epsilon)
			if state.label is not None:
				# If the label of the state is equal to the character we've read:
				if state.label == c:
					# Add the state(s) at the end of the arrow to current.
					followes(state.edges[0], current)


	# Ask the NFA if it matches the string s.
	return nfa.accept in current

if __name__ == "__main__":
	tests = [

	["a.b|b*" , "bbbb" , True],
	["a.b|b*" , "bbxxb" , False],
	["a.b" , "ab" , True]

	]

	"""An array of tests for the program"""
	for test in tests:
		assert match(test[0] , test[1]) == test[2], test[0] + ("Should" if test[2]  else "should not")+"match" + test[1]

	#Attempt 1  testing using Assert Method
	#assert match("a.b|b*" , "bbbbbbbb") , "a.b|b* should match bbbb"
	#assert not match("a.b|b*" , "bbbbbbbbxxx") , "a.b|b*  not should match bbbbbbbbxxx"