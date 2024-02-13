#tasks 2 solution
import types


def flat_generator(_list):
    _index = 0
    _nested_index = 0
    while _index < len(_list):
        while _nested_index < len(_list[_index]):
            yield _list[_index][_nested_index]
            _nested_index += 1
        _nested_index = 0
        _index += 1

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

def test_0():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for i in flat_generator(list_of_lists_1):
        print(i)



if __name__ == '__main__':
    test_2()
    #test_0()