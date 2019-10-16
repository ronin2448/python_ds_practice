def countdown(num):
    print('Starting')
    while num > 0:
        print("Starting new iteration")
        yield num
        num -= 1



if __name__ == '__main__':

    val = countdown(5)

    print(val)

    print(next(val))
    print("New call to generator")
    print(next(val))
    print(next(val))
    print(next(val))
    print(next(val))


    my_list = ['a', 'b', 'c', 'd']  # list comphrension

    print("\n***** Generator In For Loop Ex *****\n")

    def generator_iterator(my_list):
        for x in my_list:
            yield x

    for val in generator_iterator(my_list):
        print(val)

    print("\n***** Generator Short hand Ex *****\n")

    gen_obj = ('{} is an elmenet in list'.format(x) for x in my_list)  # shorthand for generator
    for val in gen_obj:
        print(val)

