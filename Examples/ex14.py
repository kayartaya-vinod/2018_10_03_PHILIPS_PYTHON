class Person(object):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.phone = kwargs.get('phone')
        self.age = kwargs.get('age')
        self.city = kwargs.get('city', 'Bangalore')
        # print('from inisde of Person.__init__')

    def __str__(self):
        '''this function returns the textual representation
        of the object referred by "self"'''
        return 'Person(name={}, city={}, email={}, phone={}, age={})'.format(self.__name, self.__city, self.__email, self.__phone, self.__age)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if type(age) not in (int, type(None)) : 
            raise TypeError('Age must be integer!')
        if age!=None and (age<1 or age>120): 
            raise ValueError('Invalid age for a person!')
        self.__age = age

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

def main():
    p1 = Person(name='Vinod', email='vinod@vinod.co')
    p1.age = 45 # must invoke a function that accepts a number as arg and assigns to the private member variable __age. For example, p1.age(45)
    p1.phone = '9731424784'

    print(p1)

    p2 = Person(name='Ramesh', age=333)
    print(p2)

if __name__=='__main__':
    try: 
        main()
    except Exception as e:
        print('There was an error: ', e)
