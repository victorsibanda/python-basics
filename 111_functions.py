#Functions
"""""
Functions are like a machine you put something in and you get a results.
It can take in inputs do some work  and it can output something different.
- They do one Job
- They should be testable and Maintanable
-- avoid stringy/spaghetti code
- Good naming convention
- == Reduced technical debt
- Concept of Don't Repeat Yourself
-Generally never print inside a function / Instead use a return
-print the calling of the function
-they need to be called (using the name and arguments )

#Syntax

def name_of_function (arg1, arg2):
    block of code
    return ('doing some work')

"""


def say_hello_zeus ():
    return 'Hello Zeus'


result = say_hello_zeus()

print(result)


def say_hello (x):
    return 'Hello' + ' ' + x


print(say_hello('Victor'))

"""""
Format each name nicely 
Use strip and capitalize
print concatenated name 
"""


def full_name_formatter(f_name,l_name):
    formatted_f_name = f_name.strip().capitalize()
    formatted_l_name = l_name.strip().capitalize()
    return formatted_f_name + ' ' + formatted_l_name


print(full_name_formatter('victor','sibanda'))


def add_func(x,y):
    return x+y

