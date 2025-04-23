
import unittest
from main import *

class TestMinSum(unittest.TestCase):
  def test_cases(self):
    arr = [3, 4, -8, 4, 2, 1, 7, -2, 1] 
    self.assertEqual(max_sum(arr), Solution(4, 7, 14))

    arr = [1, -5, -1, -3, -5]
    self.assertEqual(max_sum(arr), Solution(1, 1, 1))

    with self.assertRaises(IllegalArgumentError):
      arr = []
      sol = max_sum(arr)

    arr = [-3, -4, -8, -4, -2, -4, -7, -2, -1] 
    self.assertEqual(max_sum(arr), Solution(9, 9, -1))

    arr = [-1, -4, -8] 
    self.assertEqual(max_sum(arr), Solution(1, 1, -1))

    arr = [-4, -1, -8] 
    self.assertEqual(max_sum(arr), Solution(2, 2, -1))

    arr = [4, 5]
    self.assertEqual(max_sum(arr), Solution(1, 2, 9))

    arr = [4, 5, -1, 2, -5, -6]
    self.assertEqual(max_sum(arr), Solution(1, 4, 10))

    arr = [4, -2, 1]
    self.assertEqual(max_sum(arr), Solution(1, 1, 4))

    arr = [4, -2, 1, 3]
    self.assertEqual(max_sum(arr), Solution(1, 4, 6))

    arr = [4, -5, 2, 3]
    self.assertEqual(max_sum(arr), Solution(3, 4, 5))

    arr = [1]
    self.assertEqual(max_sum(arr), Solution(1, 1, 1))

    arr = [-1]
    self.assertEqual(max_sum(arr), Solution(1, 1, -1))

    arr = [1, 0, 4, -2, -1, 1, -4, 1]
    self.assertEqual(max_sum(arr), Solution(1, 3, 5))

    arr = [1, 0, 4, -2, -1, 4, -4, 1]
    self.assertEqual(max_sum(arr), Solution(1, 6, 6))

    arr = [-2, 1, 2, -3]
    self.assertEqual(max_sum(arr), Solution(2, 3, 3))

    arr = [-2, -1, 2, -3]
    self.assertEqual(max_sum(arr), Solution(3, 3, 2))
    
    arr = [-1, 7, -8, 3, 5, -1]
    self.assertEqual(max_sum(arr), Solution(4, 5, 8))

    # Aus der Vorlesung
    arr = [-28, -54, 88, -83, 51, 56, -57, 0, 82, -68]
    self.assertEqual(max_sum(arr), Solution(3, 9, 137))



if __name__ == "__main__":
  unittest.main()

