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


