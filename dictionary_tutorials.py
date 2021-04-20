# is a collection data type which has key value pairs
#mutable, unordered, indexed, no dublicates
'''
#Dictionary Vs. List:
#Dictionaries
phone_numbers = {'Kyle': 5513194065, 'John': 5512587415, 'Jane': 4086985478}
print(phone_numbers['Kyle'])
# output:5513194065
print(phone_numbers)
#output: {'Kyle': 5513194065, 'John': 5512587415, 'Jane': 4086985478}
del phone_numbers['John']
print(phone_numbers)
#{'Kyle': 5513194065, 'Jane': 4086985478}
phone_numbers['Crystal'] = 6694153652
print(phone_numbers)
#output: {'Kyle': 5513194065, 'Jane': 4086985478, 'Crystal': 6694153652}
print(list(phone_numbers))
print(sorted(phone_numbers))
#output: ['Kyle', 'Jane', 'Crystal']
#        ['Crystal', 'Jane', 'Kyle']
find = input("Whose phone number do you want to look up? ")
if find in phone_numbers:
	print('The Number is:', phone_numbers[find])
else: 
	print('The person cannot be found')

insert_name = input("Who do you want to add into the phone book?\nType in a name: ")
insert_number = int(input("Now enter a number: "))
phone_numbers[insert_name] = insert_number
print(phone_numbers)
'''
'''
basket = dict([('apple', 'green'), ('pineapple' , 'green'), ('orange', 'orange')])
for i,v in basket.items():
	print(i,v)

print(basket)
'''

a = {1: 'edureka' , 2: 'data science', 3: 'python'}
print (a[1])
print(a.get(2))

print (a[4])
#gives you key error
print(a.get(4))
#returns none

