#for loops

#syntax

 #for item in iterable:
    #block of code

import time


#cool_cars = ['Skoda Felicia Fun', 'Fiat Abarth','Ford Mustang','Toyota Corolla','Fiat Panda','Fiat Multipla']


#count = 1
#for car in cool_cars:
    #print(count, '-' , car)
    #count += 1
    #time.sleep(2)

##### For Loops for Dictionaries

boris_dict = {'name': 'Boris',
              'l_name':'Johnson',
              'phone': '07712345678',
              'address': '10 Downing Street'}



for key in boris_dict:
    #print(key)
    print(key ,':',boris_dict[key])
