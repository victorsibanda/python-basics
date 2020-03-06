# Mega fizz buzz exercise
# this exercise has 4 versions

# Boring Buzz
# The point of the game is to count up to a number and whenever we get multiples of 3 you will respond with 'boring' and multiples of 5 you'll respond with 'buzz'.
# multiples of 3 and 5 youll respond with 'boringbuzz'
# do this exercise with while loop and if functions.

#specs:
# multiples of 3 -- > boring
# multiples of 5 -- > buzz
# multiples of 3 and 5 --> boringbuzz


# then do this functionally

def boringbuzz(num) :
    if boring(num) and buzz(num):
        return ("boringbuzz")

def boring(num) :
    if num % 3 == 0:
        return ("boring")


def buzz(num) :
    if num % 5  == 0:
        return ("buzz")


def check_number(num,mod):
    return num % mod == 0


def fiz_buzz(num):
    if boringbuzz(num):
        return "boringbuzz" , num
    elif boring(num):
        return 'boring' , num
    elif buzz(num):
        return 'buzz', num
    else:
        return num



#print(fiz_buzz(15))

num = int(input('What range o you want to check?'))

for i in range (1, num+1):

    print(fiz_buzz(i))

