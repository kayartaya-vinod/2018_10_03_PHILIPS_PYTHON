def main():
    while True:
        m = int(input('Enter month: '))
        y = int(input('Enter year: '))
        # as a good practice, import must be done in the beginning of the module
        from myutils import max_days # loads first time; and gets from cache subsequently
        md = max_days(m, y)
        print('{}/{} has a maximum of {} days'.format(m, y, md))

        ans = input('Do you want to try again? yes/no (yes): ')
        if ans == 'no': break

    print('Bye!')

if __name__ == '__main__': main()