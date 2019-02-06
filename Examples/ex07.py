def main():
    filename = input('Enter the filename to read: ')

    try:
        file = open(filename)

        while True:
            line = file.readline()
            if line=='': break
            print(line, end='') # print line,
    except:
        print('There was an error while processing the file:', filename)

if __name__=='__main__': 
    main()
    print()