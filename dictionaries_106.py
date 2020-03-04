#Dictionaries
#Work with key and value pairs/like a real dictionary
#Different from a list as we use key's and not index's

#cringe landlord phone number and address

#syntax
#dict_variable_name = {'key': 'value'}

boris_dict = {'name': 'Boris',
              'l_name':'Johnson',
              'phone': '07712345678',
              'address': '10 Downing Street'}


print(boris_dict)
print(type(boris_dict))
 #access one key value pair
print(boris_dict['phone'])

#change key value pair

boris_dict['l_name'] = 'Son'
print(boris_dict['l_name'])

#assign new key value pair

boris_dict['age'] = 55
print(boris_dict['age'])

boris_dict['number_budgets_passed'] = 1
print(boris_dict)
boris_dict['number_budgets_passed'] += 1
print(boris_dict)
boris_dict['number_budgets_passed'] += 1
print(boris_dict)
#get all the keys and values

print(boris_dict.keys())

print(boris_dict.values())

#nested structres
boris_dict_2 = {'name': 'Boris',
              'l_name':{1:'Johnson',2 : 'West', 3: 'May'},
              'phone': '07712345678',
              'address': '10 Downing Street'}

print(boris_dict_2)

print (boris_dict_2['l_name'])

print (boris_dict_2['l_name'][2])

boris_dict_3 = {'name': 'Boris',
              'l_name':{1:'Johnson',2 : 'West', 3: ['John','Kate','Washer','Peter','Josiah']},
              'phone': '07712345678',
              'address': '10 Downing Street'}

print(boris_dict_3)

print (boris_dict_3['l_name'][3])
#going in to l_name key, then into 3rd key in the value (which is a list)

print (boris_dict_3['l_name'][3][1])
#going in to l_name key, then into 3rd key in the value, then the list

