"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая оставит в множестве только те элементы,
которые есть только в первом множестве и нет во втором
"""


from unittest import result


def diff_update(set_1: set, set_2: set) -> set:
    # TODO вставить код сюда
    set_1.difference_update(set_2)
    return set_1


if __name__ == '__main__':
    some_set = {1, 2, 3, 4}
    diff_update(some_set, {3, 4, 5})
    assert some_set == {1, 2}
    print('Решено!')
