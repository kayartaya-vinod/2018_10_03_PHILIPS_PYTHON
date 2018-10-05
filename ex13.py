class Person:
    # constructor
    def __init__(self, name=None, city='Bangalore'):
        self.__name = name # self.__name gets newly created
        self.__city = city # self.__city gets newly created

    def info(self):
        print('Name =', self.__name)
        print('City =', self.__city)
        print()

def main():
    p1 = Person('Vinod')
    p2 = Person('John', 'Dallas')

    p1.info()
    p2.info()

    p2.__name = 'Jane Doe' # does not change the member '__name'
    p2.info()

if __name__=='__main__':
    main()