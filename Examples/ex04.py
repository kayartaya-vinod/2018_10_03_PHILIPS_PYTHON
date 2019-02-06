# from myutils import is_leap, max_days
# from myutils import *
from myutils import max_days as md, is_leap

def main():
    m = int(input('Enter month: '))
    y = int(input('Enter year: '))
    d = md(m, y)
    print('{}/{} has {} days'.format(m, y, d))

    
def main_1():
    year = int(input('Enter year: '))
    result = is_leap(year)

    print('is_leap({}) is {}'.format(year, result))


if __name__ == '__main__':
    main()