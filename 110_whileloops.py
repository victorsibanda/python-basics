#syntax
#while <condition>:
    #run block of code
    # if <condition>:
    #break - used to break the while loop
    #continue allows us to skip an iteration for the next while loop printing a value outside the while loop




# counter = 0
# while counter <= 10:
#     print (counter)
#     print ('this is cool')
#     counter += 1

#user_input = str(input ('you want to play?'))

# while user_input == 'yes' or user_input == 'y' :
#     random_num = 10
#     print('welcome to our random game')
#     user_input = int(input('what is your guess?'))
#     if user_input == random_num:
#         print ('well done')
#     else:
#         print('sorry try again')
#     user_input = input ('play again?')

while True:
    user_input = input('1 for pancakes, 2 for cake, 3 to exit')
    if user_input == '1':
        print('pancakes')
    elif user_input == '2':
        print('cake')
    elif user_input == 'exit' or user_input == '3':
        print('exit')
        break
    else:
        print('Use your numbers and your keyboard')