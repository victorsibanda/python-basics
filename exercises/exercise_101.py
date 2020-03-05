#Practice strings
#Welcome to sparta exercise

#Version 1 Specs
#Define a variable name and assign a string with a name

Name = "Oliver Queen"

#print a welcome message plus the name

print ("Welcome to sparta global", Name)

#Prompt user for input and ask the user for their name
#reassign existing variable
Name = input ('What is your name :')

#Use concatenation to print a welcom message an use method to format the name/input
print("Welcome to sparta global" + Name)



#Version 2
#Do the same but use a different message and use interpolation to print the messae

firstname = input ("What is your first name:")
lastname = input ("What is your last name:")


print (f'Welcome {firstname}{lastname} You have failed this city')

print (' {} {} You have failed this city'.format(firstname,lastname))

#Calculate year of birth
age = int(input('How old are you:') )
YOB = 2020 - age
#Gather details on age and name
yourname = input ('What is your name?')

#print something like

print(f'oh wow {yourname} you are {age} old so you were born in {YOB}')