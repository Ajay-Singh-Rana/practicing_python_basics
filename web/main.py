# k@mlesh
# h3avren

# So here we will start with the basics i.e. keywords and data types

# print() is a function used in python to output (at the console) something. 

""" Keywords : These are the reserved terms for any laguage and cannot be used by the user as a variable.Examples of keywords in
    Python are for,if,else,elif,class,def,in,or,and,while,not,True,False..."""

"""Data Types : These are categories that define what kind of some data is.For example 12 is a numerical data and "Rakesh" is a
    textual data.So both "Rakesh" and 12 can not tereated as one.Therefore languages define some categories to define this data called 
    Data Types.These are string (str),integer (int),floating point (float) and many more ."""

# comments in python
"""
    comments are neglected by the interpreter but these enhance the readability of the code especially to someone who does not have any idea of what the code is all about.
    there are two ways to comment a line in python :
    1 :-> By using a hash '#' symbol before the line. This methos is used to make single line spanning comments 
    2 :-> By enclosing the lines between a pair of three double/single qoutes i.e '''This is a comment'''.This type of a comment is called a docstring and is 
    also treated as a multiline spanning string by pyhton."
"""

# integer data :
integer = 18
print(f"{integer} is of the type {type(integer)}")  # type() is a function that returns or tells the data type of any object 
""" here a special type of string substitution is used...it is called 'f string' ...in this we put an 'f' before any string then we 
    directly type the name of the variable name between '{}'"""

# string data
string = 'The only thing that is constant is "change".'
print(f"'{string}' is of the type {type(string)}")

# floating point numbers
float_value = 34.56
print(f"{float_value} is of the type {type(float_value)}")

# lists
"""List in python are arrays i.e. a combination of different data items.In Python a list can contain elements of different data types too.Lists are mutuable objects
   i.e these can be changed at will.    
"""
empty_list = [] # declaring an empty list
empty_list_2 = list()   # declaring an empty list using the 'list()' function.
one_dimensional_list = [1,2,3,4,5]
one_dimensional_list_2 = list([1,2,3,4,5])
two_dimensional_list = [[1,2,3],[4,5,6],[7,8,9]] 
two_dimensional_list_2 = list([[1,2,3],[4,5,6],[7,8,9]])
print(empty_list,"\n")
print(empty_list_2,"\n")
print(one_dimensional_list,"\n")
print(one_dimensional_list_2,"\n")
print(two_dimensional_list,"\n")
print(two_dimensional_list_2,"\n")

# list comprehension
"""
    A shortcut method to create lists without writing elements manually.
"""
list_1 = [x for x in range(20)]
print(list_1)

# sets
"""
    sets are data types that hold unique data elements.
"""
# creating a set 
set_1 = set([1,2,3,4,5])
print(set_1)
# creating a set from an existing list
list_1 = [1,1,2,2,2,3,4,5,6,7,7]
set_2 = set(list_1)
print(set_2)
# functions that can be performed on sets
# addiing elements
set_1.add(6)    # adds a new element to the set if it doesn't exist already
print(set_1)
# emptying a set
set_1.clear()
print(set_1)

# tuples
"""
    tuples are similar to lists with the only difference being that tuples are immutable i.e. cant be changed once created.
"""
empty_tuple = ()
empty_tuple_2 = tuple()
print(empty_tuple)
print(empty_tuple_2)
tuple_1 = (1,2,3,4)
tuple_2 = tuple([1,2,3,4,5,6,7])
print(tuple_1)
print(tuple_2)

# dictionaries
"""
    Dictionaries are key value pairs where values are accessed with the help of keys.//These are of immutable type.
"""
dictionary_example = {"True":1,"False":2,"I":"Fool"}

# operators like '+','-','x' are used to conduct calculations .These are also provided by programming languages

# The plus ('+') operator ::=>

# for integers and floating point values it returns the sum of the numbers
a = 3
b = 4
print(f"{a} + {b} = ",a+b)
a = 3.41
b = 4.59
print(f"{a} + {b} = ",a+b)

# for strings the '+' operator works as a concatnation function
a = "Hello "
b  = "World!"
print("'Hello ' + 'World!' = ",a+b)

# The '*' operator ::->
# for integers and floating point numbers '*' works as the multiplication operator
a = 5
b = 6
print(f'{a} * {b} = ',a*b)
a,b = 34.5,3
print(f"{a} * {b} = ",a*b)

# for strings the '*' operator means the repetition but it should be in the form string*number  
a = "Nikki "
print("'Nikki '*3 = ",a*3)

# other operators are '-','/','%',':=','==','<=','>=','<','>','!','=','-=','+=','*=','/=','%='

# the '-' operator is used as subtraction operator with integers and floating point numbers only
a = 5
b= 7
print(f"{b} - {a} = ",b-a)

# the '/' operator is used for 
a = 50
b = 10
print(f"{a} / {b} = ",a/b)

# the '%' operator is called the modulo operator and it returns the raminder of the division performed on two numbers
a = 6.7
b = 3.3
print(f"{a} % {b} = ",a%b)

# assignment operators 

# comparision operators

# conditional statements
"""
    These statements are used to evaluate certain conditions and take decisions accordingly.
"""

# if 
"""
    This statement evaluates a condition and executes the code below it if the condition is True
"""
a = 5
if(a==5):
    print("a = ",5)
if(a==6):
    print("a = ",6)

# else
"""
    This statement is a fallback for  the 'if' statement to execute desired commands if the condition with 'if' isn't satisfied.It doesn't evalutate any condition.
"""
a = 6 
if(a==7):
    print("a = ",7)
else:
    print("a = ",a)

# elif
"""This satement is similar to the 'if' staement and always comes after an 'if' statement.It is used to test multiple conditions.
   But the evaluation occurs sequentially. 
"""
a = 8
if(a==7):
    print("a = ",7)
elif(a==8):
    print("a = ",a)
else:
    print("a = ",6)

# Loops
"""
    loops are a way to write repetitive steps under a single statement.
"""
print()
# for loop
"""
    a for loop is used when we already know the number of times we need to execute a piece of code. A for loop has three arguments i.e start,end and change
"""
for i in range(1,6,1):
    for j in range(1,i+1,1):  # nested loop
        print("*",end="")
    print()

print()
# while loop
"""
    a while loop is used when we do not know exactly how many times certain steps should be repeated.So, we set it to a condition which
    helps breaking out from the loop and prevents an infinite loop.
"""
n = 1
while(n<=10):
    print("*"*n)
    n+=1

print()

# the break statement
"""
    The break statement is used to break out of a loop immediately no matter how many more iterations of the loop remain to be executed.
"""
for i in range(1,5,1):  # supposed to run 4 times
    print("Hello")
    if(i==2):
        break   # breaks out of the loop after the second iteration
print()

# the continue statement
"""
    this statement stops the execution of the ramining code under the current iteration and jumps on to the next iteration.
"""
for i in range(1,5,1):
    if(i==2):
        continue    # skips printing 2 to the console
    print(i)
print()

# user defined funtions
"""
    functions are way to reuse a piece of code that performs certain tasks, instead of writing it again and again throughout the file.
"""
def add(x,y): # 'def' is the keyword used to define a function
    return x+y  # 'return' keyword is used to make the function return some value
print(add(3,4))

# lambda expressions
"""
    lambda expressions are also known as anonymous functions.These cannot be used for multiline functions.
    syntax:
    lambda inputs : return value expression
"""
f = lambda y : y + 5    # a function that takes a input and returns a value that is biiger than the input by 5
# the lambda expression being assigned to 'f' makes f a callable function
print(f(4))

def quadratic_equation(a,b,c):  # takes the three coefficients as input
    return lambda x : ((a*(x**2)) + (b*x) + c)  # returns an expression as output that when called with an input will return the value of the quadratic equation

g = quadratic_equation(3,4,5)(2)
print(g)

# concepts of object oriented programming



# implementing object oriented programming with classes in python
