num = " "

while num != 'penpinapplespen' :
    num = int(input('Enter a number:'))
    temp_num = num
    num = 0
    while num <= temp_num:
        print(num)
        num += 1
        if num == 'penpinapplespen':
            break
        elif num % 3 == 0 and num % 5 == 0:
            print('Bizzuu')
        elif num % 3 == 0:
            print('bizz')

        elif num % 5 == 0:
            print('Zzuu')
        else:
            print('please enter a valid input')


