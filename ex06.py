#! /usr/local/bin/python3

def print_table_1():
    num = int(input('Enter a number: '))
    for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print('{} X {} = {}'.format(num, n, num*n))

def print_table(num, limit=10):
    for n in range(1, limit + 1):
        print('{} X {} = {}'.format(num, n, num*n))

def main():
    num = int(input('Enter a number: '))
    print_table(num)

if __name__=='__main__': 
    main()