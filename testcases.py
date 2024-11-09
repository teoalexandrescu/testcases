#Teodora Alexandrescu
import unittest

def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):  
        swapped = False  
        for j in range(n - i - 1):  
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
    return array


class TestBubbleSort(unittest.TestCase):
    
    #positive case
    def test_sort_positive_case(self):
        array = [78, 2, 120, 3, 2, 16, 9]
        sorted_array = [2, 2, 3, 9, 16, 78, 120]
        self.assertEqual(bubble_sort(array), sorted_array)
    

    #negative case
    def test_sort_negative_case(self):
        array = ['b', 'apple', 647]
        with self.assertRaises(TypeError):
            bubble_sort(array)


    #performance cases
    def test_sort_perfomance_cases(self):
        small_array = [165, 3]
        sorted_small_array = [3, 165]
        self.assertEqual(bubble_sort(small_array), sorted_small_array)

        large_array = list(range(2000, 0, -1))  
        sorted_large_array = list(range(1, 2001))  
        self.assertEqual(bubble_sort(large_array), sorted_large_array)

        partially1_sorted_array = [2, 1, 3, 4, 5, 6, 8, 7]
        sorted_partially1_array = list(range(1, 9))
        self.assertEqual(bubble_sort(partially1_sorted_array), sorted_partially1_array)

        partially2_sorted_array = [1, 2, 3, 5, 4, 6, 7, 8,]
        sorted_partially2_array = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(bubble_sort(partially2_sorted_array), sorted_partially2_array)
    

    #boundary cases
    def test_sort_boundary_cases(self):
        self.assertEqual(bubble_sort([]), [])

        self.assertEqual(bubble_sort([3]), [3])
 
        duplicate_array = [1, 1, 1, 1, 1, 1, 1, 1, 5, 6, 43, 23, 1, 1, 1, 1, 1, 1, 10, 
               10, 10, 1, 1, 1, 23, 43, 5, 6, 8, 1, 1, 10, 5, 5, 5, 5, 102]
        sorted_duplicate_array = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                      1, 5, 5, 5, 5, 5, 5, 6, 6, 8, 10, 10, 10, 10, 23, 23, 
                      43, 43, 102]
        self.assertEqual(bubble_sort(duplicate_array), sorted_duplicate_array)

        already_sorted_array = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(already_sorted_array), already_sorted_array)
        
        reverse_sorted_array = [20, 19, 14, 9, 3]
        self.assertEqual(bubble_sort(reverse_sorted_array), [3, 9, 14, 19, 20])
        
        
    #idempotency cases
    def test_sort_idempotency_case(self):
        array1 = [2, 9, 3, 2, 78, 16, 120]
        sorted_array1 = bubble_sort(array1.copy())
        self.assertEqual(bubble_sort(sorted_array1), sorted_array1)

        array2 = [2, 2, 3, 9, 16, 78, 120]
        sorted_array2 = bubble_sort(array2.copy())
        self.assertEqual(bubble_sort(sorted_array2), sorted_array2)

       
if __name__ == '__main__':
    unittest.main()
