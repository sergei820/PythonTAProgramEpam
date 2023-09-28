# 1. Implement a function that flatten incoming data:
# non-iterables and elements from iterables (any nesting depth should be supported)
# function should return an iterator (generator function)
# don't use third-party libraries

def merge_elems(*elems):
    for elem in elems:
        # if is_iterable(elem):
        if hasattr(elem, '__iter__') and not isinstance(elem, (str, bytes)):
            yield from merge_elems(*elem)
        else:
            yield elem


def is_iterable(obj):
    try:
        if iter(obj):
            return True
    except TypeError:
        return False



# example input
a = [1, 2, 3]
b = 6
c = 'zhaba'
d = [[1, 2], [3, 4]]

for _ in merge_elems(a, b, c, d):
    print(_, end=' ')

# output: 1 2 3 6 z h a b a 1 2 3 4
