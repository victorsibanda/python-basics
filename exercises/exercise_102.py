name = input ('What is your name:')
height = int(input('How tall are you in cm:'))
fave_colour = str(input('what is your favourite colour?'))
s_num = int(input("Enter a secret number"))

print(f'Hello {name}, it is nice to meet you, look about {height}cm. And I think {fave_colour} will look nice on you')

if s_num == 1000 :
    print ('Correct Number')
elif s_num != 1000:
    print("Wrong Number")