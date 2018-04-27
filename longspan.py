import unittest


def longest_common_sum(arr1 , arr2):
    ln1 = len(arr1)
    ln2 = len(arr2)

    if ln1 != ln2:
        return -1

    maxspan = 0
    for i in range(ln1):
        sum1 = 0
        sum2 = 0
        for j in range(i, ln2):

            sum1 = sum1 + arr1[j]
            sum2 = sum2 + arr2[j]

            if sum1 == sum2:
                span = j-i+1

                if span > maxspan :
                    maxspan = span

    return maxspan


class TestLongSpan(unittest.TestCase):
    def test_case_1(self):
        a = [0, 1, 0, 1, 1, 1, 1]
        b = [1, 1, 1, 1, 1, 0, 1]
        self.assertEqual(longest_common_sum(a , b), 6)

    def test_case_2(self):
        a = [0, 1, 0, 0, 0, 0]
        b = [1, 0, 1, 0, 0, 1]
        self.assertEqual(longest_common_sum(a , b), 4)

    def test_case3(self):
        a = [0, 0, 0]
        b = [1, 1, 1]
        self.assertEqual(longest_common_sum(a , b), 0)

    def test_case_4(self):
        a = [0, 0, 1, 0]
        b = [1, 1, 1, 1]
        self.assertEqual(longest_common_sum(a , b), 1)


if __name__ == '__main__':
    unittest.main()

