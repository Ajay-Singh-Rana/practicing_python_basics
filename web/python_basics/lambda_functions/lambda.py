# h3avren

# Lambda Functions

''' Definition :
        Lambda Functions are also called anonymous functions as these functions do not have a name.
'''

# Syntax
# A lambda function starts with the keyword `lambda`
# The syntax for a lambda function is as follows
 
# lambda arguments_list : return_expression

# Creating a lambda function 
lambda x : 3*x + 1  # here this anonymous function takes an argument namely x and returns the value 1 more than x multiplied by 3 (i.e. 3x + 1)
# But we cannot use the above function as it doesn't have a name,to use it we need to give it a name by assigning it to a variable

# using a lambda function 
no_more_anonymous = lambda x : 3*x + 1
# now to we can use the variable name as any normal python function 
print(no_more_anonymous(3))


# Lambda function without arguments 
# Like any other python function a lambda function too can have a null arguments list i.e. a function without arguments.

# example of lambda function without arguments
f = lambda : print("Hello World!")
f() # calling the function f


# Using a lambda function for impersonating a mathematical equation

# we can use lambda functions for generating quadratic equations
# let's write a function that simulates the mathematical function of ax**2 + bx + c
def quadratic_equation(a,b,c):  # this function takes the values of the coefficients of x as arguments
    return lambda x : ((a * (x ** 2)) + (b * x) + c)

f = quadratic_equation(3,2,1)   # returns a function object which impersonates the mathematical function of 3x**2 + 2x + 1

# now let's pass the values of 1,2 and 3 to the function f
print(f(0)) # returns 1
print(f(1)) # returns 6
print(f(2)) # returns 17

# you can manually check the result values by using the values of 1,2 and 3 for the equation of 3x**2 + 2x + 1

# That's it for this bit...See you in the next tutorial...Until then a H3avren style Ta-Da...

