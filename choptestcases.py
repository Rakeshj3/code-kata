
from chopmain import *
from random import randint

large_list_len = 2*40
large_list_num = randint(0, large_list_len-1)

test_data = [
  (-1, (3, [])),
  (-1, (3, [1])),
  (0, (1, [1])),
  #
  (0, (1, [1, 3, 5])),
  (1, (3, [1, 3, 5])),
  (2, (5, [1, 3, 5])),
  (-1, (0, [1, 3, 5])),
  (-1, (2, [1, 3, 5])),
  (-1, (4, [1, 3, 5])),
  (-1, (6, [1, 3, 5])),
  #
  (0, (1, [1, 3, 5, 7])),
  (1, (3, [1, 3, 5, 7])),
  (2, (5, [1, 3, 5, 7])),
  (3, (7, [1, 3, 5, 7])),
  (-1, (0, [1, 3, 5, 7])),
  (-1, (2, [1, 3, 5, 7])),
  (-1, (4, [1, 3, 5, 7])),
  (-1, (6, [1, 3, 5, 7])),
  (-1, (8, [1, 3, 5, 7])),
  (5, (6, [1, 2, 3, 4, 5, 6, 7])),
  (10, (10, range(0, 16))),
  (0, (0, range(0, 16))),
  (large_list_num, (large_list_num, range(0, large_list_len)))
]


def test_while_iteration(expected, args):
    assert while_iteration(args[0], args[1]) == expected

def test_recursive(expected, args):
    assert recursive(args[0], args[1]) == expected