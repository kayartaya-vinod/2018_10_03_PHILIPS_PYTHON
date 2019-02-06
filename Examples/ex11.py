def add(*nums):
    return sum([n for n in nums if type(n) in (int, float)])

def test_fn1(name, *args):
    print('name = ', name)
    print('args = ', args)
    print('-'*80)

def print_info(name, email, phone, city='Bangalore'):
    print('name  = ' + name)
    print('email = ' + email)
    print('phone = ' + phone)
    print('city  = ' + city )
    print()

def main_1():
    # missing optional parameter in positional parameter
    print_info('Vinod', 'vinod@vinod.co', '9731424784')

    # use as named parameter
    print_info(email='john@example.com', phone='5559282221', name='John Doe')

    input1 = ('Jane Doe', 'jane@xmpl.com', '4646488221', 'Dallas')
    print_info(*input1) # destructring the collection type (list/tuple)

    input2 = {'name': 'Smith', 'phone': '8272672622', 'city': 'Washington', 'email': 'smith@xmpl.com'}

    # *input2 --> input2.keys()
    # **input2 --> input2.values()
    print_info(**input2)


def test_fn2(name, **kwargs):
    print('Name is', name)
    print('Keyword Args is', kwargs)
    print()

def test_fn3(name, *args, **kwargs):
    print('Name is', name)
    print('Arbitrary Args is', args)
    print('Keyword Args is', kwargs)
    print()

def main():

    test_fn3('Vinod')
    test_fn3('Vinod', 'vinod@vinod.co')
    test_fn3('Vinod', 'vinod@vinod.co', 'Bangalore')
    test_fn3('Vinod', 'vinod@vinod.co', city='Bangalore', phone='9731424784')
    test_fn3('Vinod', email='vinod@vinod.co', city='Bangalore', phone='9731424784')

    # test_fn1('vinod', 'vinod@vinod.co', '9731424784', 'Bangalore')
    # test_fn1('vinod', 'vinod@vinod.co')
    # test_fn1('vinod')

    # x = add(12, 55, 500, 33, 'x', 'y', 200)
    # print('x = ', x)

    # test_fn2('Vinod')
    # test_fn2(name='Vinod')
    # test_fn2('Vinod', city='Bangalore', email='vinod@vinod.co')


if __name__=='__main__': main()

