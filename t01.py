import json

def csv2json(filename, indent=4):
    '''This method accepts a readable CSV filename as input,
    and returns a string representing the data in JSON format
    '''

    if type(filename) != str: raise TypeError('filename must be a str')

    try:
        with open(filename, 'rb') as file:
            headers = file.readline().strip().split(',')
            lst = []
            for line in file: # process the second line onwards
                values = line.strip().split(',')
                data = dict(zip(headers, values))
                lst.append(data)
            return json.dumps(lst, indent=indent)
    except:
        raise ValueError('Invalid filename: ' + filename)

if __name__=='__main__': 
    output = csv2json('phonebook.csv')
    print(output)