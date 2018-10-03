'''
This is a utility module with few useful functions

Author: Vinod <vinod@vinod.co>
Date: 3/10/2018
'''

# long factorial(int num) {
# }

def factorial(num):
    '''
    Returns the factorial of the input number. Factorial of a number less than or equals to 1 will be returned as 1
    '''
    if num<1:
        print('Input must be >= 1')
        
    f = 1
    while num > 1:
        f = f * num
        num = num - 1
    
    return f

def is_leap(year):
    # year % 4 ==0 && year % 100 !=0
    # year % 400 == 0

    # if year % 400 == 0 or (year % 4 ==0 and year % 100 !=0): return True
    # else: return False

    return year % 400 == 0 or (year % 4 ==0 and year % 100 !=0)

def max_days(month, year):
    if month == 2:
        # return 29 if is_leap(year) else 28
        if is_leap(year):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31
