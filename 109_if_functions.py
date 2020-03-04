#If functions are usually work with booleans
#True or False

#if <condition>
    #block of code
#elif


weather = str(input('What is the weather like?\n'))

if 'rainy' in weather and 'windy' in weather:
    print('weather looks terrible, stay inside')
elif 'rainy' in weather:
    print('take your umbrella')
elif weather == 'sunny':
    print('nice,take some shades')
else:
    print("didn't quit catch that , please enter again")
