# Write a bizz and zzuu game ##project

# as a user I should be able prompted for a number, as the program will print all the number up to and inclusing said number while following the constraints / specs. (bizz and buzz for multiples or 3 and 5)

# As a user I should be able to keep giving the program different numbers and it will calculate appropriately until you use the key word: 'penpinapplespen'


# write a program that take a number
# prints back each individual number, but
    # if it is a multiple of 3 it returns bizz
    # if a multiple of 5 it return zzuu
    # if a multiple of 3 and 5 it return bizzzzuu


num  =  list(range(0,101))



while num != 'penpinapplespen' :
    num = int(input('Enter a number:'))
    if num == 'penpinapplespen':
        break
    elif num % 3 == 0 and num % 5 == 0:
        print('Bizzuu')
    elif num % 3 == 0:
        print('bizz')

    elif num % 5 == 0:
        print('Zzuu')

