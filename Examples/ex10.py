def main():
    filename = input('Enter the filename to read: ')

    try:
        with open(filename) as file:
            for line in file: print(line, end='')
        # file is closed when the control comes out of the 'with' block
    except:
        print('There was an error while processing the file:', filename)

if __name__=='__main__': 
    main()
    print()