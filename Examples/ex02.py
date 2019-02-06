"""This program will ask the user to enter a number
and print if it is less / more than 100
"""

num = input('Enter a number: ') # returns a str
num = int(num) # create a new 'int' instance by supplying 'str' object

if num < 100:
    print('%d is less than %d' % (num, 100))
else:
    print('{} is more than or equals to {}'.format(num, 100));


print('End of script execution!')