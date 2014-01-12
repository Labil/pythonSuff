#Lists and copy and iteration

words = ['chia', 'butter', 'carrot']
for w in words:
	print w, len(w)

#If you need to modify the sequence you are iterating over while inside
#loop, it is recommended that you first make a copyy
#Iterating over a sequence does not implicitly make a copy. 
#Use slice notation to copy [:]
for w in words[:]: #Loop over a slice copy of the entire list.
	if len(w) >= 6:
		words.insert(0, w)
print words

# pass statement - does nothing. Can be used when a statement is required syntactically
# but the program shouldn't do anything
while True:
	pass  #wait for keyboard interrpt (Ctr + C)

#First statement of function def can be a string literal:
def funky(param):
	"""This function is funky to the MAX"""
	print "I'm too funky."
#This string is the function's documentation string, or docstring.
#Lots of tools se docstrings to automatically produce documentation, or
#let the user interactively browse through code
#Good practice to include docstrings in code that you write! Do it!

#Variable scope example:
myGlobalVariable = 3
def func():
	"""This function shows that functions cannot directly change a global variable"""
	myGlobalVariable = 5000
	print 'This is the variable inside func:', myGlobalVariable

func()
print 'This is the global variable', myGlobalVariable
#All variable assignement in a function store the value in the local symbol
#table. Variable references first look in the local symbol table, then
#in the local symbol tables of enclosing functions, then in the global table and
#finally in the table of built-in names. Thus, global variables cannot be directly
#assigned a value within a function (unless named in a global statement), but they
#may be referenced.

#You can assign functions to variables
f = func
f()

#Functions with predefined arguments
def getPermission(prompt, retries=4, complaint='Yes or no, please!'):
	while True:
		ok = raw_input(prompt)
		if ok in ('y', 'ye', 'yes'): #Tests if a sequence contains a certain value
			return True
		if ok in ('n', 'no', 'nope'):
			return False
		retries = retries - 1
		if retries < 0:
			raise IOError('Wrong user input')
		print complaint

getPermission('Do you wanna quit?')


#Lambda expressions:
#Small anonymous functions can be created with the lambda keyword
# - restricted to a single expression
#Example: (still from docs.python.org/2/tutorial)
def incrementor(n):
	"""This function returns a function.""" #Docstrings should begin with a capital letter and end with a period
	return lambda x : x + n

f = incrementor(34) #Now f stores the function lambda x : x + n
f(0) #outputs 34
f(1) #outputs 35
#You can also pass a lambda as an argument into a function

# Chapter 5.1.3 Functional programming tools
#filter(), map(), reduce()

#filter(function, sequence) returns a sequence consisting of those items
#from the sequence for which function(item) is true (If sequence is a string of tuple
# the result will be the same type; otherwise, it is always a list.)
#Ex: Compute a sequence of numbers not divisible by 2 or 3
def f(x): return x % 2 != 0 and x % 3 != 0

a = filter(f, range(2, 25))
print a

#map(function, sequence) calls function(item) for each of the sequence's items
#returns a list of the return values
#Ex: compute cubes:
def cube(x) : return x*x*x
a = map(cube, range(1,11))
print a

#Note: More than one sequence may be passed; the function must then have as many arguments
# as there are sequences and is called with the corresponding item from each seq.
#(or None if some seqence is shorter than another)
seq = range(9)
def add(x, y): return x + y
a = map(add, seq, seq)
print a

#reduce(function, sequence) returns a single value from calling the binary
#function function on the first two items of the sequence, then on the result and
#the next item, and so on. 
#Ex: compute sum of numbers 1 through 10:
def add(x, y): return x + y
a = reduce(add, range(1, 11))
print a