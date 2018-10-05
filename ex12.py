class Person:
    # these are equivalent of static variables in 
    # java or c#. These are one copy of the variable per class.
    # Objects get a copy of these to themselves
    name = None
    city = None

    # each member function of the class must accept at least
    # one parameter, representing the invoking object
    # For example, p1.info() --> Person.info(p1)
    # General convension to represent this arg is to define 
    # a variable called 'self'
    def info(self):
        print('inside Person.info(), id(self) is', id(self))
        print('Name  = {}'.format(self.name))
        print('City  = {}'.format(self.city))
        print()


# end of class Person
# --- --- --- --- --- --- --- --- --- --- ---

def main():
    p1 = Person()
    p1.name = 'Vinod'
    p1.city = 'Bangalore'

    p2 = Person()
    p2.name = 'John'
    p2.city = 'Dallas'

    print('in main(), id of p1 is', id(p1))
    p1.info()
    Person.info(p1) # same as above; but generally not done like this

    print('in main(), id of p2 is', id(p2))
    p2.info()

if __name__=='__main__':
    main()
