

name = input('Hi Jackie, what would you like to change your first name to?')
last_name = input('what about your last name ?')
species = input('What species do you identify as?')
eye_color = input('Your new eye colour?')
hair_color = input('Your new hair colour?')

print(f'Hello {name} {last_name} Welcome, your eyes are {eye_color} and your hair color is {hair_color}.')


## Calculate year of birth
# calculate the difference

age = int(input ('How old are you?'))

current_year = 2020
YOB = current_year - age

print(f'You said you were {age}, so you were born in {YOB}')


# Print them back to the user as conversation including the year they were born!
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.
# print something like: 'You said you we're 28 hence you were born in 1991!'


# Section 2 - Calculate the Age difference!
# ask user for their name and age -- store these in variables
# ask user for their Mothers name and age

nameu= input ('What is your name?')
ageu = int(input ('How old are you?'))
namem= input ('What is your mothers name?')
agem = int(input ('How old is your mother?'))
yobu = 2020 - ageu
yobm = 2020 - agem
diffage = yobu - yobm

# calculate the difference and year of birth for each
# print out these formated. something along the lines of:
# your name is <name>, and you are <age> born on the year of <y_birth>.
# This is <difference_y> later than <mom_name> who was on on <y_birth_mon>

print('your name is {},you are {} born in the year {}. You mother {} was born in {} and she is {} years older than you'
      .format(nameu,ageu,yobu,namem,yobm,diffage))
