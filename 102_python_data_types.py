#Strings
#Text and Characters
#Syntax
#"" and ''

#Define a string
#Anything that is text is a string

my_string = 'Hey I am a cool string B)'
print(my_string)
type(my_string)

#Concatenation

joint_string  = 'Hey I am another' + ' cool string, ' + my_string
print (joint_string)

#example two of concatenation
name = 'Mohamed'
welcome_text = 'Welcome to SPARRRRRRRRRRRTTTTTTTAAAAAAAAA'

print (welcome_text+' '+name)
print (welcome_text,name) #overloading the sprint

#Interpolation

#inserting a sting inside another string
#or running python inside a string

print (f'Welcome {name} to class 54, we are Contested Terrain ')

#print (f'Welcome {input("What is your name")} to class 54, we are Contested Terrain ')

print ('Welcome to class 54 ,  we are Contested Terrain'.format(name))


#Useful methods

# A method is a funtion that belongs to a specific data type.
#e.g it would not make sense to capitalize integers
example_long_str = '     Hello , This is  a badly formated test?'
print (example_long_str)
#Remove trailling white spaces
print (example_long_str.strip())
#Make it lowr case


print(example_long_str.lower())

#Make it upper case
print(example_long_str.upper())

#First character capitalised
print(example_long_str.strip().capitalize())

print(example_long_str.strip().title())

#Change the question mark into an exclamation mark
print(example_long_str.strip().replace('?','!') )

#chainsome methods and :
      # Remove trailing white spaces
      #make it nicely formatted with only first letter capitalised

#print(example_long_str.strip().replace('?','!').capitalize().replace('badly','well')

#create a list with individual words
print(example_long_str.strip().split())

