
user_input = ' '
while user_input != 'pineapple':
    user_input = input("Input?\n")

    if user_input.isdigit():

        user_input = int(user_input)

        for number in range(1,user_input+1):
            if (user_input % 3 == 0) and (user_input % 5 == 0):
                print('Bizzuu')
            elif user_input % 3 == 0:
                print("bizz")
            elif user_input % 5 == 0:
                print("Zzuu")
            else:
               print(number)
    elif user_input == 'pineapple':

        print("thank you for playing")
    else:
        print("Would you enter a different value please")



