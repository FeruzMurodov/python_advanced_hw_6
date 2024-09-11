from random import *


def find_differences(list1: list, list2: list) -> list:
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.difference(set2).union(set2.difference(set1)))


if __name__ == '__main__':
    list_1 = [randrange(0, 10) for i in range(5)]
    print(list_1)
    list_2 = [randrange(0, 10) for i in range(5)]
    print(list_2)
    print(find_differences(list_1, list_2))

__all__ = ['find_differences']
