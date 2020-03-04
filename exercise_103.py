# Define the following variables
# name, last_name, species, eye_color, hair_color
# name = 'Lana'

# Prompt user for input and Re-assign these
# name = input('what new name would you like?')

# Print them back to the user as conversation
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.

Name = 'Jackie'
last_name = 'Chan'
species = 'Human'
eye_color = 'red'
hair_color = 'brown'

name = input('Hi Jackie, what would you like to change your first name to?\n')
last_name = input('what about your last name ?\n')
species = input('What species do you identify as?\n')
eye_color = input('Your new eye colour?\n')
hair_color = input('Your new hair colour?\n')

print(f'Hello {name} {last_name} Welcome, your age is 26, your eyes are {eye_color} and your hair color is {hair_color}.')
