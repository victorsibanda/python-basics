


# - You can vote and drivre
# - You can vote
# - You can driver
# - you can't leagally drink but your mates/uncles might have your back (bigger 16)
# - Your too young, go back to school!
run = 1

while run == 1 :

    age = int(input('how old are you?'))
    driver_license = str(input('Do you have a license'))
    if age >= 18 and driver_license == 'yes':
        print('you can drive and vote')
    elif age >= 18 :
        print('you can vote')
    elif driver_license == 'yes' and age >= 17 :
        print('you can drive')
    elif 18 > age >= 16 and driver_license != 'yes':
        print("you can't legally drink but your mates/uncles might have your back ")
    else:
        print('Your too young, go back to school!')