class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.stack = []
        self.current_iterator = iter(self.list_of_list)
        return self

    def __next__(self):
        while True:
            try:
                self.item = next(self.current_iterator)
            except StopIteration:
                if not self.stack:
                    raise StopIteration
                else:
                    self.current_iterator = self.stack.pop()
                    continue

            if isinstance(self.item, list):
                self.stack.append(self.current_iterator)
                self.current_iterator = iter(self.item)
            else:
                return self.item


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
