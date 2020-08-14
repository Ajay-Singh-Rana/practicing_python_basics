# %%
# h3avren@py
# fuck'em all
# 3 is love

# %%
# What are Higher-Order Function?
# ```A higher order function is a persistent scope which makes the variable 
# be accessible even after the code execution has moved past that block.```
# A higher order function is also called a ```closure```
def outer_function():
    scoped = "Hey!"
    def inner_function():
        print(scoped)
        # copy of the function object
    return inner_function

inner_copy = outer_function()
# executing the inner_function
inner_copy()

# %%
# The function defined within the outer function gains access to all the
# variables available to the function's local variables.
# What are Decorators ?
# ```Decorators``` are wrappers to existing functions,built using the concept
# of higher-order functions (closure).

def sayHello(name):
    return "Hello {}".format(name)

def hello(function):
    def wrapper(name):
        return "{}".format(function(name))
    return wrapper

def sayGoodBye(name):
    return "Goodbye {}!".format(name)

wrap = hello(sayHello)
wrap2 = hello(sayGoodBye)

print(wrap("H3avren"))
print(wrap2("H3avren"))



# %%