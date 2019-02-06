from ex14 import Person

class Test(object):
    def __init__(self, **kwargs):
        # print('from inisde of Test.__init__')
        pass

class InvalidSalaryException(Exception):
    def __init__(self, *args):
        # super().__init__(*args)
        Exception.__init__(self, *args)

class Employee(Person, Test):
    def __init__(self, **kwargs):
        Test.__init__(self, **kwargs)
        Person.__init__(self, **kwargs)

        self.id = kwargs.get('id')
        self.salary = kwargs.get('salary', 15000)

        # super().__init__(**kwargs) # calls the constructor in the first inherited class
        # print('from inisde of Employee.__init__')

    @property
    def id(self): return self.__id
    @id.setter
    def id(self, id): self.__id = id

    @property
    def salary(self): return self.__salary
    
    @salary.setter
    def salary(self, salary): 
        if type(salary) not in (int, float):
            raise InvalidSalaryException(
                'Salary must be a number', type(salary))
        if salary < 15000:
            raise InvalidSalaryException('Salary must be >= 15000')

        self.__salary = salary

    def __str__(self):
        return 'Employee ({}, id={}, salary={})'.format(
            Person.__str__(self), self.id, self.salary)
    # Person.__str__(self) --> super().__str__()

    def __add__(self, value): 
        # self + value
        # e1 + 5000
        # e1 + ' Kumar'
        if type(value) == str: return self.name + value
        if type(value) in (int, float): return self.salary + value
        raise TypeError('Invalid type of value supplied for this operation')

    def __iadd__(self, value):
        # self += value
        # e1 += 4500
        # e1 += ' Kumar'
        if type(value) == str:
            self.name += value
        elif type(value) in (int, float): 
            self.salary += value
        else:
            raise TypeError('Invalid type of value supplied for this operation')
        return self

def main():
    e1 = Employee(name='Ramesh', id=1122, salary=20000)
    e2 = Employee(name='Vijay', id=2345)

    print(e1)
    print(e2)

    new_sal = e1 + 5000
    new_name = e1 + ' Kumar'

    print('new_sal', new_sal)
    print('new_name', new_name)

    print(e1) # no change in e1's data

    e1 += 999 # should increase the salary of e1 by 4500
    e1 += ' Rao' # should append ' Kumar' to e1's name

    print(e1) # e1's data should change

    # e1.salary = 10000

if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print('OOPS!', e)