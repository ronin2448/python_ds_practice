blah = [x for x in range(0,10)]
blah
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


import math
blah = [ math.pow(2,x) for x in range(0,10)]
blah
[1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0, 256.0, 512.0]



blah = [ math.pow(2,x) + 4 for x in range(0,10)]
blah
[5.0, 6.0, 8.0, 12.0, 20.0, 36.0, 68.0, 132.0, 260.0, 516.0]


def make_list_slower(blah):
    result = []
    for elem in blah:
        result.append(elem)
    return result

#doesn't build list incrementally
def make_list_faster(blah):
    return [elem for elem in blah]