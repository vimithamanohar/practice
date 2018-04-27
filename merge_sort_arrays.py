import unittest


def merge_sorted_arrays(arr1 , arr2):
    ln1 = len(arr1)
    ln2 = len(arr2)

    arr3 = []
    i = j = 0

    while i < ln1 and j < ln2:
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1

        elif arr2[j] < arr1[i]:
            arr3.append(arr2[j])
            j += 1

        else:
            arr3.append(arr1[i])
            i += 1
            j += 1

    for m in range(i, ln1):
        arr3.append(arr1[m])

    for n in range(j, ln2):
        arr3.append(arr2[n])

    return arr3


class TestLongSpan(unittest.TestCase):
    def test_case_1(self):
        a = [5, 8, 9]
        b = [4, 7, 8]
        self.assertEqual(merge_sorted_arrays(a , b), [4, 5, 7, 8, 9])

    def test_case_2(self):
        a = [1, 3, 4, 5]
        b = [2, 4, 6, 8]
        self.assertEqual(merge_sorted_arrays(a , b), [1, 2, 3, 4, 5, 6, 8])

    def test_case3(self):
        a = [1, 3, 5, 7]
        b = [2, 4, 6, 8]
        self.assertEqual(merge_sorted_arrays(a , b), [1, 2, 3, 4, 5, 6, 7, 8])


if __name__ == '__main__':
    unittest.main()

