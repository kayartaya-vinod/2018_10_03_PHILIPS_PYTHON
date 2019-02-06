from myutils import factorial

def main():
    num = input('Enter a number: ')
    num = int(num)

    fact = factorial(num)
    
    print('Factorial of {} is {}'.format(num, fact))

# print('Name of this module is ', __name__)
# When you import this module, the value of __name__ is 'ex03'
# When you execute this script as a program, __name__ is '__main__'

# Call the main() if this script is executed as a program, but 
# not when this script is imported as a library module in another program
if __name__ == '__main__':
    main()