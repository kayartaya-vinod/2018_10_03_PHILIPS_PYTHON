def main():
    filename = input('Enter the filename to read: ')

    try:
        file = open(filename)
        for line in file.readlines():
            print(line, end='')
        
        file.close() # close the file after working with it as a good practice
    except:
        print('There was an error while processing the file:', filename)

if __name__=='__main__': 
    main()
    print()