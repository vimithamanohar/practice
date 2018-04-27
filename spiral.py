import math
import unittest


def get_line(arr, x, y, ln, dx, dy):
    ret = []
    for i in range(ln):
        ret.append(arr[x][y])
        x = x + dx
        y = y + dy
    return ret


def get_square(arr, x, y, ln):
    if ln == 0:
        return []

    if ln == 1:
        return [arr[x][y]]

    ret = []
    ret.extend(get_line(arr, x, y, ln - 1, 0, 1))
    ret.extend(get_line(arr, x, y + ln - 1, ln - 1, 1, 0))
    ret.extend(get_line(arr, x + ln - 1, y + ln - 1, ln - 1, 0, -1))
    ret.extend(get_line(arr, x + ln - 1, y, ln - 1, -1, 0))
    return ret


def get_spiral(arr):
    arr_len = len(arr)
    if arr_len == 0:
        return []

    ret = []
    for i in range(math.ceil(arr_len / 2)):
        ret.extend(get_square(arr, i, i, arr_len - i * 2))
    return ret


class TestSpiral(unittest.TestCase):
    def test_len_3(self):
        a = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
        self.assertEqual(get_spiral(a), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_len_4(self):
        a = [[1,   2,  3,  4],
             [5,   6,  7,  8],
             [9,  10, 11, 12],
             [13, 14, 15, 16]]
        self.assertEqual(get_spiral(a), [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])

    def test_len_1(self):
        a = [[1]]
        self.assertEqual(get_spiral(a), [1])

    def test_len_0(self):
        a = []
        self.assertEqual(get_spiral(a), [])


if __name__ == '__main__':
    unittest.main()
