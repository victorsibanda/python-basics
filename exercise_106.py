import random
# Magic number game!
# I want you to use operators
# equate something

# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.


# We should define/assign number to a variable called magic_number
magic_number = random.randrange(0, 20,1)

# I need to ask user for input
user_number = float(input('What do you think the magic number is between 0 and 20:'))

while user_number != magic_number:

# I need to check if this input matches a magic_number

    if user_number == magic_number :
        print ('you are correct')
    elif user_number != magic_number:
        print('try again please')
    break



# I need to let the user know if the response was write or not
#self five