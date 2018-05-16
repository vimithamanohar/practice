import unittest

def zigzag(a):
    if len(a) == 1:
        return 1
    zig_len = 0
    max_len = 0
    start = 0
    i = 0
    while i < len(a) - 1:
        if i == 0:
            if a[i] == a[i + 1]:
                max_len = 1
                zig_len = 1
                start = 1
            else:
                zig_len = 2

        else:
            if (a[i - 1] > a[i]) and (a[i] < a[i + 1]):
                zig_len = i + 1 - start + 1

            elif (a[i - 1] < a[i]) and (a[i] > a[i + 1]):
                zig_len = i + 1 - start + 1

            else:
                zig_len = 0
                start = i

        if zig_len > max_len:
            max_len = zig_len

        i = i + 1
    return max_len


class Testzigzag(unittest.TestCase):
    def test_case_1(self):
        a = [9, 8, 8, 5, 3, 5, 3, 2, 8, 6]

        self.assertEqual(zigzag(a), 4)

    def test_case_1(self):
        a = [4,4]

        self.assertEqual(zigzag(a), 1)

    def test_case_1(self):
        a = [2, 1, 4, 4, 1, 4, 4, 1, 2, 0, 1, 0, 0, 3, 1, 3, 4, 1, 3, 4]

        self.assertEqual(zigzag(a), 6)



if __name__ == '__main__':
    unittest.main()

