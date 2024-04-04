class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.main_idx = 0
        self.nested_idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.nested_idx += 1

        if self.nested_idx == len(self.list_of_list[self.main_idx]):
            self.main_idx += 1
            self.nested_idx = 0

        if self.main_idx == len(self.list_of_list):
            raise StopIteration

        return self.list_of_list[self.main_idx][self.nested_idx]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
